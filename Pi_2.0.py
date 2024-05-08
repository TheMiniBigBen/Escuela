Acomulador = 0.0

contador = 0
DivicionActual=1.0
EsSuma = True

while DivicionActual > 0.0052:
    contador += 1
    DivicionActual = 1/ contador
   
if contador % 2 != 0:
    if EsSuma:
            Acomulador += 1/ contador
    else:
            Acomulador -= 1/ contador
    EsSuma= not EsSuma
    
print("el cuarto del area es:", Acomulador)
pi=Acomulador * 4
print("Pi es igual a: ",pi)