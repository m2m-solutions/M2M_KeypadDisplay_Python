from time import sleep
from m2m_keypad_display import KeypadDisplay, Leds


def run_tests():
    board = KeypadDisplay(0x3f)

    buttons = {
        "A": board.button_a,
        "B": board.button_b,
        "Left": board.button_left,
        "Up": board.button_up,
        "Down": board.button_down,
        "Right": board.button_right,
        "C": board.button_c,
    }
    leds = {
        "Red": Leds.RED,
        "Yellow": Leds.YELLOW,
        "Green": Leds.GREEN,
        "All": Leds.ALL,
        "None": Leds.NONE
    }

    for name in buttons:
        button = buttons[name]
        board.print(f"Press {name}")
        while not button.is_pressed:
            sleep(0.1)

    while True:
        for name in leds:
            board.print(f"LED is {name}\nHold C to quit")
            board.set_led(leds[name])
            if board.button_c.is_pressed:
                board.print("Quit...")
                exit()
            sleep(1)
    



if __name__ == "__main__":
    run_tests()
