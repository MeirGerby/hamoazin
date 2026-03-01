from pathlib import Path 

class FileMetadata:
    """add metadata on the file based on its path"""
    def __init__(self, path: str):
        self.path: Path = Path(path) 

    def add_metadata(self) -> dict:
        """add metadata on the file and return a dict with all the information about the file"""
        name = self.path.name 
        size = self.path.stat().st_size 
        print(name)
        print(size) 

FILE = r"C:\Users\MEIRG\Downloads\podcasts\podcasts\download (2).wav"
file_manager = FileMetadata(FILE)
file_manager.add_metadata()
    

    