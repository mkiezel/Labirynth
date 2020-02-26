from convert import *
from pyeasyga import pyeasyga
import random
import time

def test(pop,pok):
    data = convert('labirynt.txt')

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
            if data[m[0]][m[1]] == 3:
                break
        return sum(m)

    def create_individual(data):
        return [random.randint(0, 1) for _ in range(len(data)**2*4)]


    ga = pyeasyga.GeneticAlgorithm(data,
                                population_size=pop,
                                generations=pok,
                                crossover_probability=0.8,
                                mutation_probability=0.05,
                                elitism=True,
                                maximise_fitness=True)

    ga.create_individual = create_individual

    ga.fitness_function = fitness

    ga.run()

    print (ga.best_individual()[0])


    return ga.best_individual()[0]

"""
for i in range (0,11):
    start_time = time.time()
    test(100,50)
    print("Algorytm gen:",round(time.time() - start_time,4),'sekundy')
"""