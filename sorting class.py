class sort():
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            merge_sort(left)
            merge_sort(right)
            i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j< len(right):
            arr[k]=right[j]
            j +=1
            k+=1
            return arr

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x == pivot]
    right=[x for x in arr if x > pivot]
    print(f"pivot: {pivot}, left: {left}, middle: {middle},right: {right}")
    return quick_sort(left)+middle+quick_sort(right)


def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index=j
            arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr


def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            print(f"comparing{arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


SORT=sort()
while True:

    print("\n-------- sorting menu-------")
    print("1. merge sort")
    print("2. quick sort")
    print("3. selection sort")
    print("4. bubble sort")
    print(" exit")


    choice= int(input("enter choice:"))

    if choice==1:
        print("sorted ele",SORT.merge_sort(arr))
    elif choice==2:
        print("sotrygfqew",SORT.quick_sort(arr))
    elif choice==3:
        print("hgd",SORT.selection_sort(arr))
    elif choice==4:
        print("hdbcx",SORT.bubble_sort(arr))
    elif choice==5:
        print("ffkhh")
        break
    else:
        print("hjgfgfv")





      
    



