from m2m_keypaddisplay import KeypadDisplay, LED

def run_test(self):
    board = KeypadDisplay(0x3f)
    print(board)

    while True:
        if board.button_a.is_pressed():
            board.print("Button A")
        if board.button_b.is_pressed():
            board.print("Button B")
        if board.button_left.is_pressed():
            board.print("Button Left")
        if board.button_up.is_pressed():
            board.print("Button Up")
        if board.button_down.is_pressed():
            board.print("Button Down")
        if board.button_right.is_pressed():
            board.print("Button Right")
        if board.button_c.is_pressed():
            board.print("Button C")



if __name__ == "__main__":
    run_test()
