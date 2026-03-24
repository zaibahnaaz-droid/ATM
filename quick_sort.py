def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x == pivot]
    right=[x for x in arr if x > pivot]
    print(f"pivot: {pivot}, left: {left}, middle: {middle},right: {right}")
    return quick_sort(left)+middle+quick_sort(right)

num=list(map(int,input("Enter ele:").split()))
print("\n quick sort result:",quick_sort(num[:]))

        
