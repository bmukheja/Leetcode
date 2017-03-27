def  countPairs(k, a):
    from collections import Counter
    c = Counter(a)
    output = 0
    for item in c:
        if k-item in c and c[item]!=0:
            if item!= k/2:
                output+= c[item]*c[k-item]
                c[item],c[k-item]=0,0
            elif item == k/2 and c[item]==1:
                c[item]=0
            elif item == k/2 and c[item] > 1:
                import math
                f = math.factorial
                n = c[item]
                temp = (f(n)/f(n-2))/2
                output+= temp
                c[item]=0
    return output