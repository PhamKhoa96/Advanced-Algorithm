"""
https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/
"""


p = [10, 20, 30, 40, 30]


def minMatrixChain1(p):
    result = 2147483648

    if len(p) == 0:
        return 0
    elif len(p) == 1:
        return p[0]
    elif len(p) == 2:
        return p[0]*p[1]
    elif len(p) == 3:
        return p[0]*p[1]*p[2]
    else:
        for i in range(1, len(p)-1):
            result = min(result, p[i-1]*p[i]*p[i+1] +
                         minMatrixChain1(p[:i] + p[i+1:]))
        return result


print(minMatrixChain1(p))
