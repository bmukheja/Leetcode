# coding=utf-8
#Maximum Time possible
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
from itertools import permutations

def solution(A, B, C, D):
    # write your code in Python 2.7
    nums = [A,B,C,D]
    all_perms = sorted(permutations(nums),reverse=1)
    for a,b,c,d in all_perms:
        if isValid([a,b,c,d]):
            print("%d%d:%d%d"%(a,b,c,d))
            break
    else:
        print("NOT POSSIBLE")
    return

def isValid(time):
    if time[2]<6:
        if time[0]<=2:
            if time[0]!=2 or (time[0]==2 and time[1]<4):
                return True
    return False

solution(1,8,3,2)