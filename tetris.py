from draw import draw_board, draw_star
import time
import curses
import keyboard
from block import draw_block
import random

width = 30
height = 10
speed = 0.75
y_start = 15
x_start = 1
draw_board(width, height)  # draw a board
time.sleep(1)  # wait a second
star_y = y_start
star_x = x_start
revolve = 1
# pattern = random.randint(1,7)
pattern = 7
floor = height - 2
state = [[0]*width for i in range(height)]


def keyhandler(e):
    global star_y
    global star_x
    global revolve
    global pattern
    global state
    if(e.name == "right"):
        draw_block(star_x, star_y, revolve, pattern, state, " ")
        star_y += 1
        draw_block(star_x, star_y, revolve, pattern, state)
    elif(e.name == "left"):
        draw_block(star_x, star_y, revolve, pattern, state, " ")
        star_y -= 1
        draw_block(star_x, star_y, revolve, pattern, state)
    elif(e.name == "down"):
        draw_block(star_x, star_y, revolve, pattern, state,  " ")
        star_x += 1
        draw_block(star_x, star_y, revolve, pattern, state)
    elif(e.name == "z"):
        draw_block(star_x, star_y, revolve, pattern, state,  " ")
        revolve += 1
        if(revolve > 4):
            revolve %= 4
        change_floor(pattern, revolve)
        draw_block(star_x, star_y, revolve, pattern, state)
    elif(e.name == "x"):
        draw_block(star_x, star_y, revolve, pattern, state,  " ")
        revolve += 3
        if(revolve > 4):
            revolve %= 4
        change_floor(pattern, revolve)
        draw_block(star_x, star_y, revolve, pattern, state)


def change_floor(pattern, revolve):
    global floor
    if(pattern == 1 and (revolve == 2 or revolve == 4)):
        floor = height - 4
    elif(pattern == 3 and (revolve == 2 or revolve == 4)):
        floor = height - 3
    elif(pattern == 4 and (revolve == 2 or revolve == 4)):
        floor = height - 3
    elif(pattern == 5 and (revolve == 2 or revolve == 3 or revolve == 4)):
        floor = height - 3
    elif(pattern == 6 and (revolve == 2 or revolve == 3 or revolve == 4)):
        floor = height - 3
    elif(pattern == 7 and (revolve == 2 or revolve == 3 or revolve == 4)):
        floor = height - 3        
    else:
        floor = height - 2


keyboard.on_press(keyhandler)

while(True):
    draw_block(star_x, star_y, revolve, pattern, state)
    change_floor(pattern, revolve)
    while(star_x < floor):
        time.sleep(speed)
        draw_block(star_x, star_y, revolve, pattern, state, " ")
        star_x += 1
        success = draw_block(star_x, star_y, revolve, pattern, state)
        if(not success):
            draw_block(star_x - 1, star_y, revolve, pattern, state)
            break

    star_y = y_start
    star_x = x_start
    revolve = 1
    # pattern = random.randint(1, 7)


keyboard.wait('esc')
curses.endwin()  # return control back to the console
