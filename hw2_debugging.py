"""
A simple implementation of the merge sort algorithm.

This module provides a recursive merge sort function, `mergeSort`, which splits and sorts arrays. 
It includes a helper function, `recombine`, for merging two sorted arrays. The sort assumes elements 
are comparable by default comparison operators.

Functions:
- mergeSort(arr): Recursively sorts an array.
- recombine(leftArr, rightArr): Merges two sorted arrays into one.

No external dependencies are required.
"""
import rand


def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.

    Parameters:
    arr (list): The list of elements (either integers or floats) to be sorted.

    Returns:
    list: A new list containing all elements from the original array, sorted in ascending order.

    """
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merge two sorted arrays into a single sorted array.

    This function takes two sorted arrays `leftArr` and `rightArr` as input and combines them
    into a single sorted array. The function assumes that both input arrays are already sorted
    and performs the merge operation using a two-pointer technique, where each pointer tracks
    the current position in each of the input arrays. The function continues to compare elements
    from each array and appends the smaller element to the resulting merged array. This process
    repeats until all elements from both arrays are included in the result.

    Parameters:
    leftArr (list): The first sorted array.
    rightArr (list): The second sorted array.

    Returns:
    list: A new list containing all elements sorted in ascending order.
    """
    left_index = 0
    right_index = 0
    current_index=0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[current_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[current_index] = right_arr[right_index]
            right_index += 1
        current_index+=1

    for i in range(right_index, len(right_arr)):
        merge_arr[current_index] = right_arr[i]
        current_index+=1

    for i in range(left_index, len(left_arr)):
        merge_arr[current_index] = left_arr[i]
        current_index+=1

    return merge_arr


arr_input = rand.random_array([None] * 20)
print ("Input: ",arr_input)
arr_out = merge_sort(arr_input)

print("Output: ",arr_out)
