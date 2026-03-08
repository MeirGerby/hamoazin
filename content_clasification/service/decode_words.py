import base64 

danger_words_encoded = """
    R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlz
    cGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvb
    ixSZWZ1Z2VlcyxJQ0MsQkRT
    """ 
less_danger_words_encoded = """
    RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQY
    Wxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==
    """ 
class Decoder:
    def base64Decoder(self, encoded): 
        decoded = base64.b64decode(encoded)
        return decoded.decode('ascii')    




