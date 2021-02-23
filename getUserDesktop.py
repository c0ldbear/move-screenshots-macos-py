from pathlib import Path

def getUserDesktop():
    return Path.joinpath(Path.home(), './Desktop/')