"""
ITS 1801 F22 Exam 03
Solution
"""

import turtle

casper = turtle.Turtle()
piper = turtle.Turtle()
hazel = turtle.Turtle()

casper.shape("turtle")
piper.shape("triangle")
hazel.shape("classic")

piper.penup()
piper.goto(-150,0)
hazel.penup()
hazel.goto(150,0)
piper.pendown()
hazel.pendown()

def square(turtleName,lineColor):
  turtleName.color(lineColor)
  for i in range(4):
    turtleName.forward(50)
    turtleName.left(90)

def triangle(turtleName,lineColor):
  turtleName.color(lineColor)
  for i in range(3):
    turtleName.forward(50)
    turtleName.left(120)

def circle(turtleName,lineColor):
  turtleName.color(lineColor)
  turtleName.circle(50)

def draw(turtleName, shape, lineColor):
  if shape == '0':
    triangle(turtleName, lineColor)
  elif shape == '1':
    square(turtleName, lineColor)
  elif shape =='2':
    circle(turtleName, lineColor)
  else:
    print ('Wrong parameter selected and give to draw function')


print("This program has three turtles: Piper (left), Casper (middle) and Hazel (right)")
choiceTurtleStr = input("Select a turtle (0) Piper (1) Casper (2) Hazel: ")
choiceShapeStr = input ("Select a shape (0) triangle, (1) square, (2) circle: ")
choiceColorStr = input("Select a color (0) yellow, (1) blue, (2) red, (3) green: ")

colorList = ["yellow", "blue", "red", "green"]

choiceColorInt = int(choiceColorStr)

if choiceTurtleStr == '0':
  draw(piper, choiceShapeStr, colorList[choiceColorInt])
elif choiceTurtleStr == '1':
  draw(casper, choiceShapeStr, colorList[choiceColorInt])
elif choiceTurtleStr == '2':
  draw(hazel, choiceShapeStr, colorList[choiceColorInt])
else:
  print("Invalid turtle choice, not drawing anything")