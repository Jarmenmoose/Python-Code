import turtle
import time
import random

delay= 0.1
score = 0
high_score = 0


#Creating GameScreen
wn = turtle.Screen()
wn.title = ("Snek Game")
wn.bgcolor("green")

#setting the dimensions
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake
head = turtle.Turtle()
head.shape("square")
head.color("White")
head.penup()
head.goto(0,0)
head.direction = "Stop"

#Food
food = turtle.Turtle()
food.shape("circle")
food.color("White")
food.speed(0)
food.penup()
food.goto(0,100)

#Score Display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("Yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0   High Score : 0", align="center", font=("candara", 28,"bold"))


#Getting input from user
def up():
    if head.direction != "down":
        head.direction = 'up'
def down():
    if head.direction !="up":
        head.direction = 'down'
def left():
    if head.direction !="right":
        head.direction = 'left'
def right():
    if head.direction !='left':
        head.direction = 'right'

def move():
    if head.direction == 'up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction == 'down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction == 'left':
        x=head.xcor()
        head.setx(x-20)
    if head.direction == 'right':
        x=head.xcor()
        head.setx(x+20)

wn.listen()
wn.onkeypress(up, 'w')
wn.onkeypress(down, 's')
wn.onkeypress(left, 'a')
wn.onkeypress(right, 'd')

segments = []

#Main
while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("pink")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)

wn.mainloop()
