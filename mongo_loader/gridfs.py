from gridfs import GridFSBucket

class MongoLoader:
    def __init__(self, db, file_path, filename):
        self.db = db  
        self.file_path = file_path
        self.filename = filename 

    def send_file(self, file_id):
        """send file to mongodb by id"""
        bucket = GridFSBucket(self.db)
        with open(self.file_path, 'rb') as file_data:
            bucket.upload_from_stream_with_id(
                file_id=file_id,
                filename=self.filename, 
                source=file_data
            )
        print(f"file uploaded with fild_id {file_id}")
    