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
pattern = random.randint(1,7)
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
        pass
    elif(e.name == "x"):
        pass


keyboard.hook(keyhandler)

while(True):
    draw_block(star_x, star_y, revolve, pattern, state)
    while(star_x < height - 2):
        time.sleep(speed)
        draw_block(star_x, star_y, revolve, pattern, state, " ")
        star_x += 1
        success = draw_block(star_x, star_y, revolve, pattern, state)
        if(not success):
            draw_block(star_x - 1, star_y, revolve, pattern, state)
            break

    star_y = y_start
    star_x = x_start
    pattern = random.randint(1,7)


keyboard.wait('esc')
curses.endwin()  # return control back to the console
