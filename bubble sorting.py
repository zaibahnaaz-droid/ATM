def bubble_sort(arr):
    print("bubble sort working steps:")
    n=len(arr)
    for i in range(n):
        print(f"\npass {i+1}:")
        for j in range(0,n-i-1):
            print(f"comparing{arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j+1]:
                print(f"->swapping {arr[j]} and {arr[j+1]}")
                arr[j],arr[j+1] = arr[j+1],arr[j]
            print("current list:",arr)
    return arr

num=list(map(int,input("enter num").split()))
print("\n bubble sort result:",bubble_sort(num[:]))
         
