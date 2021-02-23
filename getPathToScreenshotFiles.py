import os
from pathlib import Path

# TODO: Remove dependency of 'os'-module. Only pathlib / Path

def getListOfScreenshotFiles(pathToDesktop):
    # List Comprehension to get all the screenshot files
    return [file for file in os.listdir(pathToDesktop) if "screenshot" in file.lower()]
