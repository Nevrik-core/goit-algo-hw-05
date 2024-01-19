def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    upper_bound = arr[-1]
    iterations = 0

    if upper_bound < x:
        return (0, None)
    
    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid -1

        else:
            return (iterations, arr[mid])
        
    return (iterations, upper_bound)

if __name__ == "__main__":
    arr = [3, 4, 10, 40, 50, 60, 70, 80, 90, 100]
    x = 6

    result = binary_search(arr, x)

    if result[1] is not None:
        print(f"Element found in {result[0]} iterations, upper bound is {result[1]}")
    else:
        print("Element is not present in array")
