# Author
# Data
# Description : Memory Game with turtle
# Revision History
# Name     Date      Desc
# scl      2/12/24      Intitial code base
#
#

import random
import turtle
import time

number_list = []
start_pos_x = -100
start_pos_y = 0
level = 3
offset = 100

def drawsquare(x,y):  
    turtle.down()
    for x in range(4):
        turtle.forward(100)
        turtle.left(90)
        
for x in range(level):
    # data type is integer
    a = random.randint(1,99)

    # data structure
    number_list.append(a)
    
    turtle.write(str(a), font =("Verdana",50, "normal"))
    turtle.up()
    save_pos = (x * offset,0)
    turtle.goto(save_pos)
    
    drawsquare(x * offset,0)
    turtle.goto(x * offset,0)
    time.sleep(3)
    
turtle.clear()
    
# please enter the answers
for x in range(level):
    answer = int(input("The number were: "))
