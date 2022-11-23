###using classes 
# n=[1,2,3,4,5,6]
# B=[{} for _ in n]

# def subseq(n):
#     max_B=0
#     if len(n)<2:
#         return len(n)
#     for i in range(len(n)):
#         for j in range(0,i):
#             cd=n[i]-n[j]
#             B[i][cd]= max(B[i].get(cd,1),B[j].get(cd,1)+1)
#             max_B= max(max_B,B[i][cd])
#     return max_B
# print(subseq(n))

###using classes 
# n=[1,2,3,4,5,6]
# B=[{} for _ in range(len(n))]
# print(B)

# def subseq(n):
#     max_B=0
#     if len(n)<2:
#         return n
#     for i in range(len(n)):
#         B[i][0]=1
#         for j in range(0,i):
#             cd=n[i]-n[j]
#             if cd not in B[j]:
#                 B[i][cd]=2
#             else:
#                 B[i][cd]=B[j][cd]+1
#         max_B= max(max_B,max(B[i].values()))
#     return max_B
# print(subseq(n))

n=input()
n=n.split()
B=[{} for _ in n]

def subseq(n):
    max_B=0
    if len(n)<2:
        return len(n)
    for i in range(len(n)):
        for j in range(0,i):
            cd=n[i]-n[j]
            B[i][cd]= max(B[i].get(cd,1),B[j].get(cd,1)+1)
            max_B= max(max_B,B[i][cd])
    return max_B
print(subseq(n))