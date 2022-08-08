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
# y calcule la sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

n1 = int(input("Ingrese el numero del comienzo: "));
n2 = int(input("Ingrese el número del final: "));
sumatoria = 0;

for n1 in range(n2):
    sumatoria += n1;
    print(sumatoria + n2)


# for ... in range(....)

# Imprimir el valor de la sumatoria

