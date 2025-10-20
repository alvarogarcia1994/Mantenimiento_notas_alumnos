#Proyecto de programación. Mantenimiento de notas de alumnos
#Importaciones
import sys
from colorama import Fore

#Declaramos cuatro arrays donde guardaremos la siguiente información (Alumno, Nota_EV1, Nota_EV2 y Nota_EV3)
Lista_Alumnos = []
Primera_evaluacion = []
Segunda_evaluacion = []
Tercera_evaluacion = []

# Funciones a desarrollar
def menu_principal():
    print("------------------------------")
    print("Qué operación deseas realizar?")
    print("------------------------------")
    print("a) Insertar tres notas a partir de un nuevo alumno")
    print("m) Mostrar alumnos y sus notas")
    print("t) Aprobar alumnos que tengan notas inferiores a 5")
    print("n) Cambiar el nombre de un alumno/a existente")
    print("c) Cambiar nota de un alumno/a a partir de una evaluación")
    print("s) Guardar información en un archivo .txt")
    print("l) Carga la información guardada")
    print("?) Ayuda")
    print("x) Salir")


#Función que valida la opción introducida por teclado
def valida_opcion():
    return input("Elige una opción: ").strip().lower()

#Función que valida que la calificación introducida tiene un entero entre 0 y 10
def validar_calificacion():
    while True:
        try:
            calificacion = int(input("Introduce una calificación: "))
            if calificacion < 0 or calificacion > 10:
                raise ValueError("La calificación debe estar entre 0 y 10")
            return calificacion
        except ValueError as e:
            print(e)


#Función con la que añadiremos un nuevo alumno y tres notas, la media se calcula a partir de sumar las tres notas y posteriormente dividirlas por tres
def insertar_alumno_y_tres_notas(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion):
    alumno = str(input("Nombre del alumno/a: ").strip()[:15])
    nota_ev1 = validar_calificacion()
    nota_ev2 = validar_calificacion()
    nota_ev3 = validar_calificacion()
    
    Lista_Alumnos.append(alumno)
    Primera_evaluacion.append(nota_ev1)
    Segunda_evaluacion.append(nota_ev2)
    Tercera_evaluacion.append(nota_ev3)
    print(f"Alumno/a {alumno} añadido/a con éxito")

#Función que se encargará de calcular la nota media de las tres evaluaciones de forma dinámica
def calcular_medias(primera, segunda, tercera):
    return [(a + b + c) / 3 for a, b, c in zip(primera, segunda, tercera)]

#Función que muestra la tabla de alumnos con sus notas y la media artimética de las mismas
def mostrar_notas():
    if not Lista_Alumnos:
        print("No hay alumnos registrados.")
        return

    medias = calcular_medias(Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion)

    print(f"{'Alumno':<13}{'1ra':<8}{'2da':<8}{'3ra':<8}{'Media':>10}")
    print("-" * 47)
    for alumno, primera, segunda, tercera, media in zip(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, medias):
        if float(media) <= 4.99:
            print(f"{alumno:<12} {primera:>2} {segunda:>7} {tercera:>7} {Fore.RED}{media:>15.2f}{Fore.RESET}")
        else:
            print(f"{alumno:<12} {primera:>2} {segunda:>7} {tercera:>7} {Fore.BLUE}{media:>15.2f}{Fore.RESET}")
    print("-" * 47)

#Función que se encargará de aumentar la calificación las notas inferiores a 5.
def aprobar(primera, segunda, tercera):
    primera[:] = [5 if nota < 5 else nota for nota in primera]
    segunda[:] = [5 if nota < 5 else nota for nota in segunda]
    tercera[:] = [5 if nota < 5 else nota for nota in tercera]
    
    media = []
    for x, y, z in zip(primera, segunda, tercera):
        media.append((x+y+z) / 3)
    print("Se han subido a 5 todas las notas inferiores a 5")

#Función que modificará el nombre del primer alumno con dicho nombre, en caso contrario mostramos el mensaje de ERROR!
def cambiar_nombre(Alumnos):
    try:
        nombre_antes = input(f"Nombre del alumno: ").strip()
        if nombre_antes in Alumnos:
            nombre_despues = input("Nombre nuevo: ").strip()[:15]
            index = Alumnos.index(nombre_antes)
            Alumnos[index] = nombre_despues
        else:
            raise ValueError(f"{nombre_antes} no figura en la lista")
    except ValueError as e:
        print(e)
    print("Nombre cambiado con éxito")

#Función que a partir de un alumno en la lista modificaremos una de las notas (1ra, 2da o 3ra evaluación) y su media. En caso de que el número de la evaluación sea inferior a 1 o bien superior a 3 mostramos un mensaje de ERROR y también aplicamos esta praxis en caso de que el alumno introducido por teclado sea inexistente.
def modificar_calificacion(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion):
    nombre = input("Dime el nombre del alumno: ").strip()
    if nombre not in Lista_Alumnos:
        print(f"{nombre} no figura en la lista.")
        return

    try:
        eval_num = int(input("Dime la evaluación (1, 2 o 3): "))
    except ValueError:
        print("Introduce un número válido (1, 2 o 3).")
        return

    if eval_num not in (1, 2, 3):
        print("Evaluación no válida. Solo se admiten los valores 1, 2 y 3.")
        return

    nota_ev = validar_calificacion()
    
    index = Lista_Alumnos.index(nombre)
    if eval_num == 1:
        Primera_evaluacion[index] = nota_ev
    elif eval_num == 2:
        Segunda_evaluacion[index] = nota_ev
    else:
        Tercera_evaluacion[index] = nota_ev

    print("Calificación modificada con éxito.")



#Función que nos peritirá volcar la información existente en un fichero
def guardar_datos_fichero(fichero):
    try:
        medias = calcular_medias(Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion) if Lista_Alumnos else []
        with open(fichero, 'w', newline='', encoding="utf-8") as file:
            file.write("-" * 47 + "\n")
            file.write(f"{'Alumno':<13}{'1ra':<8}{'2da':<8}{'3ra':<8}{'Media':>10}" + "\n")
            for alumno, primera, segunda, tercera, media in zip(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, medias):
                file.write(f"{alumno:<12} {primera:>2} {segunda:>7} {tercera:>7} {media:>15.2f}" + "\n")
        print(f"Datos guardados en el archivo {fichero}")
    except Exception as e:
        print(f"Error al guardar: {e}")

#Función que nos permitirá cargar la información previa a partir de un fichero
def cargar_datos(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            for linea in file:
                linea = linea.strip()

                # Saltar líneas vacías, guiones('-') y la cabecera del fichero .txt
                if not linea or linea.startswith('-') or linea.startswith('Alumno'):
                    continue

                # Dividir por espacios (alineación)
                datos = linea.split()
                if len(datos) == 5:
                    alumno = datos[0]
                    ev1, ev2, ev3, media = map(float, datos[1:])
                    Lista_Alumnos.append(alumno)
                    Primera_evaluacion.append(int(ev1))
                    Segunda_evaluacion.append(int(ev2))
                    Tercera_evaluacion.append(int(ev3))

        print("Carga de datos realizada con éxito")

    except FileNotFoundError:
        print(f"El fichero {file} no existe")
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {e}")

#Función que ofrece un resumen de que hace cada una de las operaciones
def ayuda():
    print("a) Opción que se encarga de insertar un nuevo alumno y tres calificaciones")
    print("m) Muestra los alumnos con sus notas y su promedio")
    print("t) Sirve para subir las notas comprendidas entre el 0 y 4.99 hasta 5")
    print("n) Cambia el nombre de un alumno existente, en caso contrario ERROR!")
    print("c) Modifica la nota de un alumno/a a partir de una evaluación (1, 2 o 3)")
    print("s) Guarda la información existente en un fichero")
    print("l) Carga la información previa")
    print("?) Muestra ayuda de cada comando")
    print("x) Sale del programa")

if __name__ == "__main__":
    while True:
        menu_principal()
        opcion = valida_opcion()

        if opcion == 'a':
            insertar_alumno_y_tres_notas(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion)

        elif opcion == 'm':
            mostrar_notas()

        elif opcion == 't':
            aprobar(Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion)

        elif opcion == 'n':
            cambiar_nombre(Lista_Alumnos)

        elif opcion == 'c':
            modificar_calificacion(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion)

        elif opcion == 's':
            file_name = 'datos.txt'
            guardar_datos_fichero(file_name)

        elif opcion == 'l':
            file_name = 'datos.txt'
            cargar_datos(file_name)

        elif opcion == '?':
            ayuda()

        elif opcion == 'x':
            print("Hasta luego...")
            sys.exit()

        else:
            print("Opción no válida, por favor selecciona una opción válida.")