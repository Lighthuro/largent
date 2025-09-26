import time


class Crypto:
    name:str
    value:float

    def __init__(self, crypto_name:str, crypto_value:str):
        self.name=crypto_name
        self.value=float(crypto_value.replace('$','').replace(',',''))
        self.time=current_timestamp = time.time()
        
    def increase_rate_percent(self, crypto)->float:
        rate:float=float((self.name/crypto.name)-1)
        return rate