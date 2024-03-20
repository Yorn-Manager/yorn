"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

from .cli import *
from .api import *
from .utils import *
from .configs_interactions import *

import shutil

def commandBuild():
    cwd = os.getcwd()
    config_path = get_config_filepath()
    if not config_path:
        print_error(f"Could not retreive \"{CONFIG_FILEPATH}\" in the parent directories !")
        return
    os.chdir(os.path.dirname(config_path))
    if os.path.isdir(".yornlibs"):
        print_error("\".yornlibs\" directory found !\nIt will be deleted and re-generated !")
        try:
            shutil.rmtree(".yornlibs")
        except:
            print_error("Could not delete old \".yornlibs\" folder !\nAborting...")
            os.chdir(cwd)
    os.mkdir(".yornlibs")
    cfgs = load_config()
    for dep in cfgs["dependencies"]:
        
    print("function \"commandBuild\" not done.")