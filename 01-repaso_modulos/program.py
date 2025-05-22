# Importar todo y notación punto
#import module
#module.print_log("Hola mundo 2")

# Importar una función con su mismo nombre
# from module import print_log
# print_log("Hola mundo 2")

# Importar una función con alias
from module import print_log as log
log("Hola mundo 3")

# Propiedades del módulo
print("Propiedades del módulo")
print(f"Nombre:  {__name__}")
print(f"Nombre Archivo: {__file__}")

# dir para revisar las funciones
# print("Directorio de funciones:")
# print(dir("module"))
