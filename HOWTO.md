# Cómo crear un paquete local de Python

> Esta es una guía corta para la creación de un paquete en Python de uso local con la estructura de directorios y archivos disponibles en este repositorio.

Python amplía su funcionalidad por medio de paquetes (*packages*). Ya hemos utilizado varios de ellos: NumPy, SciPy y Matplotlib, entre otros. Es posible también crear *nuestros propios paquetes* para simplificar el uso de algunas funciones.

El Proyecto 4 es entregado en la forma de un paquete de Python en un repositorio de GitHub.

Este paquete realiza análisis comunes de procesos aleatorios, como la determinación de momentos y ergodicidad, para los datos de demanda de potencia del Sistema Eléctrico Nacional (ver `P4.ipynb`).

## Estructura de directorios y archivos

```
P4GX/
├─ setup.py
├─ proceso/
│  ├─ __init__.py
│  ├─ espectro.py
│  ├─ estacionaridad.py
│  ├─ momentos.py
│  ├─ proceso.py
├─ README.md
├─ HOWTO.md
├─ revision.py
├─ P4.ipynb
├─ .gitignore
```

- `setup.py` tiene metadatos del paquete, incluyendo autores y dependencias de otros paquetes.
- `proceso/` es un directorio con los módulos del paquete.
    - `__init__.py` es requerido para importar el directorio como un paquete y debe estar vacío.
    - `*.py` son los archivos donde están las funciones de cada módulo.
- `README.md` tiene la documentación y los resultados del proyecto.
- `HOWTO.md` es este documento.
- `revision.py` es el archivo utilizado para revisar la funcionalidad del proyecto.
- `P4.ipynb` es el enunciado del proyecto y está aquí solamente como referencia.
- `.gitignore` tiene los archivos, directorios o extensiones que son ignorados al hacer confirmaciones (*commits*) con Git, generalmente porque se trata de archivos de uso local que no deben ser compartidos con el repositorio.

## Requisitos previos

1. Actualizar `pip` (*Package Installer for Python*):

```bash
$ python -m pip install --upgrade pip
```

2. Instalar librerías para creación de paquetes:

```bash
$ pip install setuptools
$ pip install wheel
```

- `setuptools` es para descargar, compilar, instalar, actualizar y desinstalar paquetes de Python.
- `wheel` es una extensión de `setuptools` que crea archivos WHL (Wheel) para distribución de paquetes que contienen todos los archivos y metadatos necesarios para la instalación.

## Creación del paquete

> Ejecutar en la interfaz de línea de comandos de su computadora, en el mismo directorio donde está el repositorio local del proyecto.

**Nota**: puede navegar los directorios de su computadora con el comando `cd` (*change directory*) o `dir`. Ejemplo: `$ cd /Users/maria/Documentos/MPSS/Proyecto4/P4G17` (cambia según el sistema operativo).

1. Creación de los archivos WHL (Wheel): 

```bash
$ python setup.py bdist_wheel
```

Esto creará varios directorios nuevos: `build`, `dist` y `proceso.egg-info`, con los que `pip` hace la instalación en el paso siguiente.

2. Instalación local del paquete con `pip`:

```bash
$ pip install /ubicacion/del/directorio/del/proyecto
```

**Nota**: puede encontrar `/ubicacion/del/directorio/del/proyecto` con el comando `pwd` (*print working directory*). O bien, si ya está en ese directorio (donde está `setup.py`), basta con hacer:

```bash
$ pip install .
```

donde `.` significa el directorio actual. Si todo resulta bien, saldrá algo como:

```bash
Successfully installed proceso-0.0.1
```

3. Verificación de la instalación

```bash
$ pip show proceso
```

donde mostrará la información del paquete, o bien `pip list`, donde está la lista de todos los paquetes instalados y su versión.

Ahora el paquete `proceso` está disponible para ser utilizado localmente en cualquier programa de Python, importando sus módulos, por ejemplo:

```python
from proceso import proceso, momentos, estacionaridad

proceso.densidad()
...
```

## Revisión del proyecto

- **Funcionalidad**: la revisión de la funcionalidad debe estar en el archivo `revision.py`. Este archivo es una demostración del proyecto y debe ser editado por el grupo para mostrar los resultados apropiados según el desarrollo de cada función y las decisiones tomadas en cuanto a sus argumentos de entrada. En la versión provista de ejemplo, `revision.py` solamente imprime una frase que indica que viene de una función particular. 
- **PEP-8**: la revisión será hecha con:
```bash
$ pycodestyle proceso/proceso.py
$ pycodestyle proceso/momentos.py
$ pycodestyle proceso/estacionaridad.py
```
Los códigos de error de `pycodestyle` están disponibles en su [documentación](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes).
- **PEP-257** (*docstrings*): la revisión será hecha con:
```bash
$ pydocstyle proceso/proceso.py
$ pydocstyle proceso/momentos.py
$ pydocstyle proceso/estacionaridad.py
```
Los códigos de error de `pydocstyle` están disponibles en su [documentación](https://www.pydocstyle.org/en/stable/error_codes.html).

Por favor hacer esta revisión antes y corregir todos los errores de formato que ahí se indican.

## Referencias

Para conocer más sobre la creación de paquetes en Python:

- [How to create a Python library](https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f)
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Setuptools Quickstart](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)
