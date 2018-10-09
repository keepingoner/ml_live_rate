








def qsort(list,low,high):
    if low >= high:
        return
    first=low
    last=high
    key=list[first]


    while last>first:

        while last>first and list[last] >= key:
            last-=1
        list[first]=list[last]
        while last>first and list[first] <= key:
            first+=1
        list[last]=list[first]
    list[first]=key
#这两行利用递归完成两个分区的排序
    qsort(list,low,first-1)
    qsort(list,first+1,high)
#以下是调用快速排序方法





def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)



array = [4, 6, 1, 25, 43, 53, 8, 10]

quick_sort(array, 0, len(array))