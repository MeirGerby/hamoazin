import speech_recognition as sr

from shared.logs.logs import Logger 
from .recognition_singleton import Singleton  

logger = Logger.get_logger()

class SpeechManager(Singleton):
    def recognition_from_file(self, path):
        """convert the audio file to text"""
        try:
            with sr.AudioFile(path) as source:
                audio = self.r.record(source)     # type: ignore
            logger.info("convert the audio to text")
            return self.r.recognize_google(audio)     # type: ignore
        except Exception as e:
            logger.error(f"Exception {str(e)}")
            return f"Exception: {str(e)}"



# speech_manager = SpeechManager()
# file =  r"C:\Users\MEIRG\Downloads\podcasts_extracted\podcasts\download (2).wav"
# text = speech_manager.recognition_from_file(file)
# print(text)




