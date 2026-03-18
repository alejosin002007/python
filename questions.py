import random
diccionario = {
    "estructuras":["funcion","bucle","lista"],
    "datos":["cadena","entero","variable"],
    "ejecucion":["programa","python"]
}

guessed = []
attempts = 6
puntaje = 0
print("¡Bienvenido al Ahorcado!")
print(diccionario.keys())
llave = input("Eligir una categoria: ")
print()
res = diccionario.get(llave,"incorrecto")
if res!="incorrecto":
    word = random.sample(res,1)[0]#EL [0] SE PONE PARA QUE A WORD NO LE DE UNA LISTA DE UNA SOLA PALABRA/ELEMENTO, SINO QUE LE DE EL ELEMENTO EN SI, EL STRING. YA QUE SI NO DETECTARA A LA LISTA COMO SOLO UN ELEMENTO.
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntaje += 6
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        elif(letter>="a")and(letter<="z")and(len(letter)==1):
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
            puntaje -= 1
        else:
            guessed.append(letter)
            attempts -= 1
            print("Entrada no válida.")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje = 0
    print(f"El puntaje fue de {puntaje} puntos")
else:
    print("categoria incorrecta")
    
