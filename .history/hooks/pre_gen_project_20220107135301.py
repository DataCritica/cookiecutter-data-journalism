import os
# import sys

project_slug = "{{ cookiecutter.project_slug }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

# print(f"{MESSAGE_COLOR}Let's do it! You're are going to create something awesome!")
print(f"{MESSAGE_COLOR}Creating '{project_slug}' at { os.getcwd() }{RESET_ALL}")