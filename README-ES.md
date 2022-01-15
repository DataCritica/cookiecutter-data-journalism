### [English](README.md)

---

# Cookiecutter Periodismo de Datos 🍪
Una plantilla de [cookiecutter](https://github.com/cookiecutter/cookiecutter) para proyectos de periodismo de datos con Python
---

## ¿Por qué usar esta plantilla? 🚀

El vínculo entre los datos y el periodismo de investigación está creciendo con fuerza. En la era del big data, se abre un campo para indagar en los contenidos digitales y descubrir nuevas historias.

De modo que aunque hay muchos contenidos para ciencia de datos, necesitamos contenidos y herramientas adaptados para el periodismo de datos con el fin de enfatizar la importancia del reportaje, ya que no se trata sólo de analizar y visualizar datos, sino de contar historias sobre los descubrimientos humanizando esos datos.

> ### *Desarrollar buenas practicas*

Trabajar con grandes cantidades de datos puede resultar en varias tablas dinámicas, gráficos e inevitablemente en diferentes versiones de nuestro código y datos. Así que cuando se trata de inspeccionar nuestros propios proyectos, no estamos segurxs de cuál es la versión final de los datos entre archivos llamados *datos_limpios* y *datos_procesados*, y peor aún, no recordamos si *graficos_funcionando* o *graficos_nuevos* es el código que realmente funciona para hacer un gráfico entre muchos otros casos. 

> ### *Hacer nuestro trabajo transparente y de código abierto*

Es difícil explorar un proyecto desorganizado y aún más difícil reproducirlo, por esa razón cuando reunimos proyectos estructurados y documentados para el periodismo de datos, hacemos que sean más fáciles de replicar para otros y escudriñar las decisiones metodológicas que a veces no son bien captadas por las historias publicadas. 

Por último, pero no por ello menos importante, compartir nuestros métodos y códigos de trabajo basados en datos puede ser útil para que otros periodistas los reutilicen para su propia investigación o para que rindan cuentas de nuestra investigación garantizando que la información se comunica con veracidad.

> ### *Fomentar un periodismo de datos abierto*

En resumen, si queremos que lxs periodistas compartan su trabajo, tenemos que hacer un cambio en los flujos de trabajo existentes, pero eso supondría un esfuerzo adicional y, por tanto, una inversión de tiempo, por lo que esta plantilla puede servir como una herramienta, entre muchas otras, para ayudar al periodismo de datos a lograr la transparencia.

## Contenidos
- [Características](#características)
- [Instalación](#instalación)
- [Estructura de Directorios](#estructura-de-directorios)
- [Flujo de Trabajo](#flujo-de-trabajo)
- [Entorno Virtual de Python](#entorno-virtual-de-python)
- [Paquetes de Python](#paquetes-de-python)
- [Inicialización de Git](#inicialización-de-git)
- [Otras Plantillas](#otras-plantillas)

---

## Características

Esta plantilla estandariza los proyectos para el periodismo de datos y acelera su creación al automatizar el trabajo repetitivo cuando se genera un nuevo proyecto.

- Aporta el andamiaje de un proyecto con la ayuda de una [estructura de directorios](#estructura-de-directorios) diseñada en torno a las etapas del análisis de datos y al reportaje de historias.

- Mejora el proceso de análisis con fases establecidas de un [flujo de trabajo](#flujo-de-trabajo) típico del periodismo de datos.

- Automatiza la creación de un [entorno virtual](#entorno-virtual-de-python) para hacer un proyecto de datos aislado y reproducible.

- Instala [paquetes de python](#paquetes-de-python) útiles durante el análisis de datos: pandas, numpy y plotly.

- Inicializa un repositorio local de [git](#inicialización-de-git) con el fin de gestionar un control de versiones del proyecto.

- Soporta instalación en Linux, MacOS y Windows. 

---

## Instalación 

- ### **Guía rápida**

    Primero necesitas instalar `cookiecutter` ya sea con [pip](https://pip.pypa.io/en/stable/) o [conda](https://docs.conda.io/en/latest/).

    - Instalación con `pip`:

    ```
    pip install cookiecutter
    ```

    - Instalación con `conda`:

    ```
    conda config --add channels conda-forge
    conda install cookiecutter
    ```

    Para más información sobre la instalación de cookiecutter lee la [documentación](https://cookiecutter.readthedocs.io/en/latest/installation.html).

- ### **Inicia un nuevo proyecto**

    Ahora installa la plantilla para periodismo de datos:

    ```
    cookiecutter https://github.com/fer-aguirre/cookiecutter-data-journalism
    ```

- ### **Configura tu proyecto**
    ```
    > Selecciona un nombre del proyecto:

    > Selecciona un slug del proyecto:

    > Escribe una descripción del proyecto:

    > Selecciona un autor del proyecto:

    > Selecciona una licencia: 
        1. MIT
        2. GNU General Public License v3

    > Selecciona un sistema operativo:
        1. Linux
        2. MacOS
        3. Windows

    > Selecciona una configuración para el proyecto (Crear un entorno virtual e instalar paquetes):
        1. Sí
        2. No

    > Selecciona inicializar git:
        1. Sí
        2. No
    ```

- ### **Ejemplo**

    [![asciicast](https://asciinema.org/a/U74YPnb708uumNopBsl7he2bp.svg)](https://asciinema.org/a/U74YPnb708uumNopBsl7he2bp)

- ### **Requisitos**

    La plantilla trabaja con cuadernos de jupyter, en caso de que no tengas una configuración para [jupyter](https://jupyter.org/), ejecuta el siguiente comando: 

    ```
    pip install jupyterlab notebook
    ```

---

## Flujo de Trabajo

1. Configurar el proyecto 🔧
2. Procesar datos 🧼
3. Analizar datos 🔎
4. Visualizar datos 📊
5. Redactar un informe ✏️
6. Publicar una noticia 👥

---

## Estructura de Directorios

```
|- .gitignore              # Personalización de .gitignore para proyectos en python
|- LICENSE                 # Licencia del proyecto
|- README.md               # README principal del proyecto
|
|- data                    # Carpeta de datos clasificados                     
| |- processed             # Datos limpios
| |- raw                   # Datos originales
|
|- docs                    # Material explicativo
|  |- references           # Publicaciones académicas, artículos, manuales, etc.
|  |- reports              # Reporte del análisis en PDF, HTML, etc.
|  |- data-dictionary.md   # Información sobre los datos
|  |- explore-data.md      # Preguntas para explorar los datos
|
|- notebooks               # Cuadernos de jupyter
|  |- 0.0-process.ipynb    # Procesamiento de datos (arreglar tipos de columnas, limpieza de datos, etc.)
|  |- 1.0-analyze.ipynb    # Análisis exploratorio de datos
|  |- 2.0-visualize.ipynb  # Métodos de visualización de datos
|
|- outputs                 # Exportaciones generadas por los cuadernos
|   |- tables              # Tablas dinámicas generadas para el análisis
|   |- figures             # Generación de gráficos, mapas, etc. para su uso en los informes
|  
|- Pipfile                 # Dependencias del proyecto
```

- ### `.gitignore`

    El archivo contiene una [plantilla](https://github.com/github/gitignore/blob/main/Python.gitignore) para proyectos de python.

- ### `LICENSE`

     Los repositorios públicos necesitan una licencia de código abierto para poder ser utilizados, modificados y distribuidos. Por esta razón, con esta plantilla puedes elegir entre una [Licencia MIT](https://choosealicense.com/licenses/mit/) o una [Licencia Pública General GNU v3](https://choosealicense.com/licenses/gpl-3.0/).

    Para más información sobre cómo licenciar tu código, consulta este [sitio](https://choosealicense.com/).

- ### `README.md`

    Un README es un archivo markdown que introduce y da una descripción del proyecto. Incluye la información necesaria para entender de qué trata el proyecto.

    Aquí hay un [manual](https://www.makeareadme.com/) sobre cómo crear un archivo README, un [artículo](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) sobre cómo escribir markdown y un enlace para probar un [editor en línea](http://editor.md.ipandao.com/en.html).

- ### `data`

    La sección de datos contiene dos directorios: `raw` y `processed`:

    - ### `raw`

    Los archivos de datos originales deben permanecer intactos y utilizarse únicamente con fines de consulta.

    - ### `processed`

    Todo lo relacionado con la limpieza y el pulido de datos debe ir en esta carpeta.

- ### `docs`

    Esta categoría consta de dos directorios (`references` y `reports`) y dos archivos markdown (`data-dictionary.md` y `explore-data.md`):

    - ### `references`

        Esta carpeta contiene todos los documentos que sirven de referencia para el proyecto, como publicaciones académicas, artículos, otras publicaciones periodísticas, entrevistas, solicitudes de información, documentación de los datos, etc.

    - ### `reports`

        Aquí están los reportes que dan cuenta del análisis de los datos, ponen en palabras los resultados de los gráficos y de todo lo exportado por el código.

    - ### `data-dictionary.md`

        Información sobre la base de datos o, en otras palabras, metadatos para poner la base en contexto, como la descripción de a qué se refiere cada columna.

    - ### `explore-data.md`
        Una plantilla para realizar un análisis exploratorio tratando nuestros datos como una fuente de información más y, por lo tanto, haciéndoles preguntas y averiguando qué nos dicen los datos. En este punto también tenemos que interrogar el contexto de los datos, quién los ha recolectado, cómo se han recolectado, con qué propósito y, además, considerar la posible falta de datos o voces que faltan.

        Esta plantilla está inspirada en [Putting data back into context](https://datajournalism.com/read/longreads/putting-data-back-into-context).

- ### `notebooks`

    Esta parte abarca los cuadernos jupyter divididos en tres categorías: procesamiento, análisis y visualización. Estas secciones, a su vez, pueden tener también subcategorías, de ahí que su nomenclatura contenga una enumeración para ordenarlas.

    - ### `0.0-process.ipynb`

    Durante el procesamiento limpiaremos los datos, corregiremos los tipos de variables y, en general, realizaremos procedimientos para que las categorías de datos sean comparables.

    - ### `1.0-analyze.ipynb`

        En esta etapa se extrae información significativa de los datos mediante la agrupación, el filtrado, la comparación, el cálculo, entre otros muchos métodos, con el fin de encontrar patrones y relaciones entre las categorías.

    - ### `2.0-visualize.ipynb`

    Después el análisis exploratorio, hacemos representaciones visuales de lo que se ha descubierto en el análisis, para lo cual podemos elegir entre una amplia gama de gráficos para comunicar esta información.

- ### `outputs`

    Esta sección está compuesta por dos directorios: `tables` y `figures`.

    - ### `tables`

        Esta carpeta contiene tablas simples y tablas dinámicas generadas en los cruces de diferentes variables del conjunto de datos.

    - ### `figures`

        Aquí van los gráficos, diagramas, mapas u otros tipos de visualizaciones generadas en los cuadernos.  

- ### `Pipfile`

    Archivo creado cuando se genera el entorno virtual con `pipenv`. Este archivo enumera todos los paquetes utilizados en el proyecto.

---

## Entorno Virtual de Python

Durante la generación del proyecto, se preguntará si deseas crear un entorno virtual, si aceptas [pipenv](https://pypi.org/project/pipenv/) se instalará y creará un entorno para el proyecto.

Un entorno virtual es una herramienta que separa las dependencias de diferentes proyectos. Esto significa que podemos tener proyectos aislados con sus propios paquetes, pero además nos ayudará a que nuestra investigación sea reproducible, ya que listar todas las bibliotecas necesarias para reproducir un resultado debe ser parte de nuestro flujo de trabajo.

Pipenv tiene varias ventajas en comparación con otras bibliotecas como `virtualenv` o `virtualenvwrapper`. Sus principales características son que ya no es necesario utilizar `pip` ya que está integrado en el comando `pipenv`. Asimismo su `Pipfile` es mucho más fácil de usar y entender que un archivo `requirements.txt`.

Para más información sobre `pipenv` puedes leer la [documentación](https://pipenv.pypa.io/en/latest/).

---

## Paquetes de Python
Si se acepta la opción anterior, también se instalará una selección de paquetes para un análisis básico de datos en periodismo.

| Biblioteca | Documentación  |
| :-: | :-: |
| ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) | [Pandas](https://pandas.pydata.org/)
| ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)  | [Numpy](https://numpy.org/doc/stable/)
| ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white) | [Plotly](https://plotly.com/python/)

Además de estos paquetes, también se instalará [IPython kernel](https://ipython.readthedocs.io/en/stable/install/kernel_install.html) con el fin de utilizar un kernel con el entorno virtual. 

---

## Inicialización de Git 

El uso de git es una forma de poder gestionar las diferentes versiones de un proyecto y, por tanto, tener una copia de seguridad del mismo. Podemos tener este historial en nuestro propio ordenador a través de un repositorio local o tenerlo disponible en cualquier momento a través de un repositorio remoto en servidores (como GitHub o GitLab), de forma que podemos sincronizar estos repositorios a medida que hagamos cambios en ellos.

En caso de que no tengas instalado git, aquí tienes una breve guía sobre cómo descargarlo según tu sistema operativo.

### Instalación

- ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

    Debian y Ubuntu:

    ```
    sudo apt-get update && sudo apt-get upgrade
    sudo apt-get install git
    ```

    Para otras distribuciones de Linux consulta esta [guía](https://git-scm.com/download/linux).

- ![MacOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)

    Puedes ejecutar `git` en tu terminal y si no lo tienes instalado, te pedirá que lo instales:

    ```
    git --version
    ```

    Además tienes otras [opciones](https://git-scm.com/download/mac) como instalarlo con [homebrew](https://brew.sh/):

    ```
    brew install git
    ```

- ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

    Para Windows, tienes que instalar [git](https://git-scm.com/download/win) y git bash, aquí hay un [manual](https://phoenixnap.com/kb/how-to-install-git-windows) para la instalación.

---

## Otras Plantillas
