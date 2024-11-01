import time
import turtle
import random
from turtle import Screen, Turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor('light blue')
drawing_board.title("Phyton Turtle Uygulaması")


FONT = ('Arial', 50, 'normal')

score = 0

def update_score():
    scoreboard.clear()
    scoreboard.write(f"Score: {score}", align='center', font=("Arial", 24, "normal"))

def random_position():
    return random.randint(-500, 500), random.randint(-300, 300)

def on_click(x, y):
    global score
    score += 1
    update_score()
    move_turtle()

def move_turtle():
    x, y = random_position()
    target_turtle.goto(x, y)

def countdown(time):
    screen.onclick(None)
    timer.clear()

    if time > 0:
        timer.goto(0, 100)
        timer.write(time, align='center', font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        timer.goto(0, 100)
        timer.write("0", align='center', font=FONT)
        timer.goto(0, -50)
        timer.write("Game Over", align='center', font=FONT)
        screen.onclick(lambda x, y: countdown(30))

def game_over():
    timer.clear()
    timer.write("Game Over", align='center', font=FONT)


screen = Screen()
screen.setup(width=1000, height=1000)

timer = Turtle()
timer.hideturtle()
timer.penup()

scoreboard = Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.goto(0, 550)

target_turtle = Turtle()
target_turtle.shape("turtle")
target_turtle.color("green")
target_turtle.penup()
target_turtle.speed(0)
target_turtle.goto(random_position())
target_turtle.onclick(on_click)


timer.penup()
timer.sety(200)
timer.write("Click Screen", align='center', font=FONT)

screen.onclick(lambda x, y: countdown(15))
screen.mainloop()
