# Justificación de venv: ¡El Secreto para un Entorno Limpio y Feliz! 🌱✨

¡Eu! 👋 En esta sección, vamos a desentrañar el misterio de por qué necesitamos los entornos virtuales (`venv`). ¡Es como tener un espacio de trabajo súper ordenado para cada uno de tus proyectos! Así, las dependencias de tus bibliotecas no se hacen un lío entre sí.

Para entender esto, vamos a jugar con la biblioteca `pyyaml`, que es una joya para leer y escribir archivos `YAML` (¡esos que parecen listas y diccionarios!) en Python.

## ¡El Drama del Código Viejo de `pyyaml`! 🎭👴

Imagínate que te encuentras un código de una aplicación o un tutorial viejito, como el script `yaml_old.py`. El problema es que no hay ni una pista sobre qué versión de la biblioteca `pyyaml` usaron. Así que, ¡a la aventura! Intentas instalar la última versión:

```bash
pip install pyyaml
```

Ahora, intenta ejecutar el script `yaml_old.py` y... ¡sorpresa! Probablemente te encuentres con algún error. ¡No te preocupes, es parte de la diversión!

¡Ajustando la Versión: El Viaje en el Tiempo de Pip! ⏳🔧
Para que ese código viejito funcione, necesitamos hacer un "_downgrade_" (bajar la versión) de `pyyaml`. ¡Es como viajar en el tiempo con pip!

Primero, desinstalamos la versión actual y luego instalamos una versión más antigua, ¡la 5.1 en este caso!

```bash
pip uninstall pyyaml
pip install pyyaml==5.1
```

Si vuelves a ejecutar el script `yaml_old.py`, ¡verás que ahora sí funciona! Aunque, ojo, puede que todavía te muestre algunos "warnings" (advertencias), porque es un código bastante, bastante viejito (para versiones menores a la 3.1 de la biblioteca), y esas versiones ya no se llevan bien con las versiones actuales de Python.

¡Y justo aquí está la lección clave! Esto nos muestra por qué es tan necesario tener un manejo de dependencias separado para cada proyecto. ¡Así evitas dolores de cabeza y conflictos entre versiones!

Para que veas cómo se escribe el código con las versiones modernas de `pyyaml`, échale un ojo al archivo `yaml_new.py`. 

## ¡La Solución Mágica: Entornos Virtuales (venv)! ✨

Para evitar estos dramas de versiones y mantener tus proyectos impecables, ¡aquí entra en acción venv! Vamos a crear un entorno virtual para este proyecto y verás cómo todo se soluciona.

## Pasos para un Entorno Feliz y Ordenado: 🚀

Crea tu Santuario Virtual 🌳: Repasemos los pasos que hicimos en la sesión, para que los hagas por tu cuenta... 

### Crea tu entorno 🌳

Primero, asegúrate de estar en la raíz de tu proyecto (donde tienes `yaml_old.py` y `yaml_new.py`). Luego, crea el entorno virtual. ¡Puedes llamarlo venv o como quieras!

```bash
python -m venv venv
```

Esto creará una carpeta `venv` en tu proyecto. ¡Es tu nuevo mundo aislado!

### Activa la Magia 🪄

Para empezar a usar tu entorno virtual, necesitas activarlo. ¡Es como encenderlo!

En Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

En Windows (CMD):


```bash
.\venv\Scripts\activate.bat
```

Verás que el nombre de tu entorno (`(venv)`) aparecerá en tu terminal, ¡indicando que estás dentro!

Organiza tu Código 📂: Para mantener todo súper organizado, vamos a crear una carpeta para el código que usa pyyaml y mover el script viejito ahí.

```bash
mkdir programa_yaml_viejo
copy yaml_old.py programa_yaml_viejo/
```

Ahora, tu `yaml_old.py` está en su propio espacio.

### ¡Instalando la Versión Correcta! ⏳

Ahora que estás dentro de tu venv y con el código organizado, instala la versión `5.1` de `pyyaml` solo en este entorno:

```bash
pip install pyyaml==5.1
```


### Pinea tus Dependencias 📌: 

Para que cualquiera que use tu proyecto sepa exactamente qué versiones de las bibliotecas necesita, vamos a "pinear" las dependencias en un archivo requirements.txt. ¡Es como una lista de ingredientes para que tu receta siempre funcione!

```bash
pip freeze > requirements.txt
```

Esto creará un archivo `requirements.txt` con `pyyaml==5.1` (y cualquier otra dependencia que se haya instalado automáticamente con ella).

### ¡Prueba el programa de nuevo! ✨: 

Ahora, navega a la carpeta donde moviste el script viejito y ejecútalo.

```bash
cd programa_yaml_viejo
python yaml_old.py
```

¡Verás que ahora sí funciona! Aunque, ojo, puede que todavía te muestre algunos "warnings" (advertencias) como ya lo hablamos en la sesión...

Dominar esto te hará un/a programador/a mucho más eficiente y feliz. ¡Cada venv que creas es un paso más hacia la maestría! ¡A darle con todo! ✨🚀