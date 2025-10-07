#Arrays necesarios
Lista_Alumnos = []
Primera_evaluacion = []
Segunda_evaluacion = []
Tercera_evaluacion = []
Media = []

#Función que se encargará de cargar los datos de un fichero de texto plano ya existente
def cargar_datos(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            for linea in file:
                linea = linea.strip()

                # Saltar líneas vacías, rayas y la cabecera
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

file = 'prueba.txt'
respuesta = cargar_datos(file)