"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

import argparse
from .configs import *

def parse_version(version):
    if version.count('.') != 2:
        raise argparse.ArgumentTypeError("Given version (\"" + version + "\") does not follow normal version format (\"{release}.{update}.{fix}\")")
    for e in version.split('.'):
        if not e.isnumeric():
            raise argparse.ArgumentTypeError("Given version (\"" + version + "\") is not made of ints !")
    return version

def parse_yorn_type(ytype):
    if not ytype.lower() in ("project", "library", "template"):
        raise argparse.ArgumentTypeError("Yorn type must be \"Project\", \"Library\" or \"Template\" !")
    return ytype.lower()

def build_parser():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command_subparser')

    parser_command_add = subparser.add_parser(
        "add",
        help="Add a library to the current project"
    )
    parser_command_add.add_argument(
        "-n", "--name",
        type=str,
        help="Name of the library to add. Non-official libraries must be prepended by \"github.com/{author_name}/\"."
    )
    parser_command_add.add_argument(
        "-v", "--version",
        type=parse_version,
        help="Version of the library to add in the format \"0.0.0\". Leave empty to use last version.",
        default="-1"
    )

    parser_command_remove = subparser.add_parser(
        "remove",
        help="Remove lib from project"
    )
    parser_command_remove.add_argument(
        "-n", "--name",
        type=str,
        help="Name of the library to remove. Non-official libraries must be prepended by \"github.com/{author_name}/\"."
    )

    parser_command_stat = subparser.add_parser(
        "stat",
        help=f"Give all the information about a library, project, template, etc. based on the \"{CONFIG_FILEPATH}\"."
    )

    parser_command_init = subparser.add_parser(
        "init",
        help=f"Initialize a project, library, template, etc. with all the required information base on the \"{CONFIG_FILEPATH}\".",
    )
    parser_command_init.add_argument(
        "-n", "--name",
        type=str,
        help="Name of the project to generate",
        default=""
    )
    parser_command_init.add_argument(
        "-t", "--type",
        type=str,
        help="Type of the project to generate",
        default=""
    )
    parser_command_init.add_argument(
        "-d", "--description",
        type=str,
        help="Description of the project to generate",
        default=""
    )
    parser_command_init.add_argument(
        "-l", "--language",
        type=str,
        help="Language used on the project",
        default=""
    )
    parser_command_init.add_argument(
        "-i", "--interactive",
        help="Use interactive mode to fill the required information",
        action='store_true',
        default=False
    )

    parser_command_update = subparser.add_parser(
        "update",
        help="Update a library of the current project"
    )
    parser_command_update.add_argument(
        "-n", "--name",
        type=str,
        help="Name of the library to update. Non-official libraries must be prepended by \"github.com/{author_name}/\"."
    )
    parser_command_update.add_argument(
        "-v", "--version",
        type=parse_version,
        help="Version of the library to update in the format \"0.0.0\". Leave empty to use last version.",
        default="-1"
    )

    parser_command_build = subparser.add_parser(
        "build",
        help="Importe all the required dependencies to build an executable of the project or a library. This command cannot been used in a template.",
    )

    parser_command_clean = subparser.add_parser(
        "clean",
        help="Remove all the compiled libraries and executables in a project.",
    )

    parser_command_install = subparser.add_parser(
        "install",
        help="Importe all the required dependencies in the current project.",
    )

    return parser