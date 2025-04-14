def secondlargest(a,n_size):
    largest=ndlargest=-2147483648
    for i in range(n_size):
        if a[i]>largest:
            secondlargest=largest
            largest=a[i]
        elif a[i]>secondlargest and a[i] != largest:
            largest=a[i]
    print(secondlargest)
a=[1,2,3,4,5,6,7,8,9]
n_size=len(a)
print("Second Largest:",secondlargest(a,n_size))