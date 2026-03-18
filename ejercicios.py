# 1. Escribe un programa que solicite al usuario su año de nacimiento y muestre en qué
# año cumplirá 18, 21 y 100 años.
# ano = int(input("Ingrese ano de nacimiento"))
# print("cumplira sus 18 anos en el ano",ano+18)
# print("cumplira sus 21 anos en el ano",ano+21)
# print("cumplira sus 100 anos en el ano", ano+100)
# 
# 2. Escribe un programa que solicite al usuario una cantidad de segundos y muestre
# cuántas horas, minutos y segundos equivalen. Por ejemplo, 3661 segundos son 1
# hora, 1 minuto y 1 segundo.
# seg = int(input("Ingrese segundos"))
# hora = seg // 3600
# minu = seg % 3600 // 60
# seg = (seg // 3600) % 60 
# print("horas",hora," minutos ",minu," segundos ",seg)
# 
# 3. Crea un programa que solicite al usuario un número y muestre su tabla de multiplicar
# del 1 al 10 utilizando un bucle for.
# num = int(input("ingresar numero"))
# for i in range(1,11):
#     print(" multiplo de ",i, " es ", num*i)
# 
# 4. Crea un programa que dado un número N ingresado por el usuario, imprima los
# números del 1 al N pero saltee los múltiplos de 5. Nota: utilizá la sentencia continue
# Entrega donde haga falta.
# num = int(input("ingrese numero: "))
# for i in range(1,num):
#     if(i % 5 == 0):
#         continue
#     else:
#         print(i)
# 
# 5. Escribe un programa que simule una caja registradora: el usuario ingresa precios de
# productos de a uno. Cuando ingresa 0, el programa se detiene y muestra el total
# acumulado. Nota: utilizá la sentencia break cuando haga falta.
# precio = float(input("ingrese precio del producto: "))
# total = 0.0
# while precio!=0:
#     total= total + precio
#     precio = float(input("ingrese precio del producto: "))
# print("el total acumulado es: ", total)    
# 
# 
# 6. Modifica el ejercicio 4 para que, en lugar de imprimir los números, genere dos listas:
# una con los múltiplos de 5 y otra con el resto de los números. Imprimí ambas listas al
# finalizar.
# lista1 = []
# lista2 = []
# num = int(input("ingrese numero: "))
# for i in range(1,num):
#     if(i % 5 == 0):
#         lista1.append(i)
#     else:
#         lista2.append(i)
# print(lista1)
# print(lista2)   
#    
# 7. Escribe un programa que solicite al usuario una lista de palabras. Luego, construí una
# oración uniendo únicamente las palabras que tengan más de 3 letras, separadas por
# espacios. Las palabras cortas deben ser excluidas del resultado final.
# lista = []
# elem = input("escribir una palabra: ")
# while(elem!="AAA"):
#     lista.append(elem)
#     elem = input("escribir una palabra: ") 
# oracion = ""
# for i in lista:
#     if(len(i)>3):
#         oracion = oracion + i + " "
# print(oracion) 