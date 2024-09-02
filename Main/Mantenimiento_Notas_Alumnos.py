#Proyecto de programación. Mantenimiento de notas de alumnos
#Importaciones
import os;
from colorama import Fore

#Declaramos cinco arrays donde guardaremos la siguiente información (Alumno, Nota_EV1, Nota_EV2, Nota_EV3 y Media aritmética)
Lista_Alumnos = []
Primera_evaluacion = []
Segunda_evaluacion = []
Tercera_evaluacion = []
Media = []

# Funciones a desarrollar
def menu_principal():
    print("Qué operación deseas realizar?");
    print("------------------------------");
    print("a) Insertar tres notas a partir de un nuevo alumno");
    print("m) Mostrar alumnos y sus notas");
    print("t) Aprobar alumnos que tengan notas inferiores a 5");
    print("n) Cambiar el nombre de un alumno/a existente");
    print("c) Cambiar nota de un alumno/a a partir de una evaluación");
    print("s) Guardar información en un archivo .txt");
    print("l) Carga la información guardada")
    print("?) Ayuda");
    print("x) Salir");

#Función que valida que la calificación introducida tiene un entero entre 0 y 10
def validar_calificacion():
    while True:
        try:
            cal = int(input("Introduce una calificación: "))
            if cal < 0 or cal > 10:
                raise ValueError("La calificación debe estar entre 0 y 10")
            return cal
        except ValueError as e:
            print(e)


#Función con la que añadiremos un nuevo alumno y tres notas, la media se calcula a partir de sumar las tres notas y posteriormente dividirlas por tres
def insertar_alumno_y_tres_notas(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media):
    alumno = str(input("Nombre del alumno/a: ")[0:15]);
    nota_ev1 = validar_calificacion()
    nota_ev2 = validar_calificacion()
    nota_ev3 = validar_calificacion()
    media = (nota_ev1 + nota_ev2 + nota_ev3) / 3
    Lista_Alumnos.append(alumno);
    Primera_evaluacion.append(nota_ev1);
    Segunda_evaluacion.append(nota_ev2);
    Tercera_evaluacion.append(nota_ev3);
    Media.append(media);

#Función que muestra la tabla de alumnos con sus notas y la media artimética de las mismas
def mostrar_notas():
    mostrados = []  # Array local para mostrar los alumnos
    print(f"{'Alumno':<13}{'1ra':<8}{'2da':<8}{'3ra':<8}{'Media':>10}")
    print("-" * 47)
    for alumno, primera, segunda, tercera, media in zip(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media):
        if alumno not in mostrados:
            mostrados.append(alumno)
            if float(media) <= 4.99:
                print(f"{alumno:<12} {primera:>2} {segunda:>7} {tercera:>7} {Fore.RED}{media:>15.2f}{Fore.RESET}")
            else:
                print(f"{alumno:<12} {primera:>2} {segunda:>7} {tercera:>7} {Fore.BLUE}{media:>15.2f}{Fore.RESET}")

#Función que se encargará de aumentar la calificación las notas inferiores a 5.
def aprobar(Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media):
    Primera_evaluacion[:] = [5 if nota < 5 else nota for nota in Primera_evaluacion]
    Segunda_evaluacion[:] = [5 if nota < 5 else nota for nota in Segunda_evaluacion]
    Tercera_evaluacion[:] = [5 if nota < 5 else nota for nota in Tercera_evaluacion]
    Media[:] = [5 if calificacion < 5 else calificacion for calificacion in Media]
    return Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media

#Función que modificará el nombre del primer alumno con dicho nombre, en caso contrario mostramos el mensaje de ERROR!
def cambiar_nombre(Alumnos):
    try:
        nombre_antes = input(f"Nombre del alumno: ")
        if nombre_antes in Alumnos:
            nombre_despues = input("Nombre nuevo: ")
            index = Alumnos.index(nombre_antes)
            Alumnos[index] = nombre_despues
        else:
            raise ValueError(f"{nombre_antes} no figura en la lista")
    except ValueError as e:
        print(e)

#Función que a partir de un alumno en la lista modificaremos una de las notas (1ra, 2da o 3ra evaluación) y su media. En caso de que el número de la evaluación sea inferior a 1 o bien superior a 3 mostramos un mensaje de ERROR y también aplicamos esta praxis en caso de que el alumno introducido por teclado sea inexistente.
def modificar_calificacion(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media):
    try:
        nombre = input("Dime el nombre del alumno: ")
        if nombre in Lista_Alumnos:
            eval = int(input("Dime la evaluacion: "))
            if eval >= 1 and eval <= 3:
                nota_ev = validar_calificacion()
                index = Lista_Alumnos.index(nombre)
                evaluaciones = [Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion] #Declaramos que evaluaciones son las tres listas
                evaluaciones[eval - 1][index] = nota_ev #Dado que las listas se cuentan desde cero, para restringir esos valores a (1, 2 y 3) en términos de lista fijamos [eval - 1] para evitar el error de fuera de rango. [index] hace referencia al alumno.
                Media[index] = sum(evaluaciones[i][index] for i in range(3)) / 3 #Recalculando la nota media
            else:
                raise ValueError(f"Evaluación no válida. Solo se admiten los valores 1, 2 y 3.") #En caso de que al pedir la evaluación el valor sea inferior a 1 o bien igual o superior a 4. Levantamos una excepcion
        else:
            raise ValueError(f"{nombre} no figura en la lista") #Aplicamos la misma práctica, en caso de que el alumno no figure en la lista de alumnos
    except ValueError as e:
        print(e) 

#Función que nos peritirá volcar la información existente en un fichero
def guardar_datos_fichero(fichero):
    try:
        with open(fichero, 'w+') as file:
            file.write("Notas de los alumnos" + "\n")
            file.write("-" * 47 + "\n")
            file.write(f"{'Alumno':<13}{'1ra':<8}{'2da':<8}{'3ra':<8}{'Media':>10}" + "\n")
            for alumno, primera, segunda, tercera, media in zip(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media):
                file.write("-" * 47 + "\n")
                file.write(f"{alumno:<12} {primera:>2} {segunda:>7} {tercera:>7} {media:>15.2f}" + "\n")
            file.write("-" * 47 + "\n")
        print(f"Datos guardados en el archivo {fichero}")
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {fichero}")

def cargar_datos(file):
    datos = []
    try:
        with open(file, 'r') as f:
            for _ in range(4): #Salta las 3 primeras lineas del fichero
                next(f)
            for linea in f:
                linea = linea.strip() 
                if linea and not linea.startswith('---'):
                    datos = linea.split()
                    if len(datos) == 5:
                        Lista_Alumnos.append(datos[0])
                        Primera_evaluacion.append(int(datos[1]))
                        Segunda_evaluacion.append(int(datos[2]))
                        Tercera_evaluacion.append(int(datos[3]))
                        Media.append(float(datos[4])) 
    except FileNotFoundError:
        print(f"El fichero {file} es inexistente")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    else:
        print(f"Carga de datos ok!!")
        return datos

#Función que ofrece un resumen de que hace cada una de las operaciones
def ayuda():
    print("a) Opción que se encarga de insertar un nuevo alumno y tres calificaciones");
    print("m) Muestra los alumnos con sus notas y su promedio");
    print("t) Sirve para subir las notas comprendidas entre el 0 y 4.99 hasta 5");
    print("n) Cambia el nombre de un alumno existente, en caso contrario ERROR!");
    print("c) Modifica la nota de un alumno/a a partir de una evaluación (1, 2 o 3)");
    print("s) Guarda la información existente en un fichero");
    print("l) Carga la información previa")
    print("?) Muestra ayuda de cada comando");
    print("x) Sale del programa");

menu_principal()

#Definimos como un string la opción.
opcion = str;

#Mientras no pulsemos la x
while(opcion != 'x'):
    if(opcion == 'a'):
        insertar_alumno_y_tres_notas(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media)

    elif(opcion == 'm'):
        mostrar_notas()

    elif(opcion == 't'):
        aprobar(Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media)

    elif(opcion == 'n'):
        cambiar_nombre(Lista_Alumnos)

    elif(opcion == 'c'):
        modificar_calificacion(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media)
    
    elif(opcion == 's'):
        file_name = 'datos.txt'
        guardar_datos_fichero(file_name)
    
    elif(opcion == 'l'):
        file_name = 'datos.txt'
        cargar_datos(file_name)

    elif(opcion == '?'):
        ayuda()

    elif(opcion == 'x'):
        os.exit()
        
    opcion = str(input("Elige una opción: "));