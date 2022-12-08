import random
import string

#commeted remaining 






class ShortURL1:
    #class varibles shared by all the objects in the class

    main_link="www.google.com/"
    
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

        short_link=self.main_link+shortURL
        return short_link

    def getLongUrl(self,shortURL):
        long_link=shortURL[15:]
        print(long_link)
        if long_link in self.url_dict:
            return self.url_dict[long_link]
        else:
            return  None

link=ShortURL1()

s=link.getShortUrl('www.fgyhuhguer.urertu./ryugfiergf bcfvugigvgeycggrvgeg1')
print("Short URL:::  {}".format(s))
print("Long Url:::  {}".format(link.getLongUrl(s)))
