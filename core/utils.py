##
## EPITECH PROJECT, 2024
## yorn
## File description:
## library and template manager
##

from .configs import *
import os

# def hash_data(data: bytes) -> bytes:
#     """
#     Return hashed data (sha256).

#     Uses digest (not hexdigest), so you might want to b64 the output if it is for the user to see
#     """
#     return sha256(data).digest()

def fetch_only_those_fields(array: list[dict], *values) -> list[dict]:
    """
    Return a list of dictionaries with only the asked fields, set to null if they were not present, and theire value otherwise

    Note that *values require you to put fields on the function like that :

    ```py
    fetch_only_those_fields(dico, field1, field2, field3...)
    ```

    Kind of a va_list, ey
    """
    final = []
    for element in array:
        final.append({k: None for k in values})
        for k, v in element.items():
            if k in element.keys():
                final[-1][k] = v
    return final

def get_config_filepath():
    path = os.getcwd()
    while os.path.dirname(path) != path:
        if CONFIG_FILEPATH in os.listdir(path):
            return os.path.join(path, CONFIG_FILEPATH)
        path = os.path.dirname(path)
    if CONFIG_FILEPATH in os.listdir(path):
        return os.path.join(path, CONFIG_FILEPATH)
    return None