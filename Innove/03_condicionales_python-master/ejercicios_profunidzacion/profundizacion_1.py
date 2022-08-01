# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA:
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

n1 = int(input("ingresa el primer valor: \n"))
n2 = int(input("ingresa el segundo valor: \n"))
if n1 > 0:
    print("El primer numero es positivo.")
elif n1 < 0:
    print("El primer numero es negativo.")
elif n1 == 0:
    print("El primer numero es cero.")
if n2 > 0:
    print("El segundo numero es positivo.")
elif n2 < 0:
    print("El segundo numero es negativo.")
elif n2 == 0:
    print("El segundo numero es cero.")

