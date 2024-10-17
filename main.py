import random
from turtle import Turtle, Screen

is_race_on= False

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Color:")
print(user_bet)
colors =["red", "orange", "yellow", "purple", "green", "blue"]
all_turtles = []

x = -225
y = 150
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    all_turtles.append(new_turtle)
    for turtle in colors:
        y = y-5
        new_turtle.goto(x, y)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The winning color is {winning_color}")
            else:
                print(f"You've lost! The winning color is {winning_color}")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)





screen.exitonclick()

