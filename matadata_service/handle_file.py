from pathlib import Path 

class FileMatadata:
    """add metadata on the file based on its path"""
    def __init__(self, path: str):
        self.path: Path = Path(path)

    