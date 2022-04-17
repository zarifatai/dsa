from random import randint


def quick_sort(ulist):
    if len(ulist) < 2:
        return ulist

    pivot_idx = randint(0, len(ulist)-1)
    pivot_n = ulist[pivot_idx]
    rem_list = ulist[:pivot_idx] + ulist[pivot_idx+1:]

    less = [i for i in rem_list if i < pivot_n]
    greater = [i for i in rem_list if i >= pivot_n]

    return quick_sort(less) + [pivot_n] + quick_sort(greater)
