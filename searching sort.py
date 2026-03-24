def selection_sort(arr):
    print("\n selection sorting steps:")
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index=j
            print(f"round{i+1} smallest elemente is {arr[min_index]}'swapping with {arr[i]}")
            arr[i],arr[min_index] = arr[min_index],arr[i]
            print("current list:",arr)
    return arr

num=list(map(int,input("enter num").split()))
print("\n searching sort result:",selection_sort(num[:]))
         

                        
