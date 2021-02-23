from pathlib import Path

def getPathToScreenshotsDirectory():
    return Path.joinpath(Path.home(), './Pictures/screenshots/')