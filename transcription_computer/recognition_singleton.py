import speech_recognition as sr 

class Singleton:
    _instance = None 

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.r = sr.Recognizer()  # type: ignore
        return cls._instance 
    
    