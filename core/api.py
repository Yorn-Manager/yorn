"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

import requests
import base64
from .configs import *
from .object import *

def getReleaseRequest(repository_name: str):
    return f"https://api.github.com/repos/{AUTHOR_NAME.lower()}/{repository_name.lower()}/releases"

def getRepositories() :
    response = requests.get(URL_ORGANISATION)
    if response.status_code == 200 :
        fieldsToExtract = ['name', 'html_url']
        return [{field: repo.get(field, '') for field in fieldsToExtract} for repo in response.json()]
    else:
        print(f"Failed to get the requested repository. Status code: {response.status_code}")
        return None


def getConfigContent(repository_name: str):
    url = f'https://api.github.com/repos/{AUTHOR_NAME.lower()}/{repository_name.lower()}/contents/.yorn.info'
    response = requests.get(url)

    if response.status_code == 200:
        file_info = response.json()
        content = base64.b64decode(file_info['content']).decode('utf-8')
        return parseYornInfo(content)
    else:
        print(f"Failed to retrieve file content. Status code: {response.status_code}")
        return None
