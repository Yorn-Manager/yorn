"""
** EPITECH PROJECT, 2024
** yorn
** File description:
** library and template manager
"""

from .cli import *
from .api import *
from .utils import *
from .configs_interactions import *
from .commandClean import commandClean

import tempfile
import requests
import zipfile
import shutil

def build_lib(libname: str, version: str):
    if not os.path.isdir("./.yorn.build/"):
        print_error("Directory .yorn.build not found !")
        return False
    author = AUTHOR_NAME
    lib = libname
    if not os.path.isfile("./.yorn.build/built_libs.json"):
        print_error("Could not find built_libs.json in .yorn.build !!")
        return False
    built = jloads(open(".yorn.build/built_libs.json", 'r'))
    for lib in built:
        if lib.get("name") == libname and lib.get("version") != version:
            print_error("Library already built, but another version !")
            return False
        elif lib.get("name") == libname:
            print("Lib already built !")
            return True
    if libname.count('/') == 1:
        author, lib = libname.split('/')
    elif libname.count('/') != 0:
        print_error("Invalid library name !")
        return False
    if not repoExist(author, lib):
        print_error("Library not found !")
        return False
    url = f"https://api.github.com/repos/{author.lower()}/{lib.lower()}/releases"
    r = requests.get(url)
    try:
        j = r.json()
    except:
        print_error("Could not retreive JSON !")
        return False
    if type(j) != list:
        print_error("Invalid JSON output !")
        return False
    current = None
    for e in j:
        if e.get("tag_name") == version:
            current = e
    if current is None:
        print_error("Could not retreive asked version !")
        return False
    if current.get("zipball_url") is None:
        print_error("Could not retreive ZIP URL !")
        return False
    output_file = tempfile.NamedTemporaryFile("wb+", delete=False)
    output_dir = tempfile.TemporaryDirectory()
    wget(current.get("zipball_url"), output_file)
    output_file.close()
    with zipfile.ZipFile(output_file.name, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    os.unlink(output_file)
    cwd = os.getcwd()
    os.chdir(output_dir)
    configs = load_config()
    if configs.get("dependencies"):
        for dep in configs.get("dependencies"):
            build_lib(dep.get("name"), dep.get("version"))
    if configs.get("build"):
        run_command(configs.get("build"))
    if configs.get("build_files"):
        for file in configs.get("build_files"):
            shutil.copy(file, os.path.join(cwd, "./.yorn.build/build/", os.path.basename(file)))
    if configs.get("export_files"):
        for file in configs.get("export_files"):
            shutil.copy(file, os.path.join(cwd, "./.yorn.build/includes/", os.path.basename(file)))
    built.append({"name": libname, "version": version})
    jdumps(built, open("./.yorn.build/built_libs.json", 'w+'))
    os.chdir(cwd)
    try:
        shutil.rmtree(output_dir)
    except:
        pass
    return configs.get("build_flags") if configs.get("build_flags") else ""

def commandBuild():
    try:
        cwd = os.getcwd()
        config_path = get_config_filepath()
        if not config_path:
            print_error(f"Could not retreive \"{CONFIG_FILEPATH}\" in the parent directories !")
            return
        os.chdir(os.path.dirname(config_path))
        if os.path.isdir(".yorn.build"):
            print_error("\".yorn.build\" directory found !\nIt will be deleted and re-generated !")
            try:
                shutil.rmtree(".yorn.build")
            except:
                print_error("Could not delete old \".yorn.build\" folder !\nAborting...")
                os.chdir(cwd)
                return
        os.mkdir("./.yorn.build/")
        os.mkdir("./.yorn.build/build/")
        os.mkdir("./.yorn.build/includes/")
        jdumps([], open("./.yorn.build/built_libs.json", 'w+'))
        cfgs = load_config()
        build_flags = ["-I./.yorn.build/includes/"]
        for dep in cfgs["dependencies"]:
            flags = build_lib(dep.get("name"), dep.get("version"))
            if flags == False:
                print_error(f"Error building {dep.get('name')}")
            else:
                build_flags.append(flags)
        print("Please make sure that you include the \"yorn.h\" file in your project")
        print("Please add the folowing flags to your main build flags, and press enter")
        print('"', " ".join(build_flags), '"', sep='')
        input()
        run_command("make") # Yeah, hardcode, dirty, but we are quite like running out of time rn
        commandClean()
    except KeyboardInterrupt:
        print_error("User stop !\nAborting...")
        os.chdir(cwd)