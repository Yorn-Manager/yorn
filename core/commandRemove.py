"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

from .cli import *
from .utils import *
from .configs_interactions import *

def commandRemove(libraryName):
    config_filepath = get_config_filepath()
    if config_filepath is None:
        print_error(f"No \"{CONFIG_FILEPATH}\" found.")
        return
    data = load_config(CONFIG_FILEPATH)
    if not "dependencies" in data:
        print_error(f"\"{CONFIG_FILEPATH}\" file does not contain valid yorn configs.")
        return
    if not libraryName in data["dependencies"]:
        print_error(f"The library you want to remove doesn't exist in the \"{CONFIG_FILEPATH}\".")
        return
    del data["dependencies"][libraryName]
    save_config(data, CONFIG_FILEPATH)
