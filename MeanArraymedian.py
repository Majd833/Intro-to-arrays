def mean(arr,arr_size):
    totalsum=0
    for i in range (0,arr_size):
        totalsum+=arr[i]
    return float(totalsum/arr_size)
def median(arr,arr_size):
    sorted(arr)
    if arr_size%2!=0:
        return float(arr[int(arr_size/2)])
    return float ((arr[int((arr_size-1)/2)]+arr[int(arr_size/2)])/2)
arr=[1,2,3,4,5,6,7,8]
arr_size=len(arr)
print("Mean",mean(arr,arr_size))
print("Median",median(arr,arr_size))