""" Script that runs after the project generation"""
import os

MESSAGE_COLOR = '\033[92m'
RESET_ALL = "\x1b[0m"

yes_venv = "Yes - Create a virtual environment and install packages"

# Install pipenv for Linux
if "{{cookiecutter.setup_project}}" == yes_venv and "{{cookiecutter.operating_system}}" == "Linux":
    os.system("pip install pipenv")
# Install pipenv for MacOS
if "{{cookiecutter.setup_project}}" == yes_venv and "{{cookiecutter.operating_system}}" == "MacOS":
    os.system("brew install pipenv")
# Install venv for Windows
if "{{cookiecutter.setup_project}}" == yes_venv and "{{cookiecutter.operating_system}}" == "Windows":
    os.system("python -m pip install pipenv")

# Install virtual environment
if "{{cookiecutter.setup_project}}" == yes_venv:
    print(f"{MESSAGE_COLOR}Creating virtual environment...{RESET_ALL}")
    os.system("pipenv install --three")
    os.system("pipenv install pandas numpy plotly ipykernel")

# Initialize git for Linux and MacOS
if {{"cookiecutter.initialize_git"}} == "Yes" and "{{cookiecutter.operating_system}}" == "Linux" or "{{cookiecutter.operating_system}}" == "MacOS":
    print(f"{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}")
    os.system("git init && git add . && git commit -m 'Initial commit'")
# Initialize git for Windows
if {{"cookiecutter.initialize_git"}} == "Yes" and "{{cookiecutter.operating_system}}" == "Windows":
    print(f"{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}")
    os.system("git init ; git add . ; git commit -m 'Initial commit'")

# Final message
print(f"{MESSAGE_COLOR}Your template for data journalism using python is ready!{RESET_ALL}")