"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

from .utils import *
from .configs_interactions import *

from rich import print
from rich.table import Table

def print_dict(dico: dict):
    max_len = max([len(x) for x in dico.keys()])
    print()

def table_from_dict_or_list(lst, level=0):
    if lst == []:
        return "[]"
    elif lst == {}:
        return "{}"
    if level != 0:
        t = Table(
            show_lines=True,
            expand=False,
            show_header=True,
            border_style="bold"
        )
        if type(lst) == dict:
            t.add_column("Key")
        t.add_column("Value")
    else:
        t = Table(
            show_lines=True,
            show_header=True,
            title="Current {}stats".format(lst.get("type") + ' ' if (type(lst) == dict and lst.get("type")) else ""),
            border_style="green"
        )
        if type(lst) == dict:
            t.add_column("Name")
        t.add_column(str(lst.get("name")))
    if type(lst) == list:
        for e in lst:
            if type(e) in (dict, list):
                t.add_row(table_from_dict_or_list(e, level=level + 1))
            else:
                t.add_row(e)
    else:
        for k, v in lst.items():
            if type(k) == str and k[0] == "_":
                continue
            if type(k) == str and level == 0 and k == "name":
                continue
            if type(v) in (dict, list):
                t.add_row(k, table_from_dict_or_list(v, level=level + 1))
            else:
                t.add_row(k, v)
    return t

def commandStat():
    config_filepath = get_config_filepath()
    if config_filepath is None:
        print("\n⚠ No \".yorn.info\" exist. ⚠\n")
        return
    data = load_config(CONFIG_FILEPATH)
    t = table_from_dict_or_list(data)
    
    print(t)