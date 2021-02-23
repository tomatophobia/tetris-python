draw_star(i , s_p)
draw_star(i , s_p + 1)
draw_star(i + 1, s_p + 1)
draw_star(i + 1, s_p + 2)
time.sleep(1)
draw_star(i , s_p , " ")
draw_star(i , s_p + 1 , " ")
draw_star(i + 1, s_p + 1 , " ")
draw_star(i + 1 , s_p + 2 , " ")

def draw_block(x, y, revolve, pattern, char="*"):
    if(pattern == 1):
        # 막대기
        if(revolve == 1):
            draw_star(x + 1 , y , char)
            draw_star(x + 1 , y + 1 , char)
            draw_star(x + 1 , y + 2, char)
            draw_star(x + 1 , y + 3)

        elif(revolve == 2):
            draw_star(x , y + 2)
            draw_star(x + 1 , y + 2)
            draw_star(x + 2 , y + 2)
            draw_star(x + 3 , y + 2)

        elif(revolve == 3):
            draw_star(x + 2 , y)
            draw_star(x + 2 , y + 1)
            draw_star(x + 2 , y + 2)
            draw_star(x + 2 , y + 3)

        elif(revolve == 4):
            draw_star(x , y + 1)
            draw_star(x + 1 , y + 1)
            draw_star(x + 2 , y + 1)
            draw_star(x + 3 , y + 1)

        else:
            raise RuntimeError('회전 에러') from exc

    elif(pattern == 2):
        pass

    elif(pattern == 3):
        pass

    elif(pattern == 4):
        pass

    elif(pattern == 5):
        pass

    elif(pattern == 6):
        pass

    elif(pattern == 7):
        pass

    else:
        raise RuntimeError('블럭 에러') from exc