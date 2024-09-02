#Arrays necesarios
Lista_Alumnos = []
Primera_evaluacion = []
Segunda_evaluacion = []
Tercera_evaluacion = []
Media = []

#Función que se encargará de cargar los datos de un fichero de texto plano ya existente
def cargar_datos(file):
    datos = []
    try:
        with open(file, 'r') as f: #Operación de lectura sobre el fichero de texto
            for _ in range(4): #Salta las 3 primeras lineas del fichero
                next(f)
            for line in f: #Recorremos cada linea del fichero
                line = line.strip() 
                if line and not line.startswith('---'):
                    datos = line.split()
                    if len(datos) == 5:
                        Lista_Alumnos.append(datos[0])
                        Primera_evaluacion.append(int(datos[1]))
                        Segunda_evaluacion.append(int(datos[2]))
                        Tercera_evaluacion.append(int(datos[3]))
                        Media.append(float(datos[4])) 
    except FileNotFoundError:
        print(f"El archivo {file} no existe") #En caso de que el fichero sea inexistente
    else:
        print("Carga Ok!")
        print(f"{'Alumno':<13}{'1ra':<8}{'2da':<8}{'3ra':<8}{'Media':>10}") #Plantilla
        print("-" * 47)
        for i in range(len(Lista_Alumnos)):
            print(f"{Lista_Alumnos[i]:<12} {Primera_evaluacion[i]:>2} {Segunda_evaluacion[i]:>7} {Tercera_evaluacion[i]:>7} {Media[i]:>15.2f}")
        return datos

file = 'Juego_de_pruebas/prueba.txt'
respuesta = cargar_datos(file)