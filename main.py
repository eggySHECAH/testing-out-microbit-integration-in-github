class AyoYourMom:
    def __init__(self):
        input.on_button_pressed(Button.A, self.a)
    def a(self):
        num1 = 5
        num2 = 6
        num3 = num1 + num2
        print(num3)