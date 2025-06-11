arr = [1, 2, 33, 4, 11, 100, 100, 4, 2, 103, 100, 22, 33]
arr.sort(reverse = True)
for i in range(0, len(arr)):
    if arr[i] != arr[0]:
        print("runner up score is:", arr[i])
        break