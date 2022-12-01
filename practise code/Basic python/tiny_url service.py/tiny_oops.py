import random
import string


class ShortURL:
    


    def __init__(self):
        self.d= dict()

    def getShortUrl(self, longUrl):
        rnum= random.randint(6,10)
        char= string.ascii_uppercase
        print(char)

        shortURL =''
        for i in range(rnum):
            shortURL=''.join([random.choice(char),shortURL])