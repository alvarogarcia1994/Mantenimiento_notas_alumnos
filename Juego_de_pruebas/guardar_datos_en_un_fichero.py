#Arrays con información
Lista_Alumnos = ['Pepe', 'Francisco', 'Carla', 'Patricia']
Primera_evaluacion = [3, 8, 5, 4]
Segunda_evaluacion = [7, 2, 1, 4]
Tercera_evaluacion = [5, 2, 9, 10]
Media = [5.00, 4.00, 5.00, 6.00]

#Funcionalidad que se encargará de salvaguardar la información introducida en los arrays, 
def escribir(fichero):
    try:
        with open(fichero, 'w', encoding="utf-8") as file:
            file.write("Notas de los alumnos" + "\n")
            file.write("-" * 47 + "\n")
            file.write(f"{'Alumno':<13}{'1ra':<8}{'2da':<8}{'3ra':<8}{'Media':>10}" + "\n")
            for alumno, primera, segunda, tercera, media in zip(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media):
                file.write("-" * 47 + "\n")
                file.write(f"{alumno:<12} {primera:>2} {segunda:>7} {tercera:>7} {media:>15.2f}" + "\n")
            file.write("-" * 47 + "\n")
        print(f"Datos guardados en el archivo {fichero}")
    #Capturamos la excepción en caso de que no se pueda encontrar el fichero.
    except Exception as e:
        print(f"No se pudo completar la operación de guardado: {e}")

file_name = 'prueba.txt'
escribir(file_name)