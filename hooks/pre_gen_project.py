""" Script that runs before the project generation"""
import os
import re
import sys

module_regex = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
project_slug = "{{cookiecutter.project_slug}}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

# Validate project slug
if not re.match(module_regex, project_slug):
    print(
        f"{ERROR_COLOR}ERROR: The project slug {project_slug} is not a valid Python module name"
        "Please use _ instead of -."
    )

    # Exit to cancel project
    sys.exit(1)

# Message with project's path
print(f"{MESSAGE_COLOR}Creating '{project_slug}' at {os.getcwd()}{RESET_ALL}")
