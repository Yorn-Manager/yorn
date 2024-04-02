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

from rich.live import Live

from queue import Queue, Empty
from threading import Thread

import subprocess
import requests
import shlex
import os

def wget(url: str, file):
    p = Panel("", border_style="blue", title="[white]Downloading...", title_align="left")
    response = requests.get(url, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None:
        file.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        with Live(p, refresh_per_second=20):
            for data in response.iter_content(chunk_size=4096):
                tsize, _ = os.get_terminal_size()
                tsize -= 6
                dl += len(data)
                file.write(data)
                done = int(tsize * dl / total_length)
                p.renderable = Align(f"[{'=' * done}{' ' * (tsize - done)}]", "center")

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

def fill_in_queue(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

def run_command(command):
    p = Panel("", border_style="red", title="[white]"+command, title_align="left")
    scommand = shlex.split(command)
    process = subprocess.Popen(scommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    q = Queue()
    Thread(target=fill_in_queue, args=(process.stdout, q), daemon=True).start()
    Thread(target=fill_in_queue, args=(process.stderr, q), daemon=True).start()
    with Live(p, refresh_per_second=20):
        while process.poll() is None:
            try:
                p.renderable += q.get_nowait().decode()
            except Empty:
                pass

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
