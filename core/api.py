"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

import requests
from .configs import *

def getReleaseRequest(repository_name: str):
    return f"https://api.github.com/repos/{AUTHOR_NAME.lower()}/{repository_name.lower()}/releases"

def getRepositories() :
    response = requests.get(URL_ORGANISATION)
    fieldsToExtract = ['name', 'html_url']
    return [{field: repo.get(field, '') for field in fieldsToExtract} for repo in response.json()]
