# Programa de conversion de temperatura
# from unit_conversion import temperature
from unit_conversion.temperature import celsius_to_farenheit 
from unit_conversion.temperature import farenheit_to_celsius

def menu():
    print("Conversion de temperatura - Menu")
    print("1 - Convertir C a F")
    print("2 - Convertir F a C")
    print("3 - Salir del programa")
    return input("Seleccione la opción (1-3): ")
    

# programa principal
# ciclo con menu
while True:
    # menu
    opcion = menu()
    if opcion == "1":
        # c a f
        c = input("Ingrese temperatura en Celsius: ")
        f =celsius_to_farenheit(float(c))
        print(f"La temperatura en Farenheit = {f}")
    elif opcion == "2":
        # f a c
        f = input("Ingrese temperatura en Farenheit: ")
        c = farenheit_to_celsius(float(f))
        print(f"La temperatura en Celsius = {c}")
    elif opcion == "3":
        break
    else:
        print("Opcion inválida, debe elegir entre 1 y 3")

