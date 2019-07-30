# M2M_LcdDisplay

from enum import Enum
from gpiozero import Button, LED
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

class Leds(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    NONE = 4
    ALL = 5

class KeypadDisplay(object):

    def __init__(self, lcd_address, button_pins = [17, 18, 27, 22, 23, 24, 25], led_pins = [16, 20, 21]):
        """Initializes the KeypadDisplay object

        button_pins: A list of 7 GPIO pins used for button inputs, order is A, B, L, U, D, R, C

        pin Usage
        ---|-----------
        17 | Button A
        18 | Button B
        27 | Button Left
        22 | Button Up
        23 | Button Down
        24 | Button right
        25 | Button C

        led_pins: A list of 3 GPIO pins to use for led outputs, order is R, G, B

        pin Usage
        ---|----------
        16 | Red LED
        20 | Yellow LED
        21 | Green LED
        """
        self.button_a = Button(button_pins[0])
        self.button_b = Button(button_pins[1])
        self.button_left = Button(button_pins[2])
        self.button_up = Button(button_pins[3])
        self.button_down = Button(button_pins[4])
        self.button_right = Button(button_pins[5])
        self.button_c = Button(button_pins[6])
        self.led_red = LED(led_pins[0])
        self.led_yellow = LED(led_pins[1])
        self.led_green = LED(led_pins[2])
        self.lcd = LCD(I2CPCF8574Interface(lcd_address), num_rows=4, num_cols=20)
    
    def set_led(self, value) -> Leds:
        """Sets the LED's according to the passed value"""
        self.led_red.off()
        self.led_yellow.off()
        self.led_green.off()
        if value in [Leds.RED, Leds.ALL]:
            self.led_red.on()
        if value in [Leds.YELLOW, Leds.ALL]:
            self.led_yellow.on()
        if value in [Leds.GREEN, Leds.ALL]:
            self.led_green.on()
    
    def print(self, message):
        """Clears the LCD and display the message"""
        self.lcd.clear()
        self.lcd.print(message)
