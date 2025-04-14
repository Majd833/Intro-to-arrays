def minEle(a,size):
    temp=a[0]
    for i in range (1,size):
        temp=min(temp,a[i])
    return temp
def maxEle(a,size):
    temp=a[0]
    for i in range (1,size):
        temp=max(temp,a[i])
    return temp
a=[123,675,1234,69,2]
size=len(a)
print("Max",maxEle(a,size))
print("Min",minEle(a,size))