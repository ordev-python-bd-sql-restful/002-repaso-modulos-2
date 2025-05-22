# Ejemplo dependencia sencilla con pip

En este ejemplo mostramos cómo instalar una dependencia con pip para poder utilizarla en un programa python.

## Colorama

Utilizaremos la biblioteca [colorama](https://pypi.org/project/colorama/), la cual provee funcionalidades sencillas para agregar colores al texto en la consola.  

## Instalación de la última versión

Para instalar la última versión de un  puedes usar el siguiente comando:

```
pip install colorama
```

Si no le agregas parámetros instalará la última versión. Si quisiéramos instalar una versión específica, por ejemplo la `0.4.0` podemos agregar el parámetro

```
pip install colorama==0.4.0
```

Para validar los paquetes instalados se puede usar el comando

```
pip lists 
```

Para desinstalar un paquete se puede usar `pip uninstall` como en el siguiente ejemplo

```
pip uninstall colorama
```

## Ejemplo colorama

Ahora se podrá ejecutar el script `hello_colorama.py` ya que se tiene la dependencia.
