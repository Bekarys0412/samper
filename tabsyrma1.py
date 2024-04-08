from turtle import * 
shape ('turtle')
bgcolor('black')
colors=['cyan','pink','yellow','lime','purple','blue']
speed(0)
width(2)
for x in range (0,400,2):
    color (colors[x%6])
    forward(x)
    left (91)