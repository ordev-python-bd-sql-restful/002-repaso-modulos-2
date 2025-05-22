# Justificación venv

Ahora veamos un ejemplo de la necesidad de tener entornos virtuales para tener versiones específicas de las dependencias de bibliotecas por proyecto.

Trabajaremos con la biblioteca `pyyaml` la cual sirve para escribir lectura y escritura de archivos yaml a  una variable tipo Dict en Python.

## Intentar usar un código viejo de pyyaml

Supongamos que encuentras un código de una aplicación o tutorial viejo como es el caso del script `yaml_old.py`, pero no hay una documentación acerca de la versión a usar la biblioteca. Por lo que pruebas instalando la última versión:

```
pip install pyyaml
```

Verifica la versión instalada con 

```
pip list
```

Luego de instalar la dependencia, intenta ejecutar el script `yaml_old.py` y revisa si hay algún error

## Ajustar la versión

Es necesario hacer un downgrade de la versión en pip. Debe hacerse lo siguiente

1. Desinstalar la versión actual de pyyaml.
2. Instalar una versión más antigua.

  ```
  pip uninstall pyyaml

  pip install pyyaml==5.1
  ```

Si ejecutas de nuevo el script `yaml_old.py` verás que se ejecuta, pero todavía muestra warnings, ya que es un código bastante viejo, para versiones < 3.1 de la biblioteca, pero estas versiones no funcionan con las versiones actuales de Python.

Esto nos da un ejemplo de por qué es necesario tener un manejo de dependencias separado por proyecto.

Para el caso de cómo se escribe el código con las versiones modernas de pyyaml ver el archivo `yaml_new.py`
