import speech_recognition as sr

from shared.logs.logs import Logger 

logger = Logger.get_logger()
class Singleton:
    _instance = None 

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.r = sr.Recognizer()  # type: ignore
        return cls._instance 
    

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




