from motor.motor_asyncio import AsyncIOMotorGridFSBucket
import os 

from shared.logs.logs import Logger 
from shared.core.config import settings
from shared.db.mongodb import MongoDBSingleton


logger = Logger.get_logger()
class MongoDBHandler(MongoDBSingleton):
    def __init__(self, filename,  db:str=None, file_path=None):  # type: ignore
        self.db = db or settings.MONGO_DB
        self.file_path = file_path or settings.DATA_VOLUME
        self.filename = filename 
        self.bucket = AsyncIOMotorGridFSBucket(self.client[self.db])

    async def send_file(self, file_id):
        """send file to mongodb by id"""
        try:
            with open(self.file_path, 'rb') as file_data:
                await self.bucket.upload_from_stream_with_id(
                    file_id=file_id,
                    filename=self.filename, 
                    source=file_data
                )
            logger.info(f"file uploaded with fild_id {file_id}")
        except Exception as e:
            logger.error(e) 

    async def get_file(self, destinasion, filename):
        """get file from mongo gridfs"""
        try:
            os.makedirs(os.path.dirname(destinasion), exist_ok=True)

            with open(destinasion, 'wb') as file_stream:
                await self.bucket.download_to_stream_by_name(filename, file_stream)
                logger.info(f"file downloaded with file name: {filename}")

                file_stream.seek(0)
                content = file_stream.read()
                return content

        except Exception as e:
            logger.error(e)

            