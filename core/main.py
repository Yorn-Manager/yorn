"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

from . import *

def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command_subparser == "add":
        commandAdd(args.name, args.version)
    elif args.command_subparser == "remove":
        commandRemove(args.name)
    elif args.command_subparser == "stat":
        commandStat()
    elif args.command_subparser == "init":
        commandInit(args.name, args.type, args.description, args.language, args.interactive)
    elif args.command_subparser == "build":
        commandBuild()