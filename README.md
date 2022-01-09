# Cookiecutter Data Journalism 🍪
A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for data journalism projects using python

---

## Contents
- [Features](#features)
- [Installation](#installation)
- [Directory Structure](#directory-structure)
- [Workflow](#workflow)
    - [Set up a project](#set-up-the-project)
    - [Process data](#process-data)
    - [Analyze data](#analyze-data)
    - [Visualize data](#visualize-data)
    - [Write a report](#write-a-report)
- [Python Packages](#python-packages)
- [Python Virtual Environment](#python-virtual-environment)
- [Initialize Git](#git)
- [Related Templates](#related-templates)

---

## Features

This template standardizes and speeds up the creation of a project for data journalism.

- Brings the scaffolding of a project with the help of a [directory structure](#directory-structure) designed around data pipelines.

- Improves the analysis process with established phases from a typical data [workflow](#workflow).

- Installs useful [python packages](#python-packages) during data analysis: pandas, numpy and plotly.

- Automates the creation of a [virtual environment](#python-virtual-environment) in order to make an isolated and reproducible data project.

- Initializes a local [git](#initializa-git) repository for the purpose of managing a version control of the project.

---

## Installation 

- ### **Quickstart**

    First you need to install [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) either it is with [pip](https://pip.pypa.io/en/stable/) or [conda](https://docs.conda.io/en/latest/).

    - Installing with pip:

    ```
    pip install cookiecutter
    ```

    - Installing with conda:

    ```
    conda config --add channels conda-forge
    conda install cookiecutter
    ```

- ### **Start a new project**

    Now install the data journalism template.

    ```
    cookiecutter https://github.com/fer-aguirre/cookiecutter-data-journalism
    ```
- ### **Optional**

    In addition you can install [pipenv](https://pypi.org/project/pipenv/) to create a virtual environment during the project generation.

    ```
    pip install pipenv
    ```

    The template works with notebooks, in case you don't have a set up for [jupyter](https://jupyter.org/), run the following command. 

    ```
    pip install jupyterlab notebook
    ```

---

## Workflow

1. Set up the project
2. Process data
3. Analyze data
4. Visualize data
5. Write a report

---

## Directory Structure
```
|- .gitignore              # Customized .gitignore for python projects
|- LICENSE                 # Project's license
|- README.md               # Top-level README for this project
|- requirements.txt        # Useful python packages for data journalism
|
|- data                    # Categorized data files                      
| |- processed             # Cleaned data
| |- raw                   # Original data
|
|- docs                    # Explanatory materials
|  |- references           # Papers, manuals, etc.
|  |- reports              # Report analysis as HTML, PDF, LaTeX, etc.
|  |- data-dictionary.md   # Information about the data
|
|- notebooks               # Jupyter notebooks
|  |- process.ipynb        # Data processing (fixing column types, data cleansing, etc.)
|  |- analyze.ipynb        # Exploratory data analysis
|  |- visualize.ipynb      # Data visualization methods
|
|- outputs                 # Exports generated by notebooks
|  |- tables               # Generated pivot tables to analyze data
|  |- plots                # Generated graphics to be used in reporting
|
|- env                     # Virtual python environment
```
---

## Python Packages
Install a selection of packages for a basic data analysis in journalism.

| Library | Documentation  |
| :-: | :-: |
| ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) | [Pandas](https://pandas.pydata.org/)
| ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)  | [Numpy](https://numpy.org/doc/stable/)
| ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white) | [Plotly](https://plotly.com/python/)

## Python Virtual Environment

As a feature of this project, you can create a virtual environment for your project...

![Python](https://github.com/MikeCodesDotNET/ColoredBadges/raw/master/svg/dev/languages/python.svg)

## Initialize Git 

...

Git comes by default on Linux and macOS, however if your OS is Windows, here's a [manual](https://phoenixnap.com/kb/how-to-install-git-windows) for installing git.

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

## Related templates

...