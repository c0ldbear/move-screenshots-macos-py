import os
from pathlib import Path

# TODO: Remove dependency of 'os'-module. Only pathlib / Path

def moveScreenshotFiles(pathDesktop, pathScreenshotDirectory, screenshots):
    for screenshot in screenshots:
        oldPath = Path.joinpath(pathDesktop, screenshot)
        newPath = Path.joinpath(pathScreenshotDirectory, screenshot)
        os.rename(oldPath, newPath)