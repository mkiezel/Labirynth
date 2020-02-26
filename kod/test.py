from genalg import *
from genalgcrush import *
from algA import *
import time

print("Początek testu algorytmu A*:")
start_time = time.time()
tab3 = test3()
print("Algorytm A*:",round(time.time() - start_time,4),'sekundy')

print("Początek testu algorytmu genetycznego:")

tab = []
for i in range(10):
    start_time = time.time()
    tab.append(test(100,25))
    print(round(time.time() - start_time,4),'sekundy')

print("Koniec testu algorytmu genetycznego.\nPoczątek testu algorytmu genetycznego CRUSH:")

tab2 = []
for i in range(10):
    start_time = time.time()
    tab2.append(test2())
    print(round(time.time() - start_time,4),'sekundy')



print('\nWyniki algorytmu gen:' ,tab, "\nNajlepszy wynik gen, to :" , max(tab))
print('\nWyniki algorytmu genCRUSH:' ,tab2, "\nNajlepszy wynik genCRUSH, to :" , max(tab2))