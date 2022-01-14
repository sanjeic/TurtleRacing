from turtle import Turtle, Screen
import random

canvas = Screen()
canvas.setup(1920, 1080, startx=0, starty=0)
colors = ['Red', 'Yellow', 'Green', 'Blue', 'Purple', 'Black', 'Magenta']
turtle_list = []


def turtle_running(racing_turtles, bet):
    at_goal = False
    while not at_goal:
        column_pos = 50
        cont = 0
        for turtle in racing_turtles:
            travel_distance = random.randint(0, 10)
            turtle[1] = turtle[1]+travel_distance
            turtle[0].goto(turtle[1], column_pos)
            if turtle[1] >= 900:
                at_goal = True
                if bet == colors[cont]:
                    print(f'You won {colors[cont]}')
                else:
                    print(f'You lost, {colors[cont]} won')
                break
            column_pos += 50
            cont += 1


def start_line(racing_turtles):
    column_pos = 50
    for turtle in racing_turtles:
        turtle[0].penup()
        turtle[0].goto(-900, column_pos)
        column_pos += 50
        turtle[0].pendown()


def initialize_turtles():
    for x in colors:
        turtle_list.append([Turtle(), -900])
    color_index = 0

    for turtle in turtle_list:
        turtle[0].color(colors[color_index])
        turtle[0].shape('turtle')
        turtle[0].speed('fastest')
        color_index += 1


bet = canvas.textinput('Make your bet', 'color')
initialize_turtles()
start_line(turtle_list)
turtle_running(turtle_list, bet)


canvas.exitonclick()
