import shutil, os
from pathlib import Path


def main():
    p = Path.home()
    #screenshotPath = p + "/Desktop/"
    print(p)
    pnew = p.joinpath('/Users/teddy/', './Desktop/')
    print(pnew)
    for filenames in os.listdir(pnew):
        print(filenames)


if __name__ == '__main__':
    main()

