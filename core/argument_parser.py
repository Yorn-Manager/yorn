"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

from .imports import *

import argparse

def parse_version(version):
    try:
        int(version) == -1
        return -1
    except:
        pass
    if version.count('.') != 2:
        raise argparse.ArgumentTypeError("Given version (\"" + version + "\") does not follow normal version format (\"{release}.{update}.{fix}\")")
    for e in version.split('.'):
        try:
            int(e)
        except:
            raise argparse.ArgumentTypeError("Given version (\"" + version + "\") is not made of ints !")
    return version

def build_parser():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command_subparser')
    parser_command_add = subparser.add_parser("add", help="Add a library to the current project")
    parser_command_add.add_argument("name", type=str, help="Name of the library to add. Non-official libraries must be prepended by \"github.com/{author_name}/\".")
    parser_command_add.add_argument("version", type=parse_version, help="Version of the library to add. Use \"-1\" (or leave empty) to use last version.", default=-1)

    parser_command_remove = subparser.add_parser("remove", help="Remove lib from project")
    parser_command_remove.add_argument("name", type=str, help="Name of the library to remove. Non-official libraries must be prepended by \"github.com/{author_name}/\".")

    

    return parser