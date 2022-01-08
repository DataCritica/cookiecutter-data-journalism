""" Script that runs after the project generation"""
import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

project_slug = "{{cookiecutter.project_slug}}"
env_path = os.getcwd() + "/env/bin/pip"

# Install virtual environment
if "{{cookiecutter.create_virtualenv}}" == "Yes":
    print(f"{MESSAGE_COLOR}Creating virtual environment...{RESET_ALL}")
    subprocess.call(['virtualenv', 'env'])
    subprocess.call(['pip3', 'install', 'ipykernel'])
    subprocess.call(['python3', '-m', 'ipykernel', 'install', '--user', '--name', f'{project_slug}_env'])
    os.system("virtualenv env")

# Install packages from environment path
if "{{cookiecutter.install_packages}}" == "Yes" and "{{cookiecutter.create_virtualenv}}" == "Yes":
    print(f"{MESSAGE_COLOR}Installing python packages...{RESET_ALL}")
    # subprocess.call([env_path, 'install', '-r', 'requirements.txt'])
    os.system(f"{env_path} install -r requirements.txt")

# Install packages
if "{{cookiecutter.install_packages}}" == "Yes" and "{{cookiecutter.create_virtualenv}}" == "No":
    print(f"{MESSAGE_COLOR}Installing python packages...{RESET_ALL}")
    # subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
    os.system("pip install -r requirements.txt")

# Initialize git
if "{{cookiecutter.initialize_git}}" == "Yes":
    print(f"{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}")

    # subprocess.call(['git', 'init'])
    # subprocess.call(['git', 'add', '.'])
    # subprocess.call(['git', 'commit', '-m', 'Initial commit'])
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "Initial commit"')

# Final message
print(f"{MESSAGE_COLOR}Your template for data journalism using python is ready!{RESET_ALL}")