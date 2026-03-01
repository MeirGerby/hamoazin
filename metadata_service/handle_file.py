from pathlib import Path 
from datetime import datetime 
class FileMetadata:
    """add metadata on the file based on its path"""
    def __init__(self, path: str):
        self.path: Path = Path(path) 

    def add_metadata(self) -> dict:
        """add metadata on the file and return a dict with all the information about the file"""
        name = self.path.name 
        stat = self.path.stat()
        size = stat.st_size 
        date_created = datetime.fromtimestamp(stat.st_birthtime * 1e-3) 
        date_modified = datetime.fromtimestamp(stat.st_mtime * 1e-3)
        
        
        return {
            "name": name, 
            "size": size, 
            "date_created": str(date_created), 
            "date_modified": str(date_modified) 
            }

# FILE = r"C:\Users\MEIRG\Downloads\podcasts\podcasts\download (2).wav"
# file_manager = FileMetadata(FILE)
# print(file_manager.add_metadata())
    

    