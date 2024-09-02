from colorama import Fore

Media = [5.00, 3.00, 6.33, 4.99];

def colorizaMedia():
    for nota in Media:
        if (nota < 5):
            print(f"{Fore.RED}{nota:.2f}{Fore.RESET}")
        else:
            print(f"{Fore.BLUE}{nota:.2f}{Fore.RESET}")
colorizaMedia()

#Esta función no se utiliza en el programa original puesto que las acciones que reliza esta función se integran en la función mostrar_notas() del programa original.
#Básicamente, esta función consta de una prueba para colorizar de rojo la media inferior a 5 y de azul la media igual o superior a 5. 
