##
## EPITECH PROJECT, 2024
## yorn
## File description:
## library and template manager
##

from requests import Session
from base64 import b64encode, b64decode
from hashlib import sha256
from pickle import loads as ploads, dumps as pdumps
from json import loads as jloads, dumps as jdumps
from enum import Enum

import sys
import os