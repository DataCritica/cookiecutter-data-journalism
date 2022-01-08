import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

env = "{{cookiecutter.virtualenv_dir_name}}"
env_path = os.getcwd() + f"/{env}/bin/activate/python3.exe"

print(f"{MESSAGE_COLOR}Creating virtual environment...{RESET_ALL}")

subprocess.call(['virtualenv', f'{env}'])
subprocess.call(['pip3', 'install', 'ipykernel'])
subprocess.call(['python3', '-m', 'ipykernel', 'install', '--user', '--name', f'{env}'])

print(f"{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}Installing python packages...{RESET_ALL}")

# subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
subprocess.call([env_path, '-m', 'pip', 'install', '-r', 'requirements.txt'])

print(f"{MESSAGE_COLOR}Your template for data journalism using python is ready!{RESET_ALL}")