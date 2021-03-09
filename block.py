from draw import draw_star


def draw_block(x, y, revolve, pattern, state, char="x"):
    if(pattern == 1):
        # 막대기
        if(revolve == 1 or revolve == 3):
            result = draw_star(x + 1, y, state, char)            
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x + 1, y + 3, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 1, y + 2, state, " ")
                return False
            return True

        elif(revolve == 2 or revolve == 4):
            result = draw_star(x, y + 2, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x, y + 2, state, " ")
                return False
            result = draw_star(x + 2, y + 2, state, char)
            if(not result):
                draw_star(x, y + 2, state, " ")
                draw_star(x + 1, y + 2, state, " ")
                return False
            result = draw_star(x + 3, y + 2, state, char)
            if(not result):
                draw_star(x, y + 2, state, " ")
                draw_star(x + 1, y + 2, state, " ")
                draw_star(x + 2, y + 2, state, " ")
                return False
            return True

        else:
            raise RuntimeError('회전 에러')

    elif(pattern == 2):
        # 사각형
        if(revolve == 1 or revolve == 2 or revolve == 3 or revolve == 4):
            result = draw_star(x, y, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y, state, char)
            if(not result):
                draw_star(x, y, state, " ")
                return False
            result = draw_star(x, y + 1, state, char)
            if(not result):
                draw_star(x, y, state, " ")
                draw_star(x + 1, y, state, " ")
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y, state, " ")
                draw_star(x + 1, y, state, " ")
                draw_star(x, y + 1, state, " ")
                return False
            return True


        else:
            raise RuntimeError('회전 에러')

    elif(pattern == 3):
        # 2 번개
        if(revolve == 1):
            result = draw_star(x, y, state, char)
            if(not result):
                return False
            result = draw_star(x, y + 1, state, char)
            if(not result):
                draw_star(x, y, state, " ")
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y, state, " ")
                draw_star(x, y + 1, state, " ")
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x, y, state, " ")
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            return True

        elif(revolve == 2):
            result = draw_star(x, y + 2, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x, y + 2, state, " ")
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y + 2, state, " ")
                draw_star(x + 1, y + 2, state, " ")
                return False
            result = draw_star(x + 2, y + 1, state, char)
            if(not result):
                draw_star(x, y + 2, state, " ")
                draw_star(x + 1, y + 2, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            return True

        elif(revolve == 3):
            result = draw_star(x + 1, y, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                return False
            result = draw_star(x + 2, y + 1, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y + 2, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 2, y + 1, state, " ")
                return False
            return True

        elif(revolve == 4):
            result = draw_star(x, y + 1, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                return False
            result = draw_star(x + 1, y, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 1, y, state, " ")
                return False
            return True

        else:
            raise RuntimeError('회전 에러')

    elif(pattern == 4):
        # 5 번개
        if(revolve == 1):
            result = draw_star(x, y + 1, state, char)
            if(not result):
                return False
            result = draw_star(x, y + 2, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                return False
            result = draw_star(x + 1, y, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x, y + 2, state, " ")
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x, y + 2, state, " ")
                draw_star(x + 1, y, state, " ")
                return False
            return True

        elif(revolve == 2):
            result = draw_star(x, y + 1, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y + 2, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 1, y + 2, state, " ")
                return False
            return True

        elif(revolve == 3):
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y, state, char)
            if(not result):
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 1, y + 2, state, " ")
                return False
            result = draw_star(x + 2, y + 1, state, char)
            if(not result):
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 1, y + 2, state, " ")
                draw_star(x + 2, y, state, " ")
                return False
            return True

        elif(revolve == 4):
            result = draw_star(x, y, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y, state, char)
            if(not result):
                draw_star(x, y, state, " ")
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y, state, " ")
                draw_star(x + 1, y, state, " ")
                return False
            result = draw_star(x + 2, y + 1, state, char)
            if(not result):
                draw_star(x, y, state, " ")
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            return True

        else:
            raise RuntimeError('회전 에러')

    elif(pattern == 5):
        # ㅗ
        if(revolve == 1):
            result = draw_star(x, y + 1, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y, state, " ")
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            return True

        elif(revolve == 2):
            result = draw_star(x, y + 1, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 1, y + 2, state, " ")
                return False
            return True

        elif(revolve == 3):
            result = draw_star(x + 1, y, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y + 1, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 1, y + 2, state, " ")
                return False
            return True

        elif(revolve == 4):
            result = draw_star(x, y + 1, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x + 1, y, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 2, y + 1, state, " ")
                return False
            return True

        else:
            raise RuntimeError('회전 에러')

    elif(pattern == 6):
        # L
        if(revolve == 1):
            result = draw_star(x, y + 2, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y, state, char)
            if(not result):
                draw_star(x, y + 2, state, " ")
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y + 2, state, " ")
                draw_star(x + 1, y, state, " ")
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x, y + 2, state, " ")
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            return True

        elif(revolve == 2):
            result = draw_star(x, y + 1, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y + 2, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 2, y + 2, state, " ")
                return False
            return True

        elif(revolve == 3):
            result = draw_star(x + 1, y, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 1, y + 2, state, " ")
                return False
            return True

        elif(revolve == 4):
            result = draw_star(x, y + 1, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x, y, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 2, y + 1, state, " ")
                return False
            return True
        else:
            raise RuntimeError('회전 에러')

    elif(pattern == 7):
        # ㄱ
        if(revolve == 1):
            result = draw_star(x, y, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y, state, char)
            if(not result):
                draw_star(x, y, state, " ")
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y, state, " ")
                draw_star(x + 1, y, state, " ")
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x, y, state, " ")
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            return True

        elif(revolve == 2):
            result = draw_star(x, y + 1, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                return False
            result = draw_star(x, y + 2, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x, y + 2, state, " ")
                return False
            return True

        elif(revolve == 3):
            result = draw_star(x + 1, y, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                return False
            result = draw_star(x + 1, y + 2, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")   
                return False
            result = draw_star(x + 2, y + 2, state, char)
            if(not result):
                draw_star(x + 1, y, state, " ")
                draw_star(x + 1, y + 1, state, " ")   
                draw_star(x + 1, y + 2, state, " ")
                return False
            return True

        elif(revolve == 4):
            result = draw_star(x, y + 1, state, char)
            if(not result):
                return False
            result = draw_star(x + 1, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y + 1, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                return False
            result = draw_star(x + 2, y, state, char)
            if(not result):
                draw_star(x, y + 1, state, " ")
                draw_star(x + 1, y + 1, state, " ")
                draw_star(x + 2, y + 1, state, " ")
                return False
            return True
        else:
            raise RuntimeError('회전 에러')

    else:
        raise RuntimeError('블럭 에러')
