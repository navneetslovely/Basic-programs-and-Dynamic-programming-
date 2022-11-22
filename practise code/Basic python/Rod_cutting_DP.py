n= int(input("Enter the lenght of the rod:  "))
# price_table={}
pri=[]
num=int(input("enter the lenght of table:   "))
for i in range(num):
    # len_pi=int(input("enter the lenght in inch:  "))
    pri_len=int(input("enter the price of the length:  "))
    # price_table[len_pi]=pri_len
    pri.append(pri_len)
# print(price_table)
# print(pri)
# n=4
# pri=[1, 5, 8, 9, 10, 17, 17, 20, 24, 30,40,50,60,89,54,45,6,5,20,58,96] #donot use this
# n=len(pri)
print("length",pri)
def cut_rod(pri,n):
    if n==0:
        return 0
    q=float('-inf')
    for i in range(1,n+1):
   
        # q_c= pri[i-1] + cut_rod(pri,n-1)
        q=max(q,pri[i-1] + cut_rod(pri,n-i))
        # if q_c>q:
        #     print("printing q_c",q_c)
        #     q=q_c
    return q
print("printing :::::  {}".format(cut_rod(pri,n)))