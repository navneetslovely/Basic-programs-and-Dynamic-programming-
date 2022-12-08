
"""merge this on with other files and use classes to code """
staircase_steps=int(input())
stptkn=0
def steps(staircase_steps):
    if staircase_steps<0:
        return 0
    if staircase_steps==0:
        return 1
    
    stptkn=steps(staircase_steps-1)+steps(staircase_steps-2)
    return stptkn 
print(steps(staircase_steps))

