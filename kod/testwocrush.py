from genalg import *
from genalgcrush import *
from algA import *
import time

print("Początek testu algorytmu A*:")
start_time = time.time()
tab3 = test3()
print(round(time.time() - start_time,4),'sekundy')

print("Początek testu algorytmu genetycznego:")

tab = []
for i in range(10):
    start_time = time.time()
    tab.append(test())
    print(round(time.time() - start_time,4),'sekundy')

print("Koniec testu algorytmu genetycznego.")