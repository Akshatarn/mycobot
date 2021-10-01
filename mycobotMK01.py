#!/usr/bin/python3

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time

mycobot = MyCobot(PI_PORT, PI_BAUD)

xAxis = input("Enter the X-axis:")
print(xAxis)
yAxis = input("Enter the Y-axis:")
print(yAxis)
zAxis = input("Enter the Z-axis:")
print(zAxis)
length = input("Enter the length:")
print(length)
width = input("Enter the width:")
print(width)
# finding the midpoint
lx = length/2
wy = width/2
# finding the min and max X values
xMin = xAxis + lx
xMax = xAxis - lx
# finding the min and max Y values
yMin = yAxis + wy
yMax = yAxis - wy

xAxis = xAxis - lx
yAxis  = yAxis + wy
yAxis = yAxis
for xAxis in range(xMin, xMax, 5):
    mycobot.get_coords((xAxis, yAxis,zAxis, 0, 180, 0),100)
    time.sleep(0.5)
yAxis = yMax - wy
mycobot.get_coords((xAxis, yAxis,zAxis, 0, 180, 0),100)
time.sleep(0.5)
for xAxis in range(xMax, xMin, -5):
    mycobot.get_coords((xAxis, yAxis,zAxis, 0, 180, 0),100)
    time.sleep(0.5)
    yAxis = yMin
    mycobot.get_coords((xAxis, yAxis,zAxis, 0, 180, 0),100)
    time.sleep(0.5)
for xAxis in range(xMin, xMax, 5):
    mycobot.get_coords((xAxis, yAxis,zAxis, 0, 180, 0),100)
    time.sleep(0.5)

