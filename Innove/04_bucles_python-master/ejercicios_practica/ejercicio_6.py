# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantos números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

numPos=0
NumNeg=0
n1 = int(input('Ingrese el primer número:\n'))
n2 = int(input('Ingrese el último número:\n'))

for i in range(n1,n2):
    if(i >= 0):
        numPos +=1
    else:
        NumNeg +=1

print("Cantidad de numeros negativos: ",NumNeg) 
print("Cantidad de numeros positivos: ",numPos)


        # for ... in range(....)

        # Imprimir el valor de la cantidad de números positivos y negativos
