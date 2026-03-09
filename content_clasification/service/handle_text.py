from .decode_words import danger_words_encoded, less_danger_words_encoded, Decoder
from shared.logs.logs import Logger 

logger = Logger.get_logger()

class HandleText:
    def __init__(self, decoder: Decoder):
        self.all_text = {}
        self._most_danger = decoder.base64Decoder(danger_words_encoded)
        self._less_danger = decoder.base64Decoder(less_danger_words_encoded)

    def _clean_text(self, text: str) -> list:
        """return list of one's words from row text"""   
        l =  [i for i in text.split(',') if " " not in i]
        logger.info(f"create list of words from the text, excluding the coupled words.\n   list: {l}.")
        return l

    def _coupled_words(self, text: str) -> list:
        """return coupled words from row text"""
        l = [i for i in text.split(',') if " " in i]
        logger.info(f"create list of coupled words from the text, excluding the single words.\n   list: {l}.")
        return l

    def get_words(self) -> dict:
        """containerized the lists of text into a dict"""
        danger_words = self._clean_text(self._most_danger)
        danger_coupled_words = self._coupled_words(self._most_danger)
        less_danger_words = self._clean_text(self._less_danger)
        less_danger_coupled_words = self._coupled_words(self._less_danger)
        return self._to_dict(danger_words, danger_coupled_words, less_danger_words, less_danger_coupled_words)
    
    def _to_dict(self, danger_words: list, danger_coupled_words: list, 
                 less_danger_words: list, less_danger_coupled_words: list
                ):
        # single words 
        self.all_text['danger_words'] = danger_words 
        self.all_text['less_danger_words'] = less_danger_words
        # coupled words
        self.all_text['danger_coupled_words'] = danger_coupled_words 
        self.all_text['less_danger_coupled_words'] = less_danger_coupled_words 

        logger.info("create a dict contains all the list of words.")
        return self.all_text
        
