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
            draw_star(x + 1 , y + 3, char)

        elif(revolve == 2):
            draw_star(x , y + 2, char)
            draw_star(x + 1 , y + 2, char)
            draw_star(x + 2 , y + 2, char)
            draw_star(x + 3 , y + 2, char)

        elif(revolve == 3):
            draw_star(x + 2 , y, char)
            draw_star(x + 2 , y + 1, char)
            draw_star(x + 2 , y + 2, char)
            draw_star(x + 2 , y + 3, char)

        elif(revolve == 4):
            draw_star(x , y + 1, char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 2 , y + 1, char)
            draw_star(x + 3 , y + 1, char)

        else:
            raise RuntimeError('회전 에러') from exc

    elif(pattern == 2):
        # 사각형
        if(revolve == 1 or revolve == 2 or revolve == 3 or revolve == 4):
            draw_star(x , y , char)
            draw_star(x + 1 , y , char)
            draw_star(x , y + 1, char)
            draw_star(x + 1 , y + 1, char)

        else:
            raise RuntimeError('회전 에러') from exc

    elif(pattern == 3):
        # 2 번개
        if(revolve == 1):
            draw_star(x , y , char)
            draw_star(x , y + 1 , char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 1 , y + 2, char)

        elif(revolve == 2):
            draw_star(x , y + 2, char)
            draw_star(x + 1 , y + 2, char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 2 , y + 1, char)

        elif(revolve == 3):
            draw_star(x + 1 , y, char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 2 , y + 1, char)
            draw_star(x + 2 , y + 2, char)

        elif(revolve == 4):
            draw_star(x , y + 1, char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 1 , y , char)
            draw_star(x + 2 , y , char)

        else:
            raise RuntimeError('회전 에러') from exc



    elif(pattern == 4):
        # 5 번개
        if(revolve == 1):
            draw_star(x , y + 1 , char)
            draw_star(x , y + 2 , char)
            draw_star(x + 1 , y , char)
            draw_star(x + 1 , y + 1, char)

        elif(revolve == 2):
            draw_star(x , y + 1, char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 1 , y + 2, char)
            draw_star(x + 2 , y + 2, char)

        elif(revolve == 3):
            draw_star(x + 1, y + 1 , char)
            draw_star(x + 1, y + 2 , char)
            draw_star(x + 2 , y , char)
            draw_star(x + 2 , y + 1, char)

        elif(revolve == 4):
            draw_star(x , y , char)
            draw_star(x + 1 , y , char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 2 , y + 1, char)

        else:
            raise RuntimeError('회전 에러') from exc


    elif(pattern == 5):
        # ㅗ
        if(revolve == 1):
            draw_star(x , y + 1 , char)
            draw_star(x + 1 , y , char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 1 , y + 2, char)

        elif(revolve == 2):
            draw_star(x , y + 1, char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 1 , y + 2, char)
            draw_star(x + 2 , y + 1, char)

        elif(revolve == 3):
            draw_star(x + 1, y , char)
            draw_star(x + 1, y + 1 , char)
            draw_star(x + 1 , y + 2, char)
            draw_star(x + 2 , y + 1, char)

        elif(revolve == 4):
            draw_star(x , y + 1, char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 2 , y + 1, char)
            draw_star(x + 1 , y , char)

        else:
            raise RuntimeError('회전 에러') from exc

    elif(pattern == 6):
        # L
        if(revolve == 1):
            draw_star(x , y + 2 , char)
            draw_star(x + 1 , y , char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 1 , y + 2, char)

        elif(revolve == 2):
            draw_star(x , y + 1, char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 2 , y + 2, char)
            draw_star(x + 2 , y + 1, char)

        elif(revolve == 3):
            draw_star(x + 1, y , char)
            draw_star(x + 1, y + 1 , char)
            draw_star(x + 1 , y + 2, char)
            draw_star(x + 2 , y , char)

        elif(revolve == 4):
            draw_star(x , y + 1, char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 2 , y + 1, char)
            draw_star(x , y , char)
        else:
            raise RuntimeError('회전 에러') from exc

    elif(pattern == 7):
        # ㄱ
        if(revolve == 1):
            draw_star(x , y , char)
            draw_star(x + 1 , y , char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 1 , y + 2, char)

        elif(revolve == 2):
            draw_star(x , y + 1, char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x , y + 2, char)
            draw_star(x + 2 , y + 1, char)

        elif(revolve == 3):
            draw_star(x + 1, y , char)
            draw_star(x + 1, y + 1 , char)
            draw_star(x + 1 , y + 2, char)
            draw_star(x + 2 , y + 2 , char)

        elif(revolve == 4):
            draw_star(x , y + 1, char)
            draw_star(x + 1 , y + 1, char)
            draw_star(x + 2 , y + 1, char)
            draw_star(x + 2 , y , char)
        else:
            raise RuntimeError('회전 에러') from exc

    else:
        raise RuntimeError('블럭 에러') from exc