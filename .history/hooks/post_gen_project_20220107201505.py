""" Script that runs after the project generation"""
import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

project_slug = "{{cookiecutter.project_slug}}"
env = "{{cookiecutter.virtualenv_dir_name}}"
env_path = os.getcwd() + f"/{env}/bin/pip"

if "{{cookiecutter.create_virtualenv}}" == "Yes":
    print(f"{MESSAGE_COLOR}Creating virtual environment...{RESET_ALL}")
    subprocess.call(['virtualenv', f'{env}'])
    subprocess.call(['pip3', 'install', 'ipykernel'])
    subprocess.call(['python3', '-m', 'ipykernel', 'install', '--user', '--name', f'{project_slug}_{env}'])

if "{{cookiecutter.install_packages}}" == "Yes" and "{{cookiecutter.create_virtualenv}}" == "Yes":
    print(f"{MESSAGE_COLOR}Installing python packages...{RESET_ALL}")
    subprocess.call([env_path, 'install', '-r', 'requirements.txt'])

if "{{cookiecutter.install_packages}}" == "Yes" and "{{cookiecutter.create_virtualenv}}" == "No":

print(f"{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}")
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}Your template for data journalism using python is ready!{RESET_ALL}")