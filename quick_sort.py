"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def pivot_through(array):
    array_length = len(array)
    pivot_index = array_length - 1
    check_index = 0
    #pivot through entire array
    while check_index < pivot_index:
        pivot_value = array[pivot_index]
        check_value = array[check_index]
        if check_value > pivot_value:
            displaced_value = array[(pivot_index - 1)]
            array[check_index] = displaced_value
            array[(pivot_index - 1)] = pivot_value
            array[pivot_index] = check_value
            pivot_index -= 1
        else:
            check_index += 1
    return array, pivot_index

def quicksort(array):
    array_length = len(array)
    pivot_index = array_length - 1
    array, pivot_index = pivot_through(array)
    left_half = array[0:pivot_index]
    if len(left_half) > 1:
        left_half = quicksort(array[0:pivot_index])
    right_half = array[pivot_index:]
    if len(right_half) > 1:
        right_half = quicksort(array[pivot_index:])
    array = left_half+right_half            
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))