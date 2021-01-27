import shutil, os
from pathlib import Path


def main():
    p = Path.home()
    print(f"Path: {p}")

if __name__ == '__main__':
    main()