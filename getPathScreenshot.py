from pathlib import Path

def getScreenshotPath():
    return Path.joinpath(Path.home(), './Pictures/screenshots/')