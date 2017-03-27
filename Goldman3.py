
def countStepsUtil(n):
    res = [0]*n
    res[0]=1
    res[1]=1
    for i in range(2,n):
        res[i]=0
        for j in range(1,min(i+1,4)):
            res[i]+=res[i-j]
    return res[n-1]

def countSteps(n):
    if n==1: return 0
    return countStepsUtil(n+1)

print(countSteps(0))

