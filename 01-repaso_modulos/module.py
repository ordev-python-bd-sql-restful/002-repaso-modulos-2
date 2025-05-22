def print_log(message):
    print(f"LOG: {message}")

def print_error(message):
    print(f"ERROR: {message}")

# Programa principal para probar el módulo
# Y este no se va a ver, si se ejecuta como un import desde otro programa
if __name__ == "__main__":
    print("Prueba module")
    print_log("Hola")
    print_error("Error")
    print("Fin Prueba")