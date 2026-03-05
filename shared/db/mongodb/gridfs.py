from shared.logs.logs import Logger 

from gridfs import GridFSBucket

logger = Logger.get_logger()
class MongoLoader:
    def __init__(self):
        self.db = None 
        self.file_path = None
        self.filename = None 
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
            logger.info(f"file downloaded with fild_id {file_id}")
        except Exception as e:
            logger.error(e)

    def get_file(self, destinasion):
        try:
            file = self.bucket.download_to_stream_by_name(self.filename, destinasion)
            logger.info(f"file uploaded with file name: {self.filename}")
            return file
        except Exception as e:
            logger.error(e)