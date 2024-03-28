"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

import sys

from rich.prompt import Confirm
from .cli import *

languagePossibility = ["C", "C++"]
typePossibility = ["library", "project"]


def interactive_mode(name, type, description, language):
    while True:
        response = ""
        question = ""
        if name != None and name != "":
            question = f"Enter name (default value : \"{name}\"): "
        else:
            question = f"Enter name: "
        response = input(question)
        if response != "":
            name = response
            break
        print_error("Invalid input, name cannot be empty")
        print("")
        if not Confirm.ask("Continue", default=True):
            sys.exit(84)

    while True:
        response = ""
        question = ""
        if type != None and type != "":
            question = f"Enter type (default value : \"{type}\"): "
        else:
            question = f"Enter type: "
        response = input(question)
        if response in typePossibility:
            type = response
            break
        print_error("Error: Type not recognized.\nType must be one of the following: " + str(typePossibility))
        print("")
        if not Confirm.ask("Continue", default=True):
            sys.exit(84)

    while True:
        question = ""
        if description != None and description != "":
            question = f"Enter description (default value : \"{description}\"): "
        else:
            question = f"Enter description: "
        description = input(question)
        break

    while True:
        response = ""
        question = ""
        if language != None and language != "":
            question = f"Enter language (default value : \"{language}\"): "
        else:
            question = f"Enter language: "
        response = input(question)
        if response in languagePossibility:
            language = response
            break
        print_error("Error: Language not recognized.\nLanguage must be one of the following: " + str(languagePossibility))
        print("")
        if not Confirm.ask("Continue", default=True):
            sys.exit(84)

    values = {"name": name, "type": type, "description": description, "language": language}
    print(values)
    return values


def non_interactive_mode(name, type, description, language):
    if (name == None):
        print_error("Error: Name is required.")
        sys.exit(84)

    if (not type in typePossibility):
        print_error("Error: Type not recognized.\nType must be one of the following: " + str(typePossibility))
        sys.exit(84)

    if (not language in languagePossibility):
        print_error("Error: Language not recognized.\nLanguage must be one of the following: " + str(languagePossibility))
        sys.exit(84)

    values = {"name": name, "type": type, "description": description, "language": language}
    print(values)
    return values


def commandInit(name, type, description, language, interactive):
    if (interactive):
        interactive_mode(name, type, description, language)
    else:
        non_interactive_mode(name, type, description, language)
