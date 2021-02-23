import os
from pathlib import Path

def main():
    # Get the absolute path to the users desktop
    p = Path.home()
    pathDesktop = p.joinpath(p, './Desktop/')

    # List Comprehensions to get all the screenshots
    screenshots = [file for file in os.listdir(pathDesktop) if "screenshot" in file.lower()]

    #  Move all screenshots by renaming them
    pathScreenshots = p.joinpath(p, './Pictures/screenshots/')
    for file in screenshots:
        os.rename(p.joinpath(pathDesktop, file), p.joinpath(pathScreenshots, file))

if __name__ == '__main__':
    main()

