#Arrays con información
Lista_Alumnos = ['Pepe', 'Francisco', 'Carla', 'Patricia']
Primera_evaluacion = [3, 8, 5, 4]
Segunda_evaluacion = [7, 2, 1, 5]
Tercera_evaluacion = [5, 2, 9, 10]
Media = [5.00, 4.00, 5.00, 6.33]

#Muestra los alumnos, sus notas trimestrales y la nota media global de cada uno de ellos
def mostrar_notas():
    print(f"{'Alumno':<13}{'1ra':<8}{'2da':<8}{'3ra':<8}{'Media':>10}")
    print("-" * 47)
    for alumno, primera, segunda, tercera, media in zip(Lista_Alumnos, Primera_evaluacion, Segunda_evaluacion, Tercera_evaluacion, Media):
        print(f"{alumno:<12} {primera:>2} {segunda:>7} {tercera:>7} {media:>15.2f}")


mostrar_notas()