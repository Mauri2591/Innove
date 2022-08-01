# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
from operator import le


texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if(texto_1 > texto_2):
    {
        print("texto_1 es mayor")
    }
elif(texto_2 > texto_1):
    {
        print("texto_2 es mayor")
    }

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if(len(texto_1) > len(texto_2)):
    {
        print("texto_1 tiene mayor cantidad de letras y son: ", len(texto_1))
    }
elif(len(texto_1) < len(texto_2)):
    {
        print("texto_2 tiene mayor cantidad de letras y son: ", len(texto_2))

    }

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

txt1 = texto_1[0]
txt2 = texto_2[0]
if(txt1 > txt2):
    {
        print("El caracter de texto_1 es mayor")
    }
elif(txt2 > txt1):
    {
        print("El caracter de texto_2 es mayor")
    }

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
copia_texto_1 = texto_1  # Copia de la variable texto_1
if(copia_texto_1 == texto_1):
    {
        print("Es igual")
    }
else:
    {
        print("No es igual")
    }
    
# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if(copia_texto_1 != texto_2):
    {
        print("Es distinto")
    }
else:
    {
        print("Es igual")
    }