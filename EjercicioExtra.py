"""
Desarrollar un programa que simule la tabla de posiciones de un torneo de fútbol. El
programa debe tener un menú
interactivo con las siguientes opciones:


1-Agregar un equipo al torneo.


2-Registrar un resultado ingresando equipo local, equipo visitante y marcador en formato 4 - 2.
El programa debe actualizar los puntos automáticamente (3 puntos por victoria, 1 por empate, 0 por derrota).


3-Mostrar la tabla de posiciones ordenada de mayor a menor puntaje.


4-Eliminar un equipo del torneo.


5-Salir del programa.


Se deben manejar situaciones como intentar agregar un equipo ya existente, registrar un
resultado con un equipo desconocido, o ingresar un marcador con formato inválido
"""


tabla = {
    "Boca" : 12,
    "River" : 10,
    "Racing" : 15,
    "Independiente" : 17
}
lista = ["0","1","2","3","4","5","6","7","8","9"]


while(True):
    print("""
    1-Agregar un equipo al torneo.
    2-Registrar un resultado ingresando equipo local, equipo visitante y marcador.
    3-Mostrar la tabla de posiciones ordenada de mayor a menor puntaje.
    4-Eliminar un equipo del torneo.
    5-Salir del programa.      
    """)
    opcion = int(input("Ingresar opcion: "))
    match opcion:
        case 1:
            bool=True
            while(bool):
                equipo = input("Escribir nombre de equipo a agregar: ")
                lista5 = tabla.keys()
                for elem in lista5:
                    if elem==equipo:
                        print("Equipo ya existente")
            bool=False
            tabla[equipo] = 0
        case 2:
            bool = True
            while(bool):
                letter = ""
                local = input('Ingresar equipo local: ')
                if not local in tabla:
                    print('Equipo no existe: ')
                    continue
                visi = input("Ingresar equipo visitante: ")
                if not visi in tabla:
                    print('Equipo no existe: ')
                    continue
                res = input("Ingrese marcador: ")
                lista3 = res.split()
                i=0
                if len(lista3) == 3:
                    for letter in res:
                        if letter in lista:
                            if i==0:
                                num1 = int(letter)
                                i = i+1
                            elif i==2:
                                num2 = int(letter)
                                bool = False
                        elif letter== "-" and (i==1):
                            i=i+1
            print("Marcador: ",res)
            if num1 > num2:
                puntL = 3
                puntV = 0
            elif num1 == num2:
                puntL = 1
                puntV = 1
            else:
                puntL = 0
                puntV = 3
            tabla[local] = tabla[local] + puntL
            tabla[visi] = tabla[visi] + puntV            
        case 3:
            lista2 = []
            max = -1
            llaves = tabla.keys()
            cant = len(tabla)
            for i in range(1,cant+1):
                max = -1
                pal = ""
                for elem in llaves:
                    if(tabla[elem]>=max)and(not elem in lista2):
                        max = tabla[elem]
                        pal = elem
                print("Pos: ",i," Equipo: ",pal," Puntos: ",max)
                lista2.append(pal)          
        case 4:
            bool = True
            while(bool):
                nom = input('Escriba equipo a eliminar: ')
                lista4 = tabla.keys()
                if nom in lista4:
                    tabla.pop(nom)
                    bool = False
                else:        
                    print('Equipo no existe')
        case 5:
            break
        case _:
            print('Opcion no existe')
