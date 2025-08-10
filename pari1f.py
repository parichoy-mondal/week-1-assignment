def is_Sorted_helper(arr, n):

    if (n == 0 or n == 1):
        return True

    return (arr[n - 1] >= arr[n - 2] and is_Sorted_helper(arr, n - 1))
            
def is_Sorted(arr):
    
    n = len(arr)
    
    return is_Sorted_helper(arr, n)
    
if __name__ == "__main__":
    arr = [ 10, 20, 30, 40, 50 ]

    if (is_Sorted(arr)):
       print("true")
    else:
       print("false")
