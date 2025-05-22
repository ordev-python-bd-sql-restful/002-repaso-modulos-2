# Código de la Sesión 2 🚀

¡Hola, crack! 👋 Aquí vas a encontrar todos los ejemplos de código que trabajamos en la sesión 2, ¡bien ordenaditos en sus carpetas!

Te súper recomiendo que le des un repaso al video de la sesión y, lo más importante, que te animes a ejecutar y escribir por tu cuenta lo que haga falta para completar los ejemplos. ¡No te quedes solo con ver! Documenta, crea más funciones basándote en lo que ya viste, y échale ganas a los ejercicios que te voy a plantear al final de este documento para que sigas reforzando tus súper poderes en Python. ¡Vamos que se puede! 💪

# Ejercicios Realizados 💻✨

Aquí te dejo las cuatro carpetas donde están los ejercicios que ya hicimos. ¡Son tu tesoro! 💰

1. [01-repaso_modulos](./01-repaso_modulos)

2. [02-ejemplo_paquete](./02-ejemplo_paquete)

3. [03-ejemplo_pip](./03-ejemplo_pip)

4. [04-por_que_venv](04-por_que_venv)

Para que puedas jugar con los ejemplos, solo tienes que moverte a cada directorio en tu terminal usando el comando `cd`. Así, podrás ejecutar los scripts de Python ¡como un verdadero mago! 🧙‍♂️

Y no te olvides de echarle un ojo al `README.md` que está dentro de cada directorio. Ahí vas a encontrar un resumen rápido de cada práctica. ¡Es como un mapa del tesoro! 🗺️

# Ejercicios Propuestos 🔓💡

¡Prepárate para el siguiente nivel! Estos ejercicios son tu campo de entrenamiento para convertirte en un/a verdadero/a ninja de Python. ¡A darle con todo!

## Ejercicio 1: ¡El Módulo Mágico y su Log Brillante! ✨📜

En el módulo que encuentras en la carpeta [01-repaso_modulos](./01-repaso_modulos), vamos a hacer un truco nuevo:

* Agrega una función extra que imprima un log ¡con estilo! El texto debe ir en MAYÚSCULAS y con una marca de tiempo súper precisa en formato `Y-M-D h:m:s` (hora militar). ¡Algo así como `2025-05-21 00:00:00# HOLA MUNDO`!

* Ponle el nombre que más te guste a esa función. ¡Sé creativo/a!

* ¡Y no te olvides de la documentación! Agrega el formato de docstrings que vimos en la sesión a *todas* las funciones. ¡Que no se te escape ninguna! Te dejo el formato por si lo olvidaste

```python
"""
Descripción breve de lo que hace la función.

Esta es una descripción más detallada de la función,
explicando su propósito, cómo funciona y cualquier
consideración importante.

Args:
    parametro1 (tipo): Descripción del primer parámetro.
                        Puede ocupar varias líneas si es necesario.
    parametro2 (tipo): Descripción del segundo parámetro.

Returns:
    tipo: Descripción del valor que retorna la función.
            Si la función no retorna nada, puedes omitir esta sección
            o indicar "None".

Raises:
    NombreDeExcepcion: Descripción de cuándo se lanza esta excepción.
                        (Opcional, solo si la función puede lanzar excepciones)

"""
```

Después, crea un nuevo script de Python que sea tu programa principal. En él, vas a:

* Probar todas las funciones de `module.py`. ¡A ver si funcionan!

* Imprimir la documentación de cada función del módulo. ¡Que se vea todo clarito!

* Imprimir la ruta del módulo. ¡Para saber dónde estamos parados!

## Ejercicio 2: ¡El Conversor Universal de Unidades! 📏🌡️⚖️

En la carpeta [02-ejemplo_paquete](./02-ejemplo_paquete), vamos a construir algo épico: ¡un conversor de unidades!

* Crea módulos nuevos para convertir unidades de:

  * Superficie 🏞️

  * Volumen 💧

  * Peso o masa 🏋️‍♀️

* En *todos* los módulos (sí, incluyendo los de temperatura y longitud que ya tienes), agrega al menos 3 conversiones de sistema imperial/anglosajón a sistema internacional, ¡y viceversa! Por ejemplo, de Acres a Hectáreas y de Onzas a Litros. ¡Serán dos funciones por cada conversión!

* ¡Vamos a hacer esto súper robusto! Agrega validaciones de valores donde sea necesario. Si alguien intenta convertir algo negativo o cero (como una superficie o volumen), ¡lanza una excepción con un mensaje que explique el problema! Piensa si puedes usar las excepciones de Python o si necesitas crear las tuyas. 🤔

* ¡Documenta todas las funciones! Y no olvides mencionar las excepciones que pueden lanzar.

Finalmente, crea un módulo para manejar menús y la entrada de datos. Con funciones como:

* Imprimir el menú.

* Leer datos numéricos por teclado con un mensaje personalizado.

* La función para leer datos puede tener un ciclo que valide si se ingresó un número válido. Si no, ¡que muestre un mensaje como "Debes ingresar un valor numérico, vuelve a intentarlo"!

* Usa excepciones o condicionales para que la validación de datos sea impecable.

Con todo esto listo, crea un programa principal llamado `unit_conversion_app.py`. Este programa debe:

* Mostrar un menú de conversión por tipo de unidad (Longitud, Temperatura, Área, Volumen, etc.).

* Después de seleccionar el tipo, pedir las unidades a convertir según las funciones que hayas desarrollado.

* ¡Usa el módulo de menú e ingreso de datos que creaste para que tu programa principal sea más sencillo y elegante!

## Ejercicio 3: ¡El Reporte Mágico de Temperaturas! 📊✨📄

Este es tu mini-proyecto estrella, donde aplicarás todo lo que has aprendido sobre módulos, paquetes y entornos virtuales. ¡Es hora de brillar!

Imagina que tienes un archivo `.csv` con lecturas de temperatura de todo el día. Cada línea tiene dos columnas: `hora,temperatura` en formato `hhmmss,temp`. Por ejemplo, `010555,12` significa que a la 01:05:55 AM la temperatura fue de 12 grados Celsius.

Tu programa debe:

* Pedir por teclado la ruta absoluta del archivo CSV (ej. "C:\\Documentos\\Temperaturas 20 Mayo 2025.csv"). Si el archivo no existe, ¡muestra un mensaje de error bien claro!

* También, pedir la ruta donde se guardará el archivo PDF con el reporte de temperaturas.

Una vez que el archivo CSV esté cargado:

* **Reporte en Consola "Pretty Printed"** 🎨: Muestra en la consola un reporte hermoso, usando colores y caracteres para dibujar una tabla con los títulos "HORA" y "TEMPERATURA". La hora debe verse en formato AM/PM y las temperaturas con un decimal. Al final del reporte, ¡agrega estos totales mágicos!:

  * Total de registros de Temperatura: N (el número de filas procesadas)

  * Temperatura Máxima: T a la hora HH:MM:SS P (temperatura y hora en formato AM/PM)

  * Temperatura Mínima: T a la hora HH:MM:SS P (temperatura y hora en formato AM/PM)

  * Promedio de Temperatura: P (Valor promedio a 2 decimales)

  * Desviación estándar de las Temperaturas: D (Valor de la desviación estándar a 2 decimales)

* **Reporte en PDF Elegante** 📝: Genera un reporte en PDF con un formato súper fácil de leer, con la misma tabla de registros y los resultados del punto anterior. Si hay algún problema al generar el PDF, ¡muestra un mensaje de error adecuado!

* **Opcional: ¡El Archivo de Configuración Secreto!** ⚙️: Los programas pro usan archivos de configuración. ¡Tú también puedes! Utiliza un archivo `config.yml` en formato Yaml para configurar cosas como:

  * Títulos de las columnas del reporte.

  * Color de los títulos y datos en consola.

  * Color y tipografía en el PDF.

  * Mensajes de ingreso de datos y de error.

  * Formato de la hora.

  * Cantidad de decimales en los registros de temperatura.

* **¡Documentación y Publicación!** 🚀: Agrega un `README.md` con las instrucciones de uso. Publica el proyecto en un repositorio de GitHub, ¡con archivos CSV de ejemplo! Y lo más importante, publica en el repo la documentación del código generada automáticamente.

**Para hacer este programa, ¡sigue estos pasos de superhéroe!** 🦸‍♀️🦸‍♂️

1. **Investiga Bibliotecas Poderosas** 📚: Busca bibliotecas que te ayuden con cada punto (por ejemplo, `rich` para colores y tablas en consola, `PyPDF2` para PDFs, etc.).

2. **Crea Módulos y Paquetes Estructurados** 🏗️: Divide tu programa en módulos para cada paso del proceso y crea un paquete que contenga toda la aplicación, ¡y que se pueda ejecutar desde un `__main__.py`!

3. **Entorno Virtual y Dependencias** 🌳📦: Crea un entorno virtual y su lista de dependencias en el archivo `requirements.txt`. ¡Orden y limpieza ante todo!

4. **¡Documenta Cada Función!** ✍️: No olvides documentar *todas* tus funciones. ¡Tu yo del futuro y otros desarrolladores te lo agradecerán!

5. **Generación de Documentación Automática** 🤖: Investiga qué herramientas o comandos puedes usar para generar la documentación de tu código en HTML u otros formatos a partir de tus docstrings. ¡Que el código se documente solo!

6. **¡Manos a la Obra! ¡Sin Miedo al Éxito!** ✨🚀

¡Ánimo, futuro/a gurú de la programación! Sigue practicando con esa misma chispa y verás cómo tus habilidades en Python se van al siguiente nivel. ¡El código te espera y el mundo necesita tus soluciones! 💪🐍