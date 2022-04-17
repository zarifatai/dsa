def find_smallest(arr):
    smallest_n = arr[0]
    smallest_idx = 0
    for idx, n in enumerate(arr):
        if n < smallest_n:
            smallest_n = n
            smallest_idx = idx
    return smallest_idx 

def selection_sort(arr):
    sorted_list = []
    for i in range(len(arr)):
        smallest_idx = find_smallest(arr)
        sorted_list.append(arr.pop(smallest_idx))
    return sorted_list

