
Primera = [1, 4, 6, 3, 7]
Segunda = [2, 5, 7, 1, 4]
Tercera = [5, 3, 8, 4, 4]


#Función que sirve para subir de suspenso a 5 todas las notas inferiores a 5.
def aprobar(primera, segunda, tercera):
    primera[:] = [5 if nota < 5 else nota for nota in primera]
    segunda[:] = [5 if nota < 5 else nota for nota in segunda]
    tercera[:] = [5 if nota < 5 else nota for nota in tercera]
    
    media = []

    for x, y, z in zip(primera, segunda, tercera):
        media.append((x+y+z) / 3)
    
    return primera, segunda, tercera, media
    

resultados = aprobar(Primera, Segunda, Tercera)
print(resultados)