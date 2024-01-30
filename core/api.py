from .configs import AUTHOR_NAME

def getReleaseRequest(repository_name: str):
    return f"https://api.github.com/repos/{AUTHOR_NAME.lower()}/{repository_name.lower()}/releases"