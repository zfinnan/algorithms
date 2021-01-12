# def binary_search(arr, low, high, item):  
#     if high >= low: 
#         mid = (high + low) // 2
#         if arr[mid] == item: 
#             return mid 
#         elif arr[mid] > item: 
#             return binary_search(arr, low, mid - 1, item) 
#         else: 
#             return binary_search(arr, mid + 1, high, item) 
#     else: 
#         return -1
# arr = [ 2, 3, 4, 10, 40, 50, 70 ] 
# item = 40 
# result = binary_search(arr, 0, len(arr)-1, item) 
# if result != -1: 
#     print("Element is present at index", str(result)) 
# else: 
#     print("Element is not present in array") 

def search(arr, target, lost_index = 0):
    if len(arr) == 0:
        return -1

    mid_index = len(arr) // 2
    mid_value = arr[mid_index]

    left_half = arr[:mid_index]
    right_half = arr[mid_index + 1:]

    if mid_value == target:
        return mid_index + lost_index
    elif len(arr) == 1 and mid_value != target:
        return -1
    elif mid_value < target:
        return search(right_half, target, mid_index + 1 + lost_index)
    elif mid_value > target: 
        return search(left_half, target, lost_index)

print(search([1,2,3,4,5,6,7,8,9], 4))