import shutil, os
from pathlib import Path


def main():
    p = Path.home()
    #screenshotPath = p + "/Desktop/"
    print(p)
    pnew = p.joinpath('/Users/teddy/', './Desktop/')
    print(pnew)

    # List Comprehensions
    screenshots = [file for file in os.listdir(pnew) if "screenshot" in file.lower()]
    print(screenshots)

if __name__ == '__main__':
    main()

