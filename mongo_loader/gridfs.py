from pymongo import MongoClient 
import gridfs 

class MongoLoader:
    def __init__(self, db, file_path, filename):
        self.db = db  
        self.file_path = file_path
        self.filename = filename 

    def send_file(self):
        fs = gridfs.GridFS(self.db)
        with open(self.file_path, 'rb') as file_data:
            file_id = fs.put(file_data, filename=self.filename)
        print(f"file uploaded with fild_id {file_id}")
    