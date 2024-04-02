##
## EPITECH PROJECT, 2024
## yorn
## File description:
## library and template manager
##

from json import loads as jloads, dumps as jdumps

from .utils import *
from .configs import *

import os

def load_config(filepath=None) -> dict:
    if filepath is None:
        filepath = get_config_filepath()
    if filepath is None:
        filepath = CONFIG_FILEPATH
    if not os.path.isfile(filepath):
        return {}
    try:
        with open(filepath, 'r') as f:
            return jloads(f.read())
    except Exception as e:
        print(e)
        return {}

def save_config(data: dict, filepath=None):
    if filepath is None:
        filepath = get_config_filepath()
    if filepath is None:
        filepath = CONFIG_FILEPATH
    with open(filepath, 'w+') as f:
        f.write(jdumps(data, indent=4))
    # This "locking" mechanisme isn't perfect, but it kinda works :eyes:

def create_config(data: dict):
    filepath = f"./{CONFIG_FILEPATH}"
    if os.path.isfile(filepath):
        return
    with open(filepath, 'w+') as f:
        f.write(jdumps(data, indent=4))