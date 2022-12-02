#program shows encapsulation concept

import random
import string

class ShortURL1:
    
    main_link="www.google.com/"

    def __init__(self):
        self.url_dict= dict()
    
    def getShortUrl(self,longUrl):
        rnum= random.randint(6,10)
        char= string.ascii_uppercase
        print(char)

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

print("*"*100)
link=ShortURL1()

s=link.getShortUrl('www.fgyhuhguer.urertu./ryugfiergf bcfvugigvgeycggrvgeg1')
print("Short URL:::  {}".format(s))
print("Long Url:::  {}".format(link.getLongUrl(s)))


class NewShortUrl(ShortURL1):

    main_link1="www.amazon.com/"

    def NewGetShortUrl(self,longUrl):
        rnum= random.randint(5,12)
        char= string.ascii_lowercase+string.digits
        shortURL=''.join(random.choice(char) for i in range(rnum))
        print(shortURL)

        if shortURL in self.url_dict:
            return self.getShortUrl(longUrl)
        else:
            self.url_dict[shortURL]= longUrl
        
        short_link=self.main_link1+shortURL
        return short_link


print("#"*100)
link=NewShortUrl()

s=link.NewGetShortUrl('www.fgyhuhguer.urertu./ryugfiergf bcfvugigvgeycggrvgeg1')
print("Short URL:::  {}".format(s))
print("Long Url:::  {}".format(link.getLongUrl(s)))