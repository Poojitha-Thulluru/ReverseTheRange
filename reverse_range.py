def get_reversed_array(num_array, start, end):
    while start < end:
        num_array[start], num_array[end] = num_array[end], num_array[start]
        start += 1
        end -= 1
    return num_array


try:
    nums_array = list(map(int, input("Enter only Integers separated by space : ").split()))
    start_index = int(input("Enter the starting index : "))
    end_index = int(input("Enter the ending index : "))
    if 0 <= start_index < len(nums_array) - 1 and start_index < end_index < len(nums_array):
        print("The reversed array is : ", get_reversed_array(nums_array, start_index, end_index))
    else:
        print("Give the ranges within the array size")
except ValueError:
    print("Invalid input. Enter Only Integers")

