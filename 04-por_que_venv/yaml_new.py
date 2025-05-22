import yaml

texto = """
personas:
  - nombre: Juan
    edad: 25
  - nombre: Maria
    edad: 30
"""

data = yaml.load(texto, Loader=yaml.SafeLoader)  # ✔️ Funciona en versiones nuevas
print(data)