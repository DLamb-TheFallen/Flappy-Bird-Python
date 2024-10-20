from tkinter import *



class Bird:
    alive = True
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 50
    
    def drawBird(self,canvas):
        #body
        canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, outline = "black", fill = "yellow", width = 1)
        #eye
        canvas.create_oval(self.x + (self.radius)/2, self.y - (self.radius)/2 ,self.x + (self.radius)/2 + 8,  self.y - self.radius/2 + 8, outline = "black", fill = "black", width = 1)
        #beak
        points = [self.x + (self.radius)/2 + 18, self.y - ((self.radius)/2) + 4, self.x + self.radius*1.5, self.y, self.x + (self.radius)/2 + 18, self.y - ((self.radius)/2) + 12]
        canvas.create_polygon(points, outline = "black", fill = "orange", width = 1 )


