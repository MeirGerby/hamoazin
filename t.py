from shared.logs.logs import Logger 

from gridfs import GridFSBucket

logger = Logger.get_logger()
class MongoLoader:
    def __init__(self, db, file_path, filename):
        self.db = db  
        self.file_path = file_path
        self.filename = filename 
        self.bucket = GridFSBucket(self.db)

    def send_file(self, file_id):
        """send file to mongodb by id"""
        try:
            with open(self.file_path, 'rb') as file_data:
                self.bucket.upload_from_stream_with_id(
                    file_id=file_id,
                    filename=self.filename, 
                    source=file_data
                )
            logger.info(f"file uploaded with fild_id {file_id}")
        except Exception as e:
            logger.error(e)

    def get_file(self, file_stream):
        try:
            
            self.bucket.download_to_stream_by_name(self.filename, file_stream)

            logger.info(f"file downloaded with file name: {self.filename}")
        except Exception as e:
            logger.error(e)
            raise e
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db_object = client["podcasts_db"]
    
m = MongoLoader(db=db_object, 
                file_path="C:/Users/MEIRG/Downloads/podcasts_extracted/podcasts/download.wav" , 
                filename="download (1).wav")

file = 'a.wav'
with open(file, 'wb') as file:
    m.get_file(file)