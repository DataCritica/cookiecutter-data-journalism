import os
import re

module_regex = = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
repo_name = "{{cookiecutter.project_slug}}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if not re.match(module_regex, project_slug):
    print(
        f"ERROR: The project slug {MODULE_NAME} is not a valid Python module name. "
        "Please do not use a - and use _ instead."
    )

    # Exit to cancel project
    sys.exit(1)


print(f"{MESSAGE_COLOR}Creating '{project_slug}' at {os.getcwd()}{RESET_ALL}")