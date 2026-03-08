import base64 

class Decoder:
    def base64Decoder(self, encoded): 
        decoded = base64.b64decode(encoded)
        return decoded.decode('ascii')    

decoder = Decoder()

danger_words_encoded = """
    R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlz
    cGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvb
    ixSZWZ1Z2VlcyxJQ0MsQkRT
    """ 
less_danger_words_encoded = """
    RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQY
    Wxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==
    """ 

most_danger_words = decoder.base64Decoder(danger_words_encoded)
less_danger_words = decoder.base64Decoder(less_danger_words_encoded)



