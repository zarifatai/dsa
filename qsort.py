import random


def qsort(ulist):
    if len(ulist) < 2:
        return ulist

    p_idx = random.randint(0, len(ulist)-1)
    pivot = ulist[p_idx]
    rlist = ulist[:p_idx] + ulist[p_idx+1:]

    less = [i for i in rlist if i <= pivot]
    greater = [i for i in rlist if i > pivot]

    return qsort(less) + [pivot] + qsort(greater)

random_list = random.sample(range(1, 3000), 50)
print("random:")
print(random_list)
print("ordered:")
print(qsort(random_list))