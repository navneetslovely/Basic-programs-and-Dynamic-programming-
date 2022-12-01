import random
import string


class ShortURL:
    


    def __init__(self):
        self.url_dict= dict()

    def getShortUrl(self, longUrl):
        rnum= random.randint(6,10)
        char= string.ascii_uppercase
        print(char)

        # shortURL =''
        # for i in range(rnum):
        #     shortURL=''.join([random.choice(char),shortURL])
        shortURL =''.join(random.choice(char) for i in range(rnum))
        print(shortURL)

        if shortURL in self.url_dict:
            return self.getShortUrl(longUrl)
        else:
            self.url_dict[shortURL]= longUrl

        short_link="www.google.com/"+shortURL
        return short_link

    def getLongUrl(self,shortURL):
        long_link=shortURL[16:]
        print(self.url_dict)
        if long_link in self.url_dict:
            return self.url_dict[long_link]
        # else:
        #     return  None

link=ShortURL()

s=link.getShortUrl('www.fgyhuhguer.urertu./ryugfiergf bcfvugigvgeycggrvgeg1')
print(s)
print(link.getLongUrl(s))

# print(link.url_dict)