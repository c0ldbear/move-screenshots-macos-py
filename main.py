import shutil, os
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

if __name__ == '__main__':
    main()

