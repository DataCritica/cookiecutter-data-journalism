import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

env_name = "{{virtualenv_dir_name}}"

print(f"{MESSAGE_COLOR}Creating virtual environment...{RESET_ALL}")

subprocess.call(['virtualenv', f'{env_name}'])

print(f"{MESSAGE_COLOR}Setting up {env_name}...{RESET_ALL}")

subprocess.call(['pip3', 'install', 'ipykernel'])
subprocess.call(['python3', 'm', 'ipykernel', 'install', '--user', '--name', f'{env_name='])

# print(f"{MESSAGE_COLOR}Almost done!")
print(f"{MESSAGE_COLOR}Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}Installing python packages...{RESET_ALL}")

subprocess.call(['source', f'{env_name=}/bin/activate'])
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

print(f"{MESSAGE_COLOR}Your template for data journalism using python is ready!{RESET_ALL}")