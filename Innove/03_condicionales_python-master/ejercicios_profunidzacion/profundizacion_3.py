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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''
print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

v1 = float(input("Ingrese el primer valor de temperatura: \n"));
v2 = float(input("Ingrese el segundo valor de temperatura: \n"));
v3 = float(input("Ingrese el tercer valor de temperatura: \n"));

if v1 > v2 and v1 > v3:
    print(f"El primer valor de temperatura es el mayor y es el valor: {v1}°");
elif v2 > v1 and v2 > v3:
    print(f"El segundo valor de temperatura es el mayor y es el valor: {v2}°");
elif v3 > v1 and v3 > v2:
    print(f"El tercer valor de temperatura es el mayor y es el valor: {v3}°");
if v1 < v2 and v1 < v3:
    print(f"El primer valor es la menor temperatura y es el valor: {v1}°");
elif v2 < v1 and v2 < v3:
    print(f"El segundo valor es la menor temperatura y es el valor: {v2}°");
elif v3 < v1 and v3 < v2:
    print(f"El tercer valor es la menor temperatura y es el valor: {v3}°");
promedio = (v1 + v2 + v3) / 3;
print(f"El promedio de las tres temperaturas es de: {promedio}°");

