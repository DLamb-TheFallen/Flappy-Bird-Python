from tkinter import *
from Bird import Bird
import random
import keyboard
from Pipe import Pipe


main= Tk()
width= 1600
height= 800
bird = Bird()
score = 0
frame = 0
pipes = []

main.title("Flappy Bird")
main.configure(background="light blue")
main.minsize(200,200)
main.maxsize(width,height)
main.geometry(str(width) + "x" + str(height) +"+0+0")

canvas= Canvas(main, width = width, height = height, bg = "light blue")
canvas.pack()

bird.x = 180
bird.y = height/2
bird.radius = 50



def generatePipe():
    if frame % 60 == 0:
        pipe = Pipe()
        pipe.upLeftX = width
        pipe.upLeftY = random.randint(300,height-150)
        pipes.append(pipe)
    for i in range(len(pipes)):
        pipes[i].generate(canvas, height)
        pipes[i].upLeftX -= 10

def clearPipes():
    if pipes[0].downRightX == -300:
        del pipes[0]

def detectHit():
    global bird
    global pipes
    
    for pipe in pipes:
        if pipe.downRightX <= bird.x + (bird.radius) <= pipe.upLeftX:
            if bird.y + (bird.radius) >= pipe.upLeftY or bird.y - (bird.radius) <= pipe.upLeftY - 350:
                bird.alive = False
                return

def death():
    print("You Died!")
    #buttons
    canvas.delete("All")
    canvas.create_rectangle(0,0, width, height, fill = "white")
    canvas.create_text(width/2 + 85, height/2 - 20, text="Your Score was " + str(score), font=("Arial", 20))
    againButton = Button(text="Again?", 
                   command= lambda : [againButton.place_forget(), closeButton.place_forget(), reset()],
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
    againButton.place(x= width/2, y = height/2)
    closeButton = Button(text="Exit", 
                   command= lambda : [main.quit()],
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)
    closeButton.place(x = width / 2, y = (height / 2) + 65 )

def reset():
    global bird
    global pipes
    global score
    global frame
    bird.x = 180
    bird.y = height/2
    bird.alive = True
    pipes  = []
    score  = 0
    frame  = 0
    update()


def update():
    global frame
    global pipes
    global score
    global bird
    if bird.alive: 
        canvas.delete("all")
        generatePipe()
        clearPipes()
        detectHit()
        bird.y += 20
        bird.drawBird(canvas)
        if pipes[0].upLeftX == 180:
            score += 1
        frame += 1
        if keyboard.is_pressed('space'):
            bird.y -= 100
        if keyboard.is_pressed('esc'):
            main.quit()
        main.after(60,update)
        canvas.create_text(width-100, 20, text="Score: " + str(score), font=("Helvetica", 20))
        if bird.y >= height-bird.radius or bird.y <= 0-bird.radius:
            bird.alive = False
    else:
        death()



update()
main.mainloop()



