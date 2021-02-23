import os
from pathlib import Path

def getListOfScreenshotFiles(pathToDesktop):
    # List Comprehension to get all the screenshot files
    return [file for file in os.listdir(pathToDesktop) if "screenshot" in file.lower()]
