from colorama import Fore, Style, Back


# Programa principal

print(Fore.GREEN + "¡Hola mundo con colores!")
print(Style.RESET_ALL + "Este texto es normal.")
print(Fore.RED + "¡Cuidado!")
print(Fore.RED +  Style.BRIGHT + "¡Cuidado Bright!")
print(Fore.RED +  Style.DIM + "¡Cuidado DIM!")
print(Fore.MAGENTA + Back.YELLOW + "Texto con fondo")

# Resetear colores de la consola
print(Style.RESET_ALL + "Regresamos a la normalidad" + Style.RESET_ALL)

