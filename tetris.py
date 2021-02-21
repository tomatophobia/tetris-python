from draw import draw_board, draw_star
import time
import curses
import keyboard

width = 30 
height = 10
speed = 0.75
y_start = 15
x_start = 1
draw_board(width , height)  # draw a board
time.sleep(1)  # wait a second
star_y = y_start
star_x = x_start
state = [[0]*width for i in range(height)]

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

while(True):
    while(star_x < height - 1):
        draw_star(star_x, star_y)
        

        time.sleep(speed)
        if(state[star_x + 1][star_y] == 1):
            draw_star(star_x , star_y)
            break
        draw_star(star_x , star_y, " ")
        star_x += 1
    draw_star(star_x, star_y)

    state[star_x][star_y] = 1

    star_y = y_start
    star_x = x_start






keyboard.wait('esc')
curses.endwin()  # return control back to the console