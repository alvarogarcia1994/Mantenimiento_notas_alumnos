#Array
Alumnos = ["Carla", "Juan", "Pepe", "Francisco", "Carla"];

#Función que se encarga de comprobar la existencia del nombre que figure en el array y cambiar la primera coincidencia por el nombre nuevo
def cambiar_nombre(Alumnos):
    try:
        nombre_antes = input(f"Nombre del alumno: ")
        if nombre_antes in Alumnos:
            nombre_despues = input("Nombre nuevo: ")
            index = Alumnos.index(nombre_antes)
            Alumnos[index] = nombre_despues 
        raise ValueError(f"{nombre_antes} no figura en la lista")
    except ValueError as e:
        print(e)
    return Alumnos

respuesta = cambiar_nombre(Alumnos)
print(respuesta)