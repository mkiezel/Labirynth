import math, os


def convert(lab):
    dir = os.getcwd()
    dir = dir + '/labirynty/' + lab
    f= open(dir,"r")
    text = f.read()
    plusy = text.count("+")

    plusy = int(math.sqrt(plusy) - 1)

    labirynt = []
    for i in range (0,len(text)):
        if text[i] == '+':
            labirynt.append(1)
        if text[i] == '-':
            labirynt.append(1)
        if text[i] == '|':
            labirynt.append(1)
        
        
        if text[i] == ' ':
            labirynt.append(0)


    dl = int(math.sqrt(len(labirynt)))

    ost = []
    for i in range(0,dl):
        ost.append([])
        for j in range(0,dl):
            ost[i].append(labirynt[i*dl+j])


    ost[1][0]=1
    ost[1][1] = 2
    ost[dl-2][dl-2] = 3
    ost[dl-2][dl-1] = 1

    return ost

