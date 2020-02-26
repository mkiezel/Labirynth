from convert import *


def test3():
    data = convert('labirynt.txt')
    place = [1,1] #  0 wsp - warstwa, 1 wsp - pole
    meta = (len(data)-2)*2

    while sum(place) != meta:
#    for i in range(0,140):
        data[place[0]][place[1]] = 4    # 4-oznacza wierzchołek odwiedzony 
        # kolejność sprawdzania DÓŁ PRAWO LEWO GÓRA

        if data[place[0]+1][place[1]] != 1 and data[place[0]+1][place[1]] != 4:
            place[0] += 1
            data[place[0]][place[1]] = 4
        elif data[place[0]][place[1]+1] != 1 and data[place[0]][place[1]+1] != 4:
            place[1] += 1
            data[place[0]][place[1]] = 4
        elif data[place[0]][place[1]-1] != 1 and data[place[0]][place[1]-1] != 4:
            place[1] -= 1
            data[place[0]][place[1]] = 4        
        elif data[place[0]-1][place[1]] != 1 and data[place[0]-1][place[1]] != 4:
            place[0] -= 1
            data[place[0]][place[1]] = 4

        elif (data[place[0]+1][place[1]] == 1 or data[place[0]+1][place[1]] == 4) and (data[place[0]][place[1]+1] == 1 or data[place[0]][place[1]+1] == 4) and(data[place[0]][place[1]-1] == 1 or data[place[0]][place[1]-1] == 4) and(data[place[0]-1][place[1]] == 1 or data[place[0]-1][place[1]] == 4):
            print('jestem w punkcie bez wyjścia')
            if data[place[0]+1][place[1]] == 4:
                data[place[0]][place[1]] = 1
                place[0] += 1
            elif data[place[0]][place[1]+1] == 4:
                data[place[0]][place[1]] = 1
                place[1] += 1
            elif data[place[0]][place[1]-1] == 4:
                data[place[0]][place[1]] = 1
                place[1] -= 1
            elif data[place[0]-1][place[1]] == 4:
                data[place[0]][place[1]] = 1
                place[0] -= 1

        print(sum(place))
        print(place)
    return 0
