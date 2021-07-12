
def LSI(arr):
    print("LSI ", f"LSI({arr})")
    if len(arr) == 1:
        return 1

    temp1 = []
    for i in range(len(arr)):
        temp = []
        for j in range(i+1, len(arr)):
            # print("i ", i, "j ", j)
            # if j >= len(arr) - 1:
            #     temp.append(1)
            if arr[i] < arr[j]:
                print("I AM i ", f"[{arr[i]}]", " I AM j ", arr[j:])
                temp.append(1 + LSI(arr[j:]))
                if 1 + LSI(arr[j:]) == 4:
                    print("case1 ", f"{arr[i]} , {arr[j:]}")
            else:
                temp.append(LSI(arr[j:]))
                if LSI(arr[j:]) == 4:
                    print("case1 ", LSI(arr[j:]))
        if not temp:
            temp1.append(0)
            continue

        temp1.append(max(temp))

    print("result ", max(temp1))
    if max(temp1) == 4:
        print("temp1 ", temp1)
    return max(temp1)


arr = [4, 10, 4, 3, 8, 9]


print(LSI(arr))
