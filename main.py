#!/usr/bin/python3

import sys
script, infile = sys.argv
sys.stderr = 0


def scan(line, outfileo):
    if line[0] == "PENDOWN":
        outfileo.write("pen_down()\n")
    elif line[0] == "PENUP":
        outfileo.write("pen_up()\n")
    elif line[0] == "FOR":
        outfileo.write("graphics_move(forward,"+line[1]+")\n")
    elif line[0] == "BAC":
        outfileo.write("graphics_move(backward,"+line[1]+")\n")
    elif line[0] == "RIG":
        outfileo.write("graphics_turn(right,"+line[1]+")\n")
    elif line[0] == "LEF":
        outfileo.write("graphics_turn(left,"+line[1]+")\n")
    elif line[0] == "COLOR":
        outfileo.write("graphics_colour('"+line[1]+"')\n")
    elif line[0] == "BGCOLOR":
        outfileo.write("graphics_bgcolour('"+line[1]+"')\n")


infileo = open(infile, 'r')
outfileo = open('func_langc.py', 'w')
func_lang = open('func_lang.py', 'r')
outfileo.write(func_lang.read())
outfileo.write("run_graphics()\n")

line = infileo.readline().split()

while line != "":
    scan(line, outfileo)
    line = infileo.readline().split()

print(infile, "has been compiled succefully!")
print("Type in: ./func_langc.py to run the compiled file.")
