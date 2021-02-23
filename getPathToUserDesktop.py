from pathlib import Path

def getPathToUserDesktop():
    return Path.joinpath(Path.home(), './Desktop/')