from turtle import * 
shape ('turtle')
bgcolor('black')
colors=['cyan','pink','yellow','lime','purple','blue']
speed(0)
width(2)
for x in range (1,10000,5):
    color (colors[x%6])
    forward(x)
    left (121)