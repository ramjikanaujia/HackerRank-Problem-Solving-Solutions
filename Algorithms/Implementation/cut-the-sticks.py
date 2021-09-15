
def cut_sticks(arr):
    output = []
    while (len(arr) > 0):
        cut = min(arr)
        output.append(len(arr))
        for i in range(len(arr) - 1, -1, -1):
            arr[i] = arr[i] - cut
            if arr[i] <= 0:
                arr.pop(i)
    return output

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
result = cut_sticks(arr)
for i in result:
    print (i)