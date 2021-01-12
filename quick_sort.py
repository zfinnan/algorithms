def quick_sort(arr):
    elements = len(arr)
    if elements < 2:
        return arr
    current_position = 0 
    for i in range(1, elements): 
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp
    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp
    left = quick_sort(arr[0:current_position]) 
    right = quick_sort(arr[current_position+1:elements]) 
    arr = left + [arr[current_position]] + right
    return arr
array_to_be_sorted = [4,2,7,3,1,6]
print("unsorted array: ", array_to_be_sorted)
print("sorted array: ", quick_sort(array_to_be_sorted))