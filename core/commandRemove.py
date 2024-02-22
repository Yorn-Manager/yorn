"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

from .utils import *
from .configs_interactions import *

def commandRemove(libraryName):
    config_filepath = get_config_filepath()
    if config_filepath is None:
        print("\n⚠ No \".yorn.info\" exist. ⚠\n")
        return
    data = load_config(CONFIG_FILEPATH)
    if not "dependencies" in data:
        print("\n⚠ \".yorn.info\" file does not contain valid yorn configs. ⚠\n")
        return
    if not libraryName in data["dependencies"]:
        print("\n⚠ The library you want to remove doesn't exist in the \".yorn.info\". ⚠\n")
        return
    del data["dependencies"][libraryName]
    save_config(data, CONFIG_FILEPATH)
