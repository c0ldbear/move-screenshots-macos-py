import os
from pathlib import Path

from getPathToUserDesktop import getPathToUserDesktop
from getPathToScreenshotFiles import getListOfScreenshotFiles
from getPathToScreenshotsDirectory import getPathToScreenshotsDirectory

def main():
    # Get the absolute path to the users desktop
    p = Path.home()
    pathDesktop = getPathToUserDesktop()

    # Get a list of all the screenshots at ~/Desktop/
    screenshots = getListOfScreenshotFiles(pathDesktop)

    # Get the path to ~/Pictures/screenshots
    pathScreenshots = getPathToScreenshotsDirectory()

    #  Move all screenshots by renaming them
    for file in screenshots:
        os.rename(p.joinpath(pathDesktop, file), p.joinpath(pathScreenshots, file))

if __name__ == '__main__':
    main()

