def LSI(arr):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            print(i, " ", j)


arr = [50, 3, 10, 7, 40]

LSI(arr)
