import yaml

# Este programa no funciona con versiones nuevas
# de pyyaml > 6
# Puede funcionar con pyyaml 5.1
# Aún así da un warning porque es un código viejo

texto = """
personas:
  - nombre: Juan
    edad: 25
  - nombre: Maria
    edad: 30
"""

data = yaml.load(texto) 
print(data)