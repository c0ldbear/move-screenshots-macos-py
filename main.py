# main.py

from getPathToUserDesktop import getPathToUserDesktop
from getPathToScreenshotFiles import getListOfScreenshotFiles
from getPathToScreenshotsDirectory import getPathToScreenshotsDirectory
from moveScreenshotFiles import moveScreenshotFiles

def main():
    # Get the absolute path to the users desktop
    pathDesktop = getPathToUserDesktop()

    # Get the path to ~/Pictures/screenshots
    pathScreenshots = getPathToScreenshotsDirectory()
    
    # Get a list of all the screenshots at ~/Desktop/
    screenshots = getListOfScreenshotFiles(pathDesktop)

    #  Move all screenshots by renaming them
    moveScreenshotFiles(pathDesktop, pathScreenshots, screenshots)

if __name__ == '__main__':
    main()
