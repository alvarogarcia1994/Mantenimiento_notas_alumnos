notas = []

#Función que se encargará de las buenas prácticas de la primera funcionalidad -- Insertar alumnos y tres notas. 
#La finalidad de de esta función es forzar al usuario a introducir un entero comprendido entre 0 y 10.
def valida_nota():
    while True:
        try:
            cal = int(input("Introduce una calificación: "))
            if cal < 0 or cal > 10:
                raise ValueError("La calificación debe estar entre 0 y 10")
            return cal
        except ValueError as e:
            print(e)
respuesta = valida_nota()