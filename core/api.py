##
## EPITECH PROJECT, 2024
## yorn
## File description:
## library and template manager
##

from requests import Session
from json import loads as jloads
from base64 import b64decode

from .utils import *

# Not sure we need a whole function for that, ey ?
def getReleaseRequest(repository_name: str):
    return f"https://api.github.com/repos/{AUTHOR_NAME.lower()}/{repository_name.lower()}/releases"

def repoExist(author, repo):
    return Session().get(f"https://github.com/{author}/{repo}").status_code == 200

def getRepositories(organisation = AUTHOR_NAME, fieldsToExtract=["name", "html_url"], remove_format = [{"full_name": AUTHOR_NAME + "/yorn"}]) -> list[dict]:
    """
    Return a list of repos associated with the organisation name, fetching only the fieldsToExtract fields, and removing every repo that have the remove_format atributes

    If fieldsToExtract is an empty list, it will return the entire fetched data.

    Use the remove_format atribute like that :
    ```py
        getRepositories(remove_format=[
            {
                "name": "do_not_fetch_me" # Remove each repo whose name is "do_not_fetch_me"
            },
            {
                "private": True, # Remove each repo set as private
            },
            {
                "description": None,
                "fork": False, # Remove each repo that have no description and is not a fork
            }
        ])
    ```
    """
    s = Session()
    response = s.get(URL_ORGANISATION.format(organisation))
    if response.status_code == 200:
        try:
            output = response.json()
        except:
            return []
        cleared = []
        for repo in output:
            for fltr in remove_format:
                good = False
                for k, v in fltr.items():
                    if repo.get(k) != v:
                        good = True
                if good:
                    cleared.append(repo)
        if len(fieldsToExtract):
            output = fetch_only_those_fields(repo, *fieldsToExtract)
        return output
    else:
        return [] # No need to debug here, we will check if the output of getRepositories is {}, and so, we will know the required package is void

def getConfig(repository_name: str):
    url = f"https://api.github.com/repos/{AUTHOR_NAME.lower()}/{repository_name.lower()}/contents/.yorn.info"
    s = Session()
    response = s.get(url)

    # too many ifs and we are no longer coding style x)
    # In theory, we should only return values at the last line of the function, not in any type of if or while or for...
    if response.status_code != 200:
        return {}
    try:
        file_info = response.json()
    except:
        return {}
    if not file_info.get("content"):
        return {}
    try:
        if file_info.get("encoding") == "base64":
            return jloads(b64decode(file_info['content'].replace('\n', '').encode()))
    except:
        return {}

def get_latest_version_id(lib_name: str):
    s = Session()
    response = s.get(getReleaseRequest(lib_name))
    if not response.text:
        return ""
    try:
        response.json()
    except:
        return ""
    if not len(response.json()):
        return ""
    return response[0].get("tag_name")