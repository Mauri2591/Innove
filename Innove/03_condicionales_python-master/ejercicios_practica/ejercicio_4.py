# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

from tokenize import Number


texto_1 = '5';
texto_2 = '7';
texto_3 = 5;

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
'''
if texto_1 >= texto_2:
    print("texto_1 es mayor");
elif texto_2 >= texto_1:
    print("texto_2 es mayor")
'''
# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
'''
print(type(texto_1));
print(type(texto_1));
print(type(tx1));
print(type(tx2));
'''
tx1 = int(texto_1);
tx2 = int(texto_2);
print(tx1);
print(tx2);
if tx1 > tx2:
    print("texto_1 es mayor");
elif tx2 > tx1:
    print("texto_2 es mayor")

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
'Por lo que puedo entender, lo que evalúa en este caso el intérprete es el valor y no el tipo de dato...'
'ya que como tal no se pueden sumar texto_1 + texto_2 sino concatenarlos, en el caso que sean tipo Number...'
'ambos el intérprete tomaría el tipo de dato y el valor y ahí sí se podrían realizar operaciones aritméticas...'
"Como conclusión se puede decir que el '7' tiene un mayor valor que el '5' como tipos de datos String."