import numpy as np
import random
import matplotlib.pyplot as plt

pokolenia = [20,30,40,50,60,70,80,90,100]
test_pokolen = [1, 1, 2, 3, 2, 1, 3, 3, 3]

plt.plot(pokolenia,test_pokolen)
plt.title("Pzejścia labiryntu na 10 prób przy 100 osobnikach")
plt.xlabel("Pokolenia")
plt.ylabel("Ilość przejść")
plt.ylim(-0.5,10.5)
plt.show()


liczebnosc = [70,80,90,100,110,120,130,140,150]
wyniki = [1, 1, 1, 1, 3, 1, 3, 4, 3]
plt.plot(liczebnosc,wyniki)
plt.title("Pzejścia labiryntu na 10 prób przy 50 pokoleniach")
plt.xlabel("wielkość populacji")
plt.ylabel("Ilość przejść")
plt.ylim(-0.5,10.5)
plt.show()

x10x = [1,6,5,10]
x15x = [0,4,2,10]
x20x = [0,4,1,10]
x25x = [0,0,0,10]
x30x = [0,2,0,10]

wyniki_crash = [1,0,0,0,0]
wyniki_pass = [6,4,4,0,2]
wyniki_my = [5,2,1,0,0]
all = [10,10,10,10,10]
labirynt = [10,15,20,25,30]

plt.plot(labirynt,wyniki_crash,label = 'Crash')
plt.plot(labirynt,wyniki_my,label = 'Mój')
plt.plot(labirynt,wyniki_pass,label = 'Pass')
plt.plot(labirynt,all,label = 'A*')

plt.title("Pzejścia labiryntu na 10 prób")
plt.xlabel("Rozmiar ściany labiryntu")
plt.ylabel("Ilość przejść")
plt.ylim(-0.5,10.5)
plt.legend()
plt.show()




liczebnosc = [50,60,70,80,90,100,110,120,130,140,150,160]
wyniki = [4.7404,5.6436,6.6696,7.499,8.6459,9.5292,10.1428,10.9913,11.8846,12.988,14.3576,15.0907]
l=[50,250]
li=[4.7404,22.6984]
plt.plot(l,li, color='r')
plt.plot(liczebnosc,wyniki)
plt.title("Czasy przejść labiryntu 25x25 w zależności od wielkości populacji")
plt.xlabel("wielkość populacji")
plt.ylabel("Czas przejścia w sekundach")
plt.ylim(1.5,15.5)
plt.xlim(40,170)
plt.show()


liczebnosc = [20,30,40,50,60,70,80,90,100]
wyniki = [4.0081,5.9191,7.6298,9.3229,10.9815,12.9937,14.3694,17.0073,18.7448]
l = [20,200]
li = [4.0081,36.5292]
plt.plot(liczebnosc,wyniki)
plt.plot(l,li, color='r')
plt.title("Czasy przejść labiryntu 25x25 w zależności od ilości pokoleń")
plt.xlabel("ilość pokoleń")
plt.ylabel("Czas przejścia w sekundach")
plt.ylim(1.5,20.5)
plt.xlim(10,110)
plt.show()




liczebnosc = [10,20,30,40,50,60,70,80,90,100]
wyniki = [0.194,0.7145,1.6295,2.8537,4.4631,6.8767,9.1146,11.0641,14.7252,18.8671]
plt.plot(liczebnosc,wyniki)
plt.title("Czasy przejść labiryntu 25x25")
plt.xlabel("ilość pokoleń i ich liczebność")
plt.ylabel("Czas przejścia w sekundach")
plt.ylim(-0.5,20.5)
plt.show()



labels=['20x20','30x30','40x40']

pas = [4,4,2]
moj = [5,2,1]
pas_czas = [5.2244,11.7693,20.4631]
moj_czas = [1.2742,3.294,5.0377]


x = np.arange(len(labels))
width = 0.35 

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, pas, width, label='Alg pass')
rects2 = ax.bar(x + width/2, moj, width, label='Alg mój')

ax.set_ylabel('Skuteczność na 10 przejść')
ax.set_title('Porównanie algorytmów (Skuteczność)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()


x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, pas_czas, width, label='Alg pass')
rects2 = ax.bar(x + width/2, moj_czas, width, label='Alg mój')

ax.set_ylabel('Średni czas przejścia')
ax.set_title('Porównanie algorytmów (Czas)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()

labels=['20x20','30x30','40x40']
pns = [0.4/5.2244,0.4/11.7693,0.2/20.4631]
mj = [0.5/1.2742,0.2/3.294,0.1/5.0377]

plt.plot(labels,pns,label = 'Alg pass')
plt.plot(labels,mj,label = 'Alg moj')
plt.ylabel("Ilość przejść na sekundę")
plt.xlabel("Rozmiar labiryntu")
plt.legend()
plt.show()