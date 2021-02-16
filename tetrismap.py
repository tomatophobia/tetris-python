from draw import draw_board, draw_star
import time
import curses

width = 10
height = 10
draw_board(width , height)  # draw a board
time.sleep(1)  # wait a second
s_p = 5
for i in range(1, height - 1):
    draw_star(i , s_p)
    draw_star(i , s_p + 1)
    draw_star(i + 1, s_p + 1)
    draw_star(i + 1, s_p + 2)
    time.sleep(1)
    draw_star(i , s_p , " ")
    draw_star(i , s_p + 1 , " ")
    draw_star(i + 1, s_p + 1 , " ")
    draw_star(i + 1 , s_p + 2 , " ")

    





curses.endwin()  # return control back to the console