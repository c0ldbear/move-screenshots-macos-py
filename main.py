import os
from pathlib import Path


def main():
    p = Path.home()
    #screenshotPath = p + "/Desktop/"
    print(p)
    pathDesktop = p.joinpath(p, './Desktop/')
    print(pathDesktop)

    # List Comprehensions
    screenshots = [file for file in os.listdir(pathDesktop) if "screenshot" in file.lower()]
    print(screenshots)

    # TODO: Move the found files to /Users/teddy/Pictures/screenshots
    pathScreenshots = p.joinpath(p, './Pictures/screenshots/')
    print(pathScreenshots)
    for file in screenshots:
        os.rename(p.joinpath(pathDesktop, file), p.joinpath(pathScreenshots, file))

if __name__ == '__main__':
    main()

