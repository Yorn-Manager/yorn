## ----------------------------------------------------------------------------------- ##
##                                                                                     ##
## EPITECH PROJECT - Tue, Feb, 2024                                                    ##
## Title           - yorn                                                              ##
## Description     -                                                                   ##
##     cli                                                                             ##
##                                                                                     ##
## ----------------------------------------------------------------------------------- ##
##                                                                                     ##
##       ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄  ▄▀▀█▀▄    ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▄▄▄▄   ▄▀▀▄ ▄▄            ##
##      ▐  ▄▀   ▐ █   █   █ █   █  █  █    █  ▐ ▐  ▄▀   ▐ █ █    ▌ █  █   ▄▀           ##
##        █▄▄▄▄▄  ▐  █▀▀▀▀  ▐   █  ▐  ▐   █       █▄▄▄▄▄  ▐ █      ▐  █▄▄▄█            ##
##        █    ▌     █          █        █        █    ▌    █         █   █            ##
##       ▄▀▄▄▄▄    ▄▀        ▄▀▀▀▀▀▄   ▄▀        ▄▀▄▄▄▄    ▄▀▄▄▄▄▀   ▄▀  ▄▀            ##
##       █    ▐   █         █       █ █          █    ▐   █     ▐   █   █              ##
##       ▐        ▐         ▐       ▐ ▐          ▐        ▐         ▐   ▐              ##
##                                                                                     ##
## ----------------------------------------------------------------------------------- ##

from rich import print
from rich.panel import Panel
from rich.align import Align
from rich.table import Table

def print_error(error, title=""):
    title = '⚠' + ((f" {title} ⚠") if (title != "") else "")
    print(Panel(Align(error, "center"), title=title, title_align="left", border_style="red"))

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

## ----------------------------------------------------------------------------------- ##
##                                                                                     ##
## MIT License                                                                         ##
## Copyright (c) 2024 Tech0ne                                                          ##
##                                                                                     ##
## Permission is hereby granted, free of charge, to any person obtaining a copy        ##
## of this software and associated documentation files (the "Software"), to deal       ##
## in the Software without restriction, including without limitation the rights        ##
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell           ##
## copies of the Software, and to permit persons to whom the Software is               ##
## furnished to do so, subject to the following conditions:                            ##
##                                                                                     ##
## The above copyright notice and this permission notice shall be included in all      ##
## copies or substantial portions of the Software.                                     ##
##                                                                                     ##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR          ##
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,            ##
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE         ##
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER              ##
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,       ##
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE       ##
## SOFTWARE.                                                                           ##
##                                                                                     ##
## ----------------------------------------------------------------------------------- ##
