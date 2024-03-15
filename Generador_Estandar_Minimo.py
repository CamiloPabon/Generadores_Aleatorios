import matplotlib.pyplot as plt
import numpy as np
multiplicador = 7**5
modulo = 2**31-1
semilla = 4
def Generador_Congruente_Multiplicativo(semilla,n):
    numeros = []
    for i in range(n):
        semilla = (multiplicador*semilla)%modulo
        numeros.append(semilla/modulo)
    return numeros
n= 100000
numeros_aleatorios = Generador_Congruente_Multiplicativo(semilla,n)

plt.hist(numeros_aleatorios, bins=50)
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Histograma de numeros aleatorios')
plt.show()