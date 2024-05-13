import random
import math

cuantos = 1000
cuantosSi = 0

for i in range(cuantos):
    x = random.random()
    y = random.random()
    
    YCalculada = math.sqrt(1-x*x)
    if y>YCalculada:
        None
    else:
        cuantosSi += 1  
cuartoDeArea = float(cuantosSi) / float(cuantos)

print(cuartoDeArea)