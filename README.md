### [Español](README-ES.md)

---

# Cookiecutter Data Journalism 🍪
A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for data journalism projects using python

---

## Why use this template? 🚀

The bond between data and investigative journalism is growing heartily. In the era of the big data, there's an opening field to dig into the digital content and uncover new stories.

That's why although there are a lot of content for data science, we need adapted contents and tools for data journalism in order to emphasize the importance of reporting since it is not only a matter of analyzing and visualizing data but telling stories about the discoveries humanizing that data.

> ### *Develop good practices*

Working with big amounts of data can result on several pivot tables, graphics and inevitable on different versions of our code and data. So when it comes to look through our own projects, we're not sure which is the final version of our data  among files called *data_cleanned* and *data_processed*, and what is more, we don't remember if *plots_working* or *plots_new* is the code that actually works for making a plot and the list can go on. 

> ### *Make our work transparent and open source*

It's hard to explore a disorganized project and even harder to reproduce it, for that reason when we bring together structured and documented projects for data journalism, we make them easier for others to replicate and scrutinize methodological decisions that sometimes are not well captured by published stories. 

Last but not least, sharing our data driven work methods and codes can be helpful to other journalists to reuse them for their own investigation or to give accountability to our research ensuring information is reported truthfully.

> ### *Encourage an open data journalism*

In short, if we want journalists to share their work, we need to make a change on existing workflows, but that would mean and extra effort and therefore time investment, thus this template can serve as a tool, among others, to help data journalism achieve transparency.

## Contents
- [Features](#features)
- [Installation](#installation)
- [Directory Structure](#directory-structure)
- [Workflow](#workflow)
- [Python Virtual Environment](#python-virtual-environment)
- [Python Packages](#python-packages)
- [Initialize Git](#initialize-git)
- [Related Templates](#related-templates)

---

## Features

This template standardizes projects for data journalism and speeds up their creation by automating repetitive work when a new project is generated.

- Brings the scaffolding of a project with the help of a [directory structure](#directory-structure) designed around data pipelines and reporting stories.

- Improves the analysis process with established phases from a typical data journalism [workflow](#workflow).

- Automates the creation of a [virtual environment](#python-virtual-environment) in order to make an isolated and reproducible data project.

- Installs useful [python packages](#python-packages) during data analysis: pandas, numpy and plotly.

- Initializes a local [git](#initializa-git) repository for the purpose of managing a version control of the project.

- The template supports Linux, MacOS and Windows installation. 

---

## Installation 

- ### **Quickstart**

    First you need to install `cookiecutter` either it is with [pip](https://pip.pypa.io/en/stable/) or [conda](https://docs.conda.io/en/latest/).

    - Installing with `pip`:

    ```
    pip install cookiecutter
    ```

    - Installing with `conda`:

    ```
    conda config --add channels conda-forge
    conda install cookiecutter
    ```

    For more information about installing cookiecutter read the [documentation](https://cookiecutter.readthedocs.io/en/latest/installation.html).

- ### **Start a new project**

    Now install the data journalism template:

    ```
    cookiecutter https://github.com/fer-aguirre/cookiecutter-data-journalism
    ```

    [![asciicast](https://asciinema.org/a/SI22AS1HdLlgpkU28jpXoNH7p.svg)](https://asciinema.org/a/SI22AS1HdLlgpkU28jpXoNH7p)

- ### **Requirements**

    The template works with Jupyter notebooks, in case you don't have a set up for [jupyter](https://jupyter.org/), run the following command: 

    ```
    pip install jupyterlab notebook
    ```
---

## Workflow

1. Set up the project 🔧
2. Process data 🧼
3. Analyze data 🔎
4. Visualize data 📊
5. Write a report ✏️
6. Publish a story 👥

---

## Directory Structure

```
|- .gitignore              # Customized .gitignore for python projects
|- LICENSE                 # Project's license
|- README.md               # Top-level README for this project
|
|- data                    # Categorized data files                      
| |- processed             # Cleaned data
| |- raw                   # Original data
|
|- docs                    # Explanatory materials
|  |- references           # Papers, manuals, articles, etc.
|  |- reports              # Report analysis as PDF, HTML, etc.
|  |- data-dictionary.md   # Information about the data
|  |- explore-data.md      # Questions to explore the data
|
|- notebooks               # Jupyter notebooks
|  |- 0.0-process.ipynb    # Data processing (fixing column types, data cleansing, etc.)
|  |- 1.0-analyze.ipynb    # Exploratory data analysis
|  |- 2.0-visualize.ipynb  # Data visualization methods
|
|- outputs                 # Exports generated by notebooks
|   |- tables              # Generated pivot tables to analyze data
|   |- figures             # Generated graphics, maps, etc. to be used in reporting
|  
|- Pipfile                 # Project dependencies
```

- ### `.gitignore`

    The file contains a [template](https://github.com/github/gitignore/blob/main/Python.gitignore) for python projects.

- ### `LICENSE`

    Public repositories need an open source license in order to be used, modified and distributed. For this reason, with this template you can choose between a [MIT License](https://choosealicense.com/licenses/mit/) or a [GNU General Public License v3](https://choosealicense.com/licenses/gpl-3.0/).

    For more information on how to license your code, checkout this [site](https://choosealicense.com/).

- ### `README.md`

    A README is a markdown file that introduces and gives a description of the project. It includes information that is required to understand what the project is about.

    Here's a [manual](https://www.makeareadme.com/) on how to create a README file, an [article](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) on how to write markdown and a link to test an [online editor](http://editor.md.ipandao.com/en.html).

- ### `data`

    The data section contains two directories: `raw` and `processed`:

    - ### `raw`

    The original data files should remain intact and only be used for consultation purposes.

    - ### `processed`

    Everything related to data cleansing and polishing should go in this folder.

- ### `docs`

    This category consists of two directories (`references` and `reports`) and two markdown files (`data-dictionary.md` and `explore-data.md`):

    - ### `references`

        This folder contains all the documents that serve as reference for the project such as papers, articles, other journalistic publications, interviews, FOIA requests, data documentation, etc.

    - ### `reports`

        Here are the reports that account for the analysis of the data and put into words the results from the graphs and in general all the outputs generated by the code.

    - ### `data-dictionary.md`

        Information about the dataset or, in other words, metadata to put the data in context such as describing what each column refers to.

    - ### `explore-data.md`
        A template for making an exploratory analysis by treating our data as a source of information and therefore asking it questions and find out what data are telling us. At this point we also need to interrogate the context of the data, who collected them, how they were collected, for what purpose and more than that consider possible data gaps or missing voices.

        This template was inspired by [Putting data back into context](https://datajournalism.com/read/longreads/putting-data-back-into-context).

- ### `notebooks`

    This part covers jupyter notebooks divided into three categories: processing, analysis and visualization. These sections in turn may have subcategories as well, hence their nomenclature contains an enumeration to arrange them.

    - ### `0.0-process.ipynb`

        During processing we will clean the data, correct the variable types and generally perform procedures in order to make the data categories comparable.

    - ### `1.0-analyze.ipynb`

        In this stage, meaningful information is extracted from the data by grouping, filtering, comparing, calculating among many other methods in order to find patterns and relationships between categories.

    - ### `2.0-visualize.ipynb`

        After the exploratory analysis, we make visual representations of what has been discovered in the analysis, for which we can choose from a wide range of graphics to communicate this information.

- ### `outputs`

    This section is composed of two directories: `tables` and `figures`

    - ### `tables`

        This folder contains simple tables and pivot tables generated in the crosses of different variables from the dataset.

    - ### `figures`

        Here comes the graphs, diagrams, maps or other types of visualizations generated on notebooks.  

- ### `Pipfile`

    A file created when the virtual environment is generated with `pipenv`. This file lists all the packages used in the project.

---

## Python Virtual Environment

During the project generation, you'll be asked if you want to create a virtual environment, if you accept [pipenv](https://pypi.org/project/pipenv/) will be installed and create an environment for the project. It is worth mentioning that the template will initialize a **Python 3** virtual environment.

A virtual environment is a tool that separates dependencies of different projects. That means we can have isolated projects with their own packages, but on top of that it will help us to make our research reproducible since listing all the libraries necessary to reproduce an outcome should be part of our workflow.

Pipenv has several advantages in comparison to other libraries like `virtualenv` or `virtualenvwrapper`. Its main features are that you no longer need to use `pip` since it is already integrated in `pipenv` command. Likewise its `Pipfile` is much easier to use and understand than a `requirements.txt` file.

For more information about `pipenv` you can read the [documentation](https://pipenv.pypa.io/en/latest/).

---

## Python Packages
If you accept the previous option, you will also install a selection of packages for a basic data analysis in journalism.

| Library | Documentation  |
| :-: | :-: |
| ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) | [Pandas](https://pandas.pydata.org/)
| ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)  | [Numpy](https://numpy.org/doc/stable/)
| ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white) | [Plotly](https://plotly.com/python/)

Besides those packages, [IPython kernel](https://ipython.readthedocs.io/en/stable/install/kernel_install.html) will be installed too with the purpose of using a kernel with the virtual environment. 

---

## Initialize Git 

Using git is a way to be able to manage the different versions of a project and therefore have a backup of it. We can have this history on our own computer through a local repository or have it available at any time through a remote repository on servers (such as GitHub or GitLab), so that we can synchronize these repositories as we make changes to them.

In case you don't have git installed, here's a brief guide on how to download it according to your operating system.

### Installation

- ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

    Debian and Ubuntu:

    ```
    sudo apt-get update && sudo apt-get upgrade
    sudo apt-get install git
    ```

    For other Linux distributions checkout this [guide](https://git-scm.com/download/linux).

- ![MacOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)

    You can run `git` on your terminal and if you don't have it installed, it will prompt you to install it:

    ```
    git --version
    ```

    Furthermore you have a few other [options](https://git-scm.com/download/mac) like installing it with [homebrew](https://brew.sh/):

    ```
    brew install git
    ```

- ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

    For Windows, you have to install [git](https://git-scm.com/download/win) and git bash, here's a [manual](https://phoenixnap.com/kb/how-to-install-git-windows) for the installation.

---

## Related Templates

