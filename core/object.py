"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

class RepositoryInfo:
    def __init__(self, name, type, language, description):
        self.type = type
        self.name = name
        self.language = language
        self.description = description

def parseYornInfo(info_string):
    info_dict = {}
    lines = info_string.strip().split('\n')
    for line in lines:
        key, value = line.split(' : ', 1)
        info_dict[key.lower()] = value
    return RepositoryInfo(**info_dict)
