def farenheit_to_celsius(fahrenheit):
   """Convierte temperatura de grados fahrenheit a celsius (centígrados)

   Args: (parámetros)
       fahrenheit (Float): La temperatura en Grados Fahrenheit

   Returns: (valor de retorno)
       Float: La temperatura en Celsius (Grados Centígrados)
   
   Raises: (excepciones que lanza)
       Ninguna.
   """
   return (fahrenheit - 32) * 5/9

def celsius_to_farenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    print(f"Prueba módulo {__file__}")
    print(f"100 C = {celsius_to_farenheit(100.00)} F")
