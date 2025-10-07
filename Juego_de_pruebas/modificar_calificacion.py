Alumnos = ["Pepe"]
Primera = [1]
Segunda = [2]
Tercera = [5]
Media = [2.66]

def valida_nota():
    while True:
        try:
            cal = int(input("Introduce una calificación: "))
            if cal < 0 or cal > 10:
                raise ValueError("La calificación debe estar entre 0 y 10")
            return cal
        except ValueError as e:
            print(e)

def modificar_calificacion(Alumnos, Primera, Segunda, Tercera, Media):
    try:
        nombre = input("Dime el nombre del alumno: ")
        if nombre in Alumnos:
            eval = int(input("Dime la evaluacion: "))
            if eval >= 1 and eval <= 3:
                nota_ev = valida_nota()
                index = Alumnos.index(nombre)
                evaluaciones = [Primera, Segunda, Tercera] #Declaramos que evaluaciones son las tres listas
                evaluaciones[eval - 1][index] = nota_ev #Dado que las listas se cuentan desde cero, para restringir esos valores a (1, 2 y 3) en términos de lista fijamos [eval - 1] para evitar el error de fuera de rango. [index] hace referencia al alumno.
                Media[index] = sum(evaluaciones[i][index] for i in range(3)) / 3 #Recalculando la nota media
            else:
                raise ValueError(f"Evaluación no válida. Solo se admiten los valores 1, 2 y 3.")
        else:
            raise ValueError(f"{nombre} no figura en la lista")
    except ValueError as e:
        print(e)
    return Alumnos, Primera, Segunda, Tercera, Media

print(modificar_calificacion(Alumnos, Primera, Segunda, Tercera, Media))

