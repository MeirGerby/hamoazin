from motor.motor_asyncio import AsyncIOMotorGridFSBucket
import os 

from shared.logs.logs import Logger 

logger = Logger.get_logger()

class MongoDB:
    def __init__(self, db):
        self.db = db  
        # self.filename = filename 
        self.bucket = AsyncIOMotorGridFSBucket(self.db)

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


