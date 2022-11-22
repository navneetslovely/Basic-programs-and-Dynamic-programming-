###using classes 
n=[1,2,3,4,5,6]
B=[{} for _ in range(len(n))]
max_B=1
def subseq(n):
    B[i][0]=1
    if len(n)<2:
        return n
    for i in range(len(n)):
        for j in range(0,i):
            cd=n[i]-n[j]
            if cd not in B[j]:
                
            max_B= max(max_B,B[i][cd])
    return max_B
print(subseq(n))