from draw import draw_board, draw_star
import time
import curses
import keyboard
from block import draw_block

width = 30
height = 10
speed = 0.75
y_start = 15
x_start = 1
draw_board(width, height)  # draw a board
time.sleep(1)  # wait a second
star_y = y_start
star_x = x_start
state = [[0]*width for i in range(height)]


def keyhandler(e):
    global star_y
    global star_x
    if(e.name == "right"):
        draw_block(star_x, star_y, 1, 3, state, " ")
        star_y += 1
        draw_block(star_x, star_y, 1, 3, state)
    elif(e.name == "left"):
        draw_block(star_x, star_y, 1, 3, state, " ")
        star_y -= 1
        draw_block(star_x, star_y, 1, 3, state)
    elif(e.name == "down"):
        draw_block(star_x, star_y, 1, 3, state,  " ")
        star_x += 1
        draw_block(star_x, star_y, 1, 3, state)
    elif(e.name == "z"):
        pass
    elif(e.name == "x"):
        pass


keyboard.hook(keyhandler)

while(True):
    while(star_x < height - 1):
        draw_block(star_x, star_y, 1, 3, state)

        time.sleep(speed)
        if(state[star_x + 1][star_y] == 1):
            draw_block(star_x, star_y, 1, 3, state)
            break
        draw_block(star_x, star_y, 1, 3, state, " ")
        star_x += 1
    draw_block(star_x, star_y, 1, 3, state)

    state[star_x][star_y] = 1

    star_y = y_start
    star_x = x_start


keyboard.wait('esc')
curses.endwin()  # return control back to the console
