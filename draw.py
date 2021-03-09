import curses
import time

console = curses.initscr()  # initialize is our playground

# this can be more streamlined but it's enough for demonstration purposes...
def draw_board(width, height, charset="+^| "):
    h_line = charset[0] + charset[1] * (width - 2) + charset[0]
    v_line = charset[2] + charset[3] * (width - 2) + charset[2]
    console.clear()
    console.addstr(0, 0, h_line)
    for line in range(1, height):
        console.addstr(line, 0, v_line)
    console.addstr(height-1, 0, h_line)
    console.refresh()

def draw_star(x, y, state , char="x"):
    if(char == " "):
        state[x][y] = 0
    else:
        if(state[x][y] == 1):
           return False 
        state[x][y] = 1
        

    console.addstr(x, y, char)
    console.refresh()
    return True

    
    

if __name__ == "__main__":
    draw_board(10, 10)  # draw a board
    time.sleep(1)  # wait a second
    draw_star(6, 1)  # draw our star
    time.sleep(1)  # wait a second
    draw_star(6, 1, " ")  # clear the star
    draw_star(3, 3)  # place the star on another position
    time.sleep(3)  # wait a few seconds
    curses.endwin()  # return control back to the console