# Arrays vacíos

Lista_Alumnos = [];
Primera_evaluacion = [];
Segunda_evaluacion = [];
Tercera_evaluacion = [];

def nuevo_alumno():
    alumno = input("Nombre del alumno: ")
    Lista_Alumnos.append(alumno)
    pri_nota = int(input("Calificación: "))
    Primera_evaluacion.append(pri_nota)
    seg_nota = int(input("Calificación: "))
    Segunda_evaluacion.append(seg_nota)
    ter_nota = int(input("Calificación: "))
    Tercera_evaluacion.append(ter_nota)
    print("Datos añadidos", Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion)

nuevo_alumno()