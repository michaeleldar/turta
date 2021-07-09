#!/usr/bin/python3

import random
import sys
from turtle import *

sys.stderr = 0


def run_graphics():  # opens the turtle window and makes
    shape("classic")  # standard settings
    speed(1)
    pensize(4)


varibles = {}  # makes a varibles dictionary


def varint(name):
    return int(varibles[name])


def varstr(name):
    return str(varibles[name])


def make_ran_num(varible, min_num, max_num):  # makes a
    varibles[varible] = random.randint(min_num, max_num)
    # random number and sets it to a varible


def graphics_turn(direction, degrees):  # turns the turtle
    direction(degrees)


def graphics_move(direction, pixels):  # moves the turtle
    direction(pixels)


def graphics_colour(colour):  # sets the pen colour
    color(colour)


def write(contents):  # displays text on the screen
    print(str(contents))


def declare(varible, value):  # makes a varible
    varibles[varible] = value


def ask_input(varible, question):
    varibles[varible] = input(question + " ")

    # answer to a varible


def add(varible, num1, num2):  # adds 2 numbers and sets
    varibles[varible] = int(num1) + int(num2)


def subtract(varible, num1, num2):  # subtracts two numbers
    varibles[varible] = int(num1) - int(num2)


def multiply(varible, num1, num2):  # multiplys two numbers
    varibles[varible] = int(num1) * int(num2)


def divide(varible, num1, num2):  # divides two numbers
    varibles[varible] = int(num1) / int(num2)


def check_equals(condition, truec, falsec):
    if condition:
        exec(truec)
    else:
        exec(falsec)


def repeat(times, code):
    for x in range(0, times):
        exec(code)


def rep_while_eq(condition, code):
    while condition:
        exec(code)


def graphics_bgcolour(colour):
    Screen().bgcolor(colour)


def end():
    quit()
run_graphics()
graphics_colour('turquoise')
graphics_bgcolour('gold')
graphics_move(forward,199)
graphics_move(forward,77)
graphics_turn(right,88)
graphics_move(forward,10)
graphics_colour('green')
graphics_turn(left,10)
graphics_move(forward,50)
