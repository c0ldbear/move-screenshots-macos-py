import os
from pathlib import Path

from getUserDesktop import getUserDesktop
from getScreenshotFiles import getListOfScreenshotFiles

def main():
    # Get the absolute path to the users desktop
    p = Path.home()
    pathDesktop = getUserDesktop()

    # Get a list of all the screenshots at ~/Desktop/
    screenshots = getListOfScreenshotFiles(pathDesktop)

    #  Move all screenshots by renaming them
    pathScreenshots = p.joinpath(p, './Pictures/screenshots/')

    for file in screenshots:
        os.rename(p.joinpath(pathDesktop, file), p.joinpath(pathScreenshots, file))

if __name__ == '__main__':
    main()

