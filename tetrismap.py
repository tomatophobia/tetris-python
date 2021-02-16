from draw import draw_board, draw_star
import time
import curses
import keyboard

width = 30 
height = 10
draw_board(width , height)  # draw a board
time.sleep(1)  # wait a second
star_y = 15
star_x = 0

def keyhandler(e):
    global star_y
    global star_x
    if(e.name == "right"):
        draw_star(star_x, star_y, " ")
        star_y += 1
        draw_star(star_x, star_y)
    elif(e.name == "left"):
        draw_star(star_x, star_y, " ")
        star_y -= 1
        draw_star(star_x, star_y)
    elif(e.name == "down"):
        draw_star(star_x, star_y, " ")
        star_x +=1
        draw_star(star_x, star_y)
    elif(e.name == "z"):
        pass
    elif(e.name == "x"):
        pass       

keyboard.hook(keyhandler)

while(star_x < height - 1):
    star_x += 1
    draw_star(star_x, star_y)
    time.sleep(1)
    draw_star(star_x , star_y, " ")

curses.endwin()  # return control back to the console