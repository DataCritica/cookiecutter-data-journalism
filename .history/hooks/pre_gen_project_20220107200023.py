import os
import re
import sys

module_regex = = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
repo_name = "{{cookiecutter.project_slug}}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

# Validate project slug
if not re.match(module_regex, repo_name):
    print(
        f"ERROR: The project slug {repo_name} is not a valid Python module name"
        "Please use _ instead of -."
    )

    # Exit to cancel project
    sys.exit(1)


print(f"{MESSAGE_COLOR}Creating '{repo_name}' at {os.getcwd()}{RESET_ALL}")