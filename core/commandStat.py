"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

from .cli import *
from .utils import *
from .configs_interactions import *

def commandStat():
    config_filepath = get_config_filepath()
    if config_filepath is None:
        print_error("No \".yorn.info\" exist.")
        return
    data = load_config(CONFIG_FILEPATH)
    t = table_from_dict_or_list(data)
    
    print(t)