#important libraries
import random
import string 
#*************************************************************#
# take the url from the users
# full_url= input("enter your URL")

#*************************************************************#
#predefine url
#www.fgyhuhguer.urertu./ryugfiergf bcfvugigvgeycggrvgeg
full_url='www.fgyhuhguer.urertu./ryugfiergfbcfvugigvgeycggrvgeg'
#*************************************************************#
url_dict={}
def short_url(a):
    randnum= random.randint(6,10)
    # print(randnum)
    char=string.ascii_uppercase
    # print(char)

    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    
    #one line 'for loop' for compact code
     
    # sh_url= ''.join(random.choice(char) for i in range(randnum))
    
    #*************************************************************#
    
    # logic with for loop 

    sh_url= ''
    for i in range(randnum):
        sh_url= ''.join([random.choice(char),sh_url])
    print(sh_url)
    #*************************************************************#

    if sh_url in url_dict:
        return short_url(a)
    else:
        url_dict[sh_url]=full_url
    print(url_dict)
    short_link= "www.google.com/"+sh_url
    return short_link


print(short_url(full_url))