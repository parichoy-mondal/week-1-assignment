def left_rotate_by_one(arr):

    if not arr:
        return

    temp = arr[0] 
    for i in range(len(arr) - 1):
        arr[i] = arr[i+1]  
    arr[len(arr) - 1] = temp  

my_array = [1, 2, 3, 4, 5]
print(f"Original array: {my_array}")
left_rotate_by_one(my_array)
print(f"Array after one left rotation: {my_array}")

