# En 1980 la ciudad A tenia 3.5 millones de habitantes, y tasa de crecimiento de 7% anual; y la ciudad B tenia 5 millones y una tasa de crecimiento de 5% anual. 
# Si el crecimiento poblacional se mantiene constante en las dos ciudades, hacer el diagrama de flujo y el programa en Python que calcule e imprima en que año la población de la ciudad A es mayor que la de la ciudad B.

print("------------------------------------------------------------")
print("-------------------CRECIMIENTO-POBACIONAL-------------------")
print("------------------------------------------------------------")

#process and output
i = 1980
c1 = 3500000
c2 = 5000000

while c2 > c1:
    c1 = c1 + c1 * 0.07
    c2 = c2 + c2 * 0.05
    i = i +1
else:
    print("En el año",i,"la ciudad A supero la población de la ciudad B")
    print("Ciudad A:",int(c1))
    print("Ciudad B:",int(c2))