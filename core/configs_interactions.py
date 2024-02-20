##
## EPITECH PROJECT, 2024
## yorn
## File description:
## library and template manager
##

from .imports import *
from .configs import *

def load_config(filepath=CONFIG_FILEPATH) -> dict:
    if not os.path.isfile(filepath):
        return {}
    try:
        with open(filepath, 'r') as f:
            return jloads(f.read())
    except:
        return {}

def save_config(data: dict, filepath=CONFIG_FILEPATH):
    with open(filepath, 'w+') as f:
        f.write(jdumps(data, indent=4)) # pdumps(data)
