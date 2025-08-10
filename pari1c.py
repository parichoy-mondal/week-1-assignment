def find_second_largest_sorted(arr):
    if len(arr) < 2:
        return None  
    
    arr.sort(reverse=True)  
    return arr[1]
my_list = [10, 20, 4, 45, 99]
second_largest = find_second_largest_sorted(my_list)
print(f"The second largest element is: {second_largest}") 
