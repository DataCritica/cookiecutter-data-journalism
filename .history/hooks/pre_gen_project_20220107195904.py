import os
import re

module_regex = = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
repo_name = "{{cookiecutter.repo_name}}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if not re.match(module_regex, repo_name):
    print(
        f"ERROR: The project slug {repo_name} is not a valid Python module name. "
        "Please do not use a - and use _ instead."
    )

    # Exit to cancel project
    sys.exit(1)


print(f"{MESSAGE_COLOR}Creating '{repo_name}' at {os.getcwd()}{RESET_ALL}")