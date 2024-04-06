"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

from enum import Enum

from .cli import *
from .api import *
from .utils import *
from .configs_interactions import *

class CommandAddStatus(Enum):
    VERSION_ERROR = 0
    ALREADY_SET = 1
    LIB_NOT_FOUND = 2
    ALL_CLEAR = 3

    def displayError(status):
        if (status == CommandAddStatus.VERSION_ERROR):
            print_error("The library you want to add is already installed but in another version.\nTry to use the command \"update\" to update the library.")
        elif (status == CommandAddStatus.ALREADY_SET):
            print_error("The library you want to add is already installed in the same version.")
        elif (status == CommandAddStatus.LIB_NOT_FOUND):
            print_error("The library you want to add isn't an official library.")

def checkForYornConfig():
    config_filepath = get_config_filepath()
    if config_filepath != None:
        return True
    print_error(f"No \"{CONFIG_FILEPATH}\" found in this folder and parent ones. Exiting...")
    return False

def addLibraryInConfig(configs: dict, librayName, version) -> bool:
    if not librayName.count('/') in (0, 1):
        print_error(f"Library name not valid !\nAwaiting 0 or 1 '/', but got {librayName.count('/')}")
        return CommandAddStatus.LIB_NOT_FOUND
    if not "dependencies" in configs:
        configs["dependencies"] = []
    for dep in configs["dependencies"]:
        if dep.get("name") == librayName:
            if dep.get("version") == version:
                return CommandAddStatus.ALREADY_SET
            return CommandAddStatus.VERSION_ERROR
    if not repoExist((AUTHOR_NAME if librayName.count('/') != 1 else librayName.split('/')[0]), (librayName if librayName.count('/') == 0 else librayName.split('/')[1])):
        print_error("Library does not exists !\nCould not find the required library on github !")
        return CommandAddStatus.LIB_NOT_FOUND

    configs["dependencies"].append({
        "name": librayName,
        "version": version,
    })
    return CommandAddStatus.ALL_CLEAR

def commandAdd(libraryName, version):
    if not checkForYornConfig():
        return
    config = load_config()
    if (version == "-1"):
        version = get_latest_version_id(libraryName)
    status = addLibraryInConfig(config, libraryName, version)
    if (status == CommandAddStatus.ALL_CLEAR):
        save_config(config)
    else:
        CommandAddStatus.displayError(status)
