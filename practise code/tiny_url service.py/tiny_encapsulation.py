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

given_link= input("Enter your link which you want to short")

print("*"*100)
link=ShortURL1()
s1=link.getShortUrl(given_link)
print("Short URL:::  {}".format(s1))
print("Long Url:::  {}".format(link.getLongUrl(s1)))

print("#"*100)
link1=NewShortUrl()
s2=link1.NewGetShortUrl(given_link)
print("Short URL:::  {}".format(s2))
print("Long Url:::  {}".format(link1.getLongUrl(s2)))