# https://www.geeksforgeeks.org/count-number-of-ways-to-partition-a-set-into-k-subsets/

# S(n,k) = k*S(n-1, k) + S(n-1,k-1)

def find(n, k):
    if k > n or k == 0 or n == 0:
        return 0
    elif n == k or k == 1:
        return 1
    else:
        return k*find(n-1, k) + find(n-1, k-1)


print(find(3, 2))


def find2(n):
    temp = 0
    for k in range(n+1):
        temp = temp + find(n, k)
    return temp


print(find2(25))
