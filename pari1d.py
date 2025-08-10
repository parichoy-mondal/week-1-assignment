def move_zeros_list_comprehension(arr):
    non_zeros = [num for num in arr if num != 0]
    zeros = [num for num in arr if num == 0]
    return non_zeros + zeros

my_array = [0, 1, 9, 0, 5, 0, 4]
result = move_zeros_list_comprehension(my_array)
print(result) 
