"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

import sys

from .cli import *

typePossibily = ["library", "template", "project"]


def interactive_mode(name, type, description, language, templates):
    print("name : [" + name + "]")
    print("type : [" + type + "]")
    print("description : [" + description + "]")
    print("language : [" + language + "]")
    print("templates : [" + templates + "]")


def non_interactive_mode(name, type, description, language, templates):
    if (name == None):
        print_error("Error: Name is required.")
        sys.exit(84)

    if (not type in typePossibily):
        print_error("Error: Type not recognized.\nType must be one of the following: " + str(typePossibily))
        sys.exit(84)

    # if (templates != None and language != templates)

    {"name": name, "type": type, "language": language, "description": description}


def commandInit(name, type, description, language, templates, interactive):
    if (interactive):
        interactive_mode(name, type, description, language, templates)
    else:
        non_interactive_mode(name, type, description, language, templates)
