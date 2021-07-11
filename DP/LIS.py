def LSI(arr):
    for i in range(len(arr)):
        if i >= len(arr) - 1:
            return 1
        elif arr[i] < arr[i+1]:
            print("case1", arr[i+1:])
            return 1 + LSI(arr[i+1:])
        else:
            print("case2", arr[i+1:])
            return LSI(arr[i+1:])


arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

print(LSI(arr))
