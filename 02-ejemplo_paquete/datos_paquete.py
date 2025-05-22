# Obtiene datos del paquete
import unit_conversion
import unit_conversion.temperature

if __name__  == "__main__":
    print(unit_conversion.__doc__)

    print("documentacion de convecion F a C")
    print(unit_conversion.temperature.farenheit_to_celsius.__doc__)