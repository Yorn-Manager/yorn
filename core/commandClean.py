"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

import shutil
import sys

from .utils import *
from .cli import *

def commandClean():
    cwd = os.getcwd()
    if not get_config_filepath():
        print_error("No config found !")
        return
    os.chdir(os.path.dirname(get_config_filepath()))
    try:
        shutil.rmtree("./.yorn.build/")
    except Exception as e:
        print(f"Error while cleaning the repo : {e}")
    os.chdir(cwd)