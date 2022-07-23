# Tipos de variables [Python]
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
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia
- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''
# from ast import Break
# print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
#calculadora

print("************** Calculadora ****************");
print("Debe ingresar los dos números: ");
n1 = float(input("Digite el primer número: "));
n2= float(input("Digite el segundo número: "))

operacion = input("Digite el operador aritmético: ").upper();

if operacion=='S':
  suma = n1+n2;
  print(f"\nUstd eligió sumar y el resultado es: {suma}");
elif operacion=='R':
  resta = n1 - n2;
  print(f"\nUstd eligió restar y el resultado es: {resta}");
elif operacion=='M':
  multiplicacion = n1*n2;
  print(f"\nUstd eligió multiplicar y el resultado es: {multiplicacion}");
elif operacion=='D':
  division= n1/n2;
  print(f"\nUstd eligió dividir y el resultado es: {division: .3f}");
else:
  print("\nSe equivocó de operación")



