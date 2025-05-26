from unit_conversion import lenght

try:
    l = input("Ingresar longitud en metros: ")
    p = lenght.meters_to_feet(float(l))
except ValueError as e:
    print("Valor ingresado no válido")