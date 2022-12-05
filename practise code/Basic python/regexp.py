



def isMatch(p,s):
    print(p,s)


    if p==s:
        return True


    if p=="*":
        return True

    if p=='' and s=='':
        return False

    if p[0]==s[0] or p[0]=='?':
        return isMatch(p[1:],s[1:])

    if p[0]=="*":
        return (isMatch(p[1:],s) or isMatch(p,s[1:]))
    
    if p[0]!= s[0]:
        return False
# print(isMatch("*","ab"))
print(isMatch('a*' , 'ba'))
# print(isMatch("*","gerdgfy"))