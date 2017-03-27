# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    size = len(A)
    for left in range(size - 1):
        if A[left] > A[left + 1]:
            break
    if left == size - 1:
        return 0

    for right in range(size - 1, 0, -1):
        if A[right] < A[right - 1]:
            break

    max = A[left]
    min = A[right]
    for i in range(left + 1, right + 1):
        if A[i] < min:
            min = A[i]
        if A[i] > max:
            max = A[i]

    for i in range(size - 1, right, -1):
        if A[i] < max:
            right = i
            break

    for i in range(left):
        if A[i] > min:
            left = i
            break

    return (right - left + 1)

array = [1,2,0,0,0,18,19]
print(solution(array))