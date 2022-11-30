import random
import string 


#www.fgyhuhguer.urertu./ryugfiergf bcfvugigvgeycggrvgeg
# full_url= input("enter your URL")
full_url='www.fgyhuhguer.urertu./ryugfiergf bcfvugigvgeycggrvgeg'
url_dict={}
def short_url(a):
    randnum= random.randint(6,10)
    # print(randnum)
    char=string.ascii_uppercase
    # print(char)
    # sh_url= ''.join(random.choice(char) for i in range(randnum))
    sh_url= ''
    for i in range(randnum):
        sh_url= ''.join([random.choice(char),sh_url])
    print(sh_url)

    if sh_url in url_dict:
        return short_url(a)
    else:
        url_dict[sh_url]=full_url
    print(url_dict)
    short_link= "www.google.com/"+sh_url
    return short_link


print(short_url(full_url))