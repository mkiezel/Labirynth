import numpy as np
import random
import matplotlib.pyplot as plt
from convert import *

import time
start_time = time.time()

data = convert('labirynt.txt')
best = [0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#        1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20

def create_individual():
    p = []
    for _ in range (0,len(data)**2):
        p.append(random.randint(0, 1))
    p.append(2)
    return p
od_gory = []
def fitness(individual,data):
#   10 10 01 11 00 11 01 00 10 01 00 01 10 01 11 11 01 10 01
#   00 - Prawo
#   01 - Lewo       pierwsza wsp - wiersz, druga kolumna
#   10 - Dół
#   11 - Góra
    m = [1,1]
    for i in range (0,len(individual)-2,2):        
        if individual[i] == 0:
            if individual[i+1] == 0:
                if data[m[0]][m[1]+1] != 1:
                    m[1] += 1
            else:
                if data[m[0]][m[1]-1] != 1:
                    m[1] -= 1
        else:
            if individual[i+1] == 0:
                if data[m[0]+1][m[1]] != 1:
                    m[0] += 1
            else:
                if data[m[0]-1][m[1]] != 1:
                    m[0] -= 1
        if data[m[0]][m[1]] == 2:
            break
        if [m[0],m[1]] not in od_gory:
            od_gory.append([m[0],m[1]])
    return sum(m)

generation = []
for i in range(0,25):
    generation.append(create_individual())

def next_gen(gen):
    for i in range(0,len(gen)):
        gen[i][-1] = fitness(gen[i],data)
    gen.sort(key=lambda x: x[-1])
    
    for i in range (0,21):
        k = random.randint(22,24)
        for j in range(0,len(gen[1]),2):
            if random.randint(0,1) == 0:
                gen[i][j] = gen [k][j]
                gen[i][j+1] = gen [k][j+1]
            else:
                pass

    for i in range(0,21):
        k = random.randint(0,2)
        if k == 1:
            p = random.randint(0,len(gen[1])-3)
            if gen[i][p] == 1:
                gen[i][p] = 0
            else:
                gen[i][p] = 1



    return gen

max = []
#print (generation[21][80])
for i in range(0,100):
    max.append(generation[24][80])
    generation = next_gen(generation)

#print(max)
#szukanie od dołu  ###############################################################################
#szukanie od dołu  ###############################################################################
od_dolu=[]

generation2 = []
for i in range(0,25):
    generation2.append(create_individual())

def fitness2(individual,data):
#   10 10 01 11 00 11 01 00 10 01 00 01 10 01 11 11 01 10 01
#   00 - Prawo
#   01 - Lewo       pierwsza wsp - wiersz, druga kolumna
#   10 - Dół
#   11 - Góra
    m = [len(data)-2,len(data)-2]
    for i in range (0,len(individual)-2,2):        
        if individual[i] == 0:
            if individual[i+1] == 0:
                if data[m[0]][m[1]+1] != 1:
                    m[1] += 1
            else:
                if data[m[0]][m[1]-1] != 1:
                    m[1] -= 1
        else:
            if individual[i+1] == 0:
                if data[m[0]+1][m[1]] != 1:
                    m[0] += 1
            else:
                if data[m[0]-1][m[1]] != 1:
                    m[0] -= 1

        if [m[0],m[1]] not in od_dolu:
            od_dolu.append([m[0],m[1]])
    return (len(data)-1)**2 - sum(m)



def next_gen2(gen):
    for i in range(0,len(gen)):
        gen[i][-1] = fitness2(gen[i],data)
    gen.sort(key=lambda x: x[-1])
    
    for i in range (3,25):
        k = random.randint(22,24)
        for j in range(0,80,2):
            if random.randint(0,1) == 0:
                gen[i][j] = gen [k][j]
                gen[i][j+1] = gen [k][j+1]
            else:
                pass

    for i in range(3,25):
        k = random.randint(0,2)
        if k == 1:
            p = random.randint(0,len(gen[1])-3)
            if gen[i][p] == 1:
                gen[i][p] = 0
            else:
                gen[i][p] = 1

    return gen




for i in range(0,100):
    generation2 = next_gen2(generation2)












print ('od dolu :',od_dolu)
print('od gory :', od_gory)
print("Algorytm moj:",round(time.time() - start_time,4),'sekundy')

for i in (0,len(od_dolu)-1):
    if od_dolu[i] in od_gory:
        print("Hura, znalazłem ścieżkę")

'''
plt.plot(max)
plt.xlabel('Pokolenie')
plt.ylabel('Fitness')
plt.ylim(0,31)
plt.show()
#generation.sort(key=lambda x: x[80])
#print (generation)
'''