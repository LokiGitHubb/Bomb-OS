from vex import *

brain = Brain()
leftToggle = Touchled(Ports.PORT9)
rightToggle = Touchled(Ports.PORT11)

buttons = []

class button:
    def __init__(self, x,y, color, fontType, Text, callback, sizeX, SizeY, name) -> None:
        brain.screen.set_cursor(x,y)
        brain.screen.set_pen_color(color)
        brain.screen.set_fill_color(color)
        brain.screen.set_font(fontType)
        brain.screen.draw_rectangle(x, y, sizeX, SizeY, color)
        self.callBack = callback
        self.x = x
        self.y = y
        self.color = color
        self.text = Text
        self.sizeX = sizeX
        self.sizeY = SizeY
        self.name = name
        buttons.append(self)
    def toggle(self, nameClassified):
        if nameClassified == self.name:
            self.callBack()
    def delete(self):
        self.name = ""
        self = None
class mouse:
    def __init__(self) -> None:
        self.position = "button1"
    def press(self):
        for _, button in enumerate(buttons):
            button.toggle()
        
def clearScreen():
    for _, button in enumerate(buttons):
        button.delete()
    brain.screen.clear_screen()

def enterProgramMenu():
    pass


def MenuEnter():
    clearScreen()
    brain.play_sound(SoundType.RATCHET)
    brain.screen.set_cursor(2,1)
    brain.screen.set_font(FontType.MONO20)
    brain.screen.print("Bomb-OS V-0.00")
    startingButton = button(5,1, Color.GREEN, FontType.MONO20, "Programs", enterProgramMenu, 10,5,"Enter Programs")
    


MenuEnter()