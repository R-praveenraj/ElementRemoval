# Given an integer array A of size N. You can remove any element from the array in one operation.
# The cost of this operation is the sum of all elements in the array present before this operation.
# Find the minimum cost to remove all elements from the array.

# Input 1:
# A = [2, 1]
# Input 2:
# A = [5]

# Output 1:
# 4
# Output 2:
# 5
def removal(a):
    a.sort(reverse=True)
    b=0
    for i in range(len(a)):
        b+=a[i]*(i+1)
    return b
a=list(map(int,input().split()))
print(removal(a))