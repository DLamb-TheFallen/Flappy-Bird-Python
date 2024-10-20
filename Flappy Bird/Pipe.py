
from tkinter import *



class Pipe:
    def __init__(self):
        self.upLeftX    = 0
        self.upLeftY    = 0
        self.downRightX = 0
        self.downRightY = 0
    def generate(self, canvas, height):
        #gap is 350 pixels
        self.downRightX = self.upLeftX-200
        canvas.create_rectangle(self.upLeftX, self.upLeftY, self.downRightX, height, fill = "green" ) #bottom pipe
        canvas.create_rectangle(self.upLeftX - 250, self.upLeftY, self.upLeftX + 50, self.upLeftY + 85, fill = "green" ) #bottom pipe outing
        canvas.create_rectangle(self.upLeftX, 0, self.upLeftX - 200, self.upLeftY - 350 , fill = "green" ) #top pipe
        canvas.create_rectangle(self.upLeftX - 250, self.upLeftY-350, self.upLeftX + 50, self.upLeftY - 275, fill = "green" ) #top pipe outing
        #add hit detection to pipe outings 