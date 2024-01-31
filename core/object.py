"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

class RepositoryInfo:
    def __init__(self, dico: dict):
        self.type = None
        self.name = None
        self.language = None
        self.description = None
        for k, v in dico.items():
            if k == "type":
                self.type = v
            elif k == "name":
                self.name = v
            elif k == "language":
                self.language = v
            elif k == "description":
                self.description = v
            else:
                print("gnegne")
                
def parseYornInfo(info_string):
    info_dict = {}
    lines = info_string.strip().split('\n')
    for line in lines:
        splitted = line.split(':', 1)
        key = splitted[0]
        value = ':'.join(splitted[1:])
        while key[0] == ' ':
            key = key[1:]
        while key[-1] == ' ':
            key = key[:-1]
        while value[0] == ' ':
            value = value[1:]
        while value[-1] == ' ':
            value = value[:-1]

        info_dict[key.lower()] = value
    return RepositoryInfo(info_dict)
