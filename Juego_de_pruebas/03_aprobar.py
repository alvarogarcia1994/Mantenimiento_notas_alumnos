
Primera = [1, 4, 6, 3]
Segunda = [2, 5, 7, 1]
Tercera = [5, 3, 8, 4]
Media = [2.66, 4.00, 7.00, 2.66]

#Función que sirve para subir de suspenso a 5 todas las notas inferiores a 5.
def aprobar(Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media):
    Primera_evaluacion[:] = [5 if nota < 5 else nota for nota in Primera_evaluacion]
    Segunda_evaluacion[:] = [5 if nota < 5 else nota for nota in Segunda_evaluacion]
    Tercera_evaluacion[:] = [5 if nota < 5 else nota for nota in Tercera_evaluacion]
    Media[:] = [5 if calificacion < 5 else calificacion for calificacion in Media]
    return Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media


print(aprobar(Primera,Segunda,Tercera,Media))