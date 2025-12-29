#!/usr/bin/env python3
"""
Cybersyn Chair Controller
=========================
Raspberry Pi Zero 2 W firmware for armrest button control.

Hardware:
- 9 buttons in original Cybersyn layout
- Optional: OLED display, NFC reader, haptic feedback
- MQTT for Home Assistant integration
"""

import asyncio
import json
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Optional

# Hardware abstraction - use gpiozero on actual Pi
try:
    from gpiozero import Button, LED
    HARDWARE_AVAILABLE = True
except ImportError:
    HARDWARE_AVAILABLE = False
    print("Running in simulation mode (no GPIO)")

# MQTT client
try:
    import paho.mqtt.client as mqtt
    MQTT_AVAILABLE = True
except ImportError:
    MQTT_AVAILABLE = False
    print("MQTT not available - install paho-mqtt")


class ButtonName(Enum):
    """Original Cybersyn button layout."""
    # Top row - data screen selection
    DATA_1 = "data_1"
    DATA_2 = "data_2"
    DATA_3 = "data_3"
    # Middle row - navigation
    NAV_1 = "nav_1"
    NAV_2 = "nav_2"
    NAV_3 = "nav_3"
    NAV_4 = "nav_4"
    NAV_5 = "nav_5"
    # Bottom row - index/home
    INDEX = "index"


@dataclass
class ButtonConfig:
    """GPIO pin configuration for a button."""
    name: ButtonName
    gpio_pin: int
    led_pin: Optional[int] = None


# Default GPIO pin mapping (adjust for your wiring)
DEFAULT_BUTTON_CONFIG = [
    ButtonConfig(ButtonName.DATA_1, gpio_pin=17, led_pin=27),
    ButtonConfig(ButtonName.DATA_2, gpio_pin=22, led_pin=10),
    ButtonConfig(ButtonName.DATA_3, gpio_pin=23, led_pin=9),
    ButtonConfig(ButtonName.NAV_1, gpio_pin=24),
    ButtonConfig(ButtonName.NAV_2, gpio_pin=25),
    ButtonConfig(ButtonName.NAV_3, gpio_pin=8),
    ButtonConfig(ButtonName.NAV_4, gpio_pin=7),
    ButtonConfig(ButtonName.NAV_5, gpio_pin=12),
    ButtonConfig(ButtonName.INDEX, gpio_pin=16, led_pin=20),
]


class CybersynController:
    """Main controller for a Cybersyn chair."""

    def __init__(
        self,
        chair_id: str = "chair_1",
        mqtt_broker: str = "localhost",
        mqtt_port: int = 1883,
        button_config: list[ButtonConfig] = None,
    ):
        self.chair_id = chair_id
        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        self.button_config = button_config or DEFAULT_BUTTON_CONFIG

        self.buttons: dict[ButtonName, Button] = {}
        self.leds: dict[ButtonName, LED] = {}
        self.mqtt_client: Optional[mqtt.Client] = None

        self._callbacks: dict[ButtonName, list[Callable]] = {
            btn.name: [] for btn in self.button_config
        }

    def setup_hardware(self):
        """Initialize GPIO buttons and LEDs."""
        if not HARDWARE_AVAILABLE:
            print(f"[{self.chair_id}] Simulating hardware setup")
            return

        for config in self.button_config:
            # Setup button with pull-up resistor
            self.buttons[config.name] = Button(
                config.gpio_pin,
                pull_up=True,
                bounce_time=0.05  # 50ms debounce
            )
            self.buttons[config.name].when_pressed = (
                lambda name=config.name: self._on_button_pressed(name)
            )
            self.buttons[config.name].when_released = (
                lambda name=config.name: self._on_button_released(name)
            )

            # Setup LED if configured
            if config.led_pin:
                self.leds[config.name] = LED(config.led_pin)

        print(f"[{self.chair_id}] Hardware initialized: {len(self.buttons)} buttons")

    def setup_mqtt(self):
        """Connect to MQTT broker."""
        if not MQTT_AVAILABLE:
            print(f"[{self.chair_id}] MQTT not available")
            return

        self.mqtt_client = mqtt.Client(client_id=f"cybersyn_{self.chair_id}")
        self.mqtt_client.on_connect = self._on_mqtt_connect
        self.mqtt_client.on_message = self._on_mqtt_message

        try:
            self.mqtt_client.connect(self.mqtt_broker, self.mqtt_port)
            self.mqtt_client.loop_start()
            print(f"[{self.chair_id}] Connected to MQTT broker at {self.mqtt_broker}")
        except Exception as e:
            print(f"[{self.chair_id}] MQTT connection failed: {e}")

    def _on_mqtt_connect(self, client, userdata, flags, rc):
        """Handle MQTT connection."""
        # Subscribe to commands for this chair
        topic = f"cybersyn/chair/{self.chair_id}/command/#"
        client.subscribe(topic)

        # Publish online status
        self._publish_status("online")

    def _on_mqtt_message(self, client, userdata, msg):
        """Handle incoming MQTT messages."""
        try:
            payload = json.loads(msg.payload.decode())
            # Handle LED control commands
            if "/led/" in msg.topic:
                button_name = msg.topic.split("/")[-1]
                self._set_led(ButtonName(button_name), payload.get("state", False))
        except Exception as e:
            print(f"[{self.chair_id}] Error processing message: {e}")

    def _on_button_pressed(self, button_name: ButtonName):
        """Handle button press event."""
        print(f"[{self.chair_id}] Button pressed: {button_name.value}")

        # Publish to MQTT
        self._publish_button_event(button_name, "pressed")

        # Trigger registered callbacks
        for callback in self._callbacks.get(button_name, []):
            callback(button_name, "pressed")

        # Visual feedback
        if button_name in self.leds:
            self.leds[button_name].on()

    def _on_button_released(self, button_name: ButtonName):
        """Handle button release event."""
        print(f"[{self.chair_id}] Button released: {button_name.value}")

        # Publish to MQTT
        self._publish_button_event(button_name, "released")

        # Trigger registered callbacks
        for callback in self._callbacks.get(button_name, []):
            callback(button_name, "released")

        # Turn off LED feedback
        if button_name in self.leds:
            self.leds[button_name].off()

    def _publish_button_event(self, button_name: ButtonName, state: str):
        """Publish button event to MQTT."""
        if not self.mqtt_client:
            return

        topic = f"cybersyn/chair/{self.chair_id}/button/{button_name.value}"
        payload = json.dumps({
            "state": state,
            "chair_id": self.chair_id,
            "button": button_name.value,
        })
        self.mqtt_client.publish(topic, payload)

    def _publish_status(self, status: str):
        """Publish chair status to MQTT."""
        if not self.mqtt_client:
            return

        topic = f"cybersyn/chair/{self.chair_id}/status"
        payload = json.dumps({
            "status": status,
            "chair_id": self.chair_id,
        })
        self.mqtt_client.publish(topic, payload, retain=True)

    def _set_led(self, button_name: ButtonName, state: bool):
        """Set LED state."""
        if button_name in self.leds:
            if state:
                self.leds[button_name].on()
            else:
                self.leds[button_name].off()

    def register_callback(
        self,
        button_name: ButtonName,
        callback: Callable[[ButtonName, str], None]
    ):
        """Register a callback for button events."""
        self._callbacks[button_name].append(callback)

    def run(self):
        """Run the controller main loop."""
        self.setup_hardware()
        self.setup_mqtt()

        print(f"[{self.chair_id}] Controller running. Press Ctrl+C to exit.")

        try:
            # Keep running
            while True:
                asyncio.get_event_loop().run_until_complete(asyncio.sleep(1))
        except KeyboardInterrupt:
            print(f"\n[{self.chair_id}] Shutting down...")
            self._publish_status("offline")
            if self.mqtt_client:
                self.mqtt_client.loop_stop()


# =============================================================================
# Modular Expansion System
# =============================================================================

class ArmrestModule:
    """Base class for armrest expansion modules."""

    MODULE_TYPE = "base"

    def __init__(self, controller: CybersynController):
        self.controller = controller
        self.enabled = False

    def setup(self):
        """Initialize the module hardware."""
        raise NotImplementedError

    def poll(self) -> dict:
        """Read current module state."""
        raise NotImplementedError

    def cleanup(self):
        """Cleanup module resources."""
        pass


class OLEDDisplayModule(ArmrestModule):
    """1.3" OLED status display in armrest."""

    MODULE_TYPE = "oled_display"

    def __init__(self, controller: CybersynController, i2c_address: int = 0x3C):
        super().__init__(controller)
        self.i2c_address = i2c_address
        self.display = None

    def setup(self):
        """Initialize OLED display."""
        try:
            # Requires: pip install luma.oled
            from luma.core.interface.serial import i2c
            from luma.oled.device import sh1106

            serial = i2c(port=1, address=self.i2c_address)
            self.display = sh1106(serial)
            self.enabled = True
            print(f"[OLED] Display initialized at 0x{self.i2c_address:02X}")
        except Exception as e:
            print(f"[OLED] Failed to initialize: {e}")

    def show_text(self, text: str, font_size: int = 16):
        """Display text on OLED."""
        if not self.display:
            return

        from PIL import Image, ImageDraw, ImageFont

        img = Image.new("1", (self.display.width, self.display.height), "black")
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), text, fill="white")
        self.display.display(img)

    def poll(self) -> dict:
        return {"enabled": self.enabled}


class NFCReaderModule(ArmrestModule):
    """RC522 NFC reader for user identification."""

    MODULE_TYPE = "nfc_reader"

    def __init__(self, controller: CybersynController):
        super().__init__(controller)
        self.reader = None
        self.last_uid = None

    def setup(self):
        """Initialize NFC reader."""
        try:
            # Requires: pip install mfrc522
            from mfrc522 import SimpleMFRC522
            self.reader = SimpleMFRC522()
            self.enabled = True
            print("[NFC] Reader initialized")
        except Exception as e:
            print(f"[NFC] Failed to initialize: {e}")

    def poll(self) -> dict:
        """Check for NFC card."""
        if not self.reader:
            return {"uid": None}

        try:
            uid, _ = self.reader.read_no_block()
            if uid and uid != self.last_uid:
                self.last_uid = uid
                # Publish to MQTT
                if self.controller.mqtt_client:
                    topic = f"cybersyn/chair/{self.controller.chair_id}/nfc"
                    payload = json.dumps({"uid": str(uid)})
                    self.controller.mqtt_client.publish(topic, payload)
            return {"uid": str(uid) if uid else None}
        except Exception:
            return {"uid": None}


class HapticFeedbackModule(ArmrestModule):
    """Vibration motor for button feedback."""

    MODULE_TYPE = "haptic"

    def __init__(self, controller: CybersynController, gpio_pin: int = 21):
        super().__init__(controller)
        self.gpio_pin = gpio_pin
        self.motor = None

    def setup(self):
        """Initialize haptic motor."""
        if HARDWARE_AVAILABLE:
            from gpiozero import PWMOutputDevice
            self.motor = PWMOutputDevice(self.gpio_pin)
            self.enabled = True

            # Register for all button presses
            for button_name in ButtonName:
                self.controller.register_callback(
                    button_name,
                    self._on_button_event
                )
            print("[Haptic] Motor initialized")

    def _on_button_event(self, button_name: ButtonName, state: str):
        """Vibrate on button press."""
        if state == "pressed" and self.motor:
            self.pulse(duration=0.05, intensity=0.7)

    def pulse(self, duration: float = 0.1, intensity: float = 1.0):
        """Pulse the vibration motor."""
        if self.motor:
            self.motor.value = intensity
            asyncio.get_event_loop().call_later(
                duration,
                lambda: setattr(self.motor, 'value', 0)
            )

    def poll(self) -> dict:
        return {"enabled": self.enabled}


# =============================================================================
# Main Entry Point
# =============================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Cybersyn Chair Controller")
    parser.add_argument(
        "--chair-id",
        default="chair_1",
        help="Unique identifier for this chair (1-7)"
    )
    parser.add_argument(
        "--mqtt-broker",
        default="localhost",
        help="MQTT broker address"
    )
    parser.add_argument(
        "--mqtt-port",
        type=int,
        default=1883,
        help="MQTT broker port"
    )
    args = parser.parse_args()

    # Create and run controller
    controller = CybersynController(
        chair_id=args.chair_id,
        mqtt_broker=args.mqtt_broker,
        mqtt_port=args.mqtt_port,
    )

    # Optional: Add expansion modules
    # oled = OLEDDisplayModule(controller)
    # oled.setup()
    # haptic = HapticFeedbackModule(controller)
    # haptic.setup()

    controller.run()
