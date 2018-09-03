def bubble_sort(lst):
    """
    move the biggest to right
    """
    swapped = False
    lst_len = len(lst)
    for i in range(lst_len):
        for j in range(1, lst_len-i):
            if lst[j-1] > lst[j]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


def selection_sort(lst):
    lst_len = len(lst)
    for i in range(lst_len):
        min = i
        for j in range(i+1, lst_len):
            if lst[j] < lst[min]:
                min = j
        lst[min], lst[i] = lst[i], lst[min]
    return lst


def insertion_sort(lst):
    lst_len = len(lst)

    for i in range(1, lst_len):
        tmp = lst[i]
        j = i - 1
        while j >= 0 and tmp < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = tmp
    return lst


def shell_sort(lst):
    lst_len = len(lst)
    gap = lst_len // 2
    while gap > 0:
        for i in range(gap, lst_len):
            tmp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > tmp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = tmp
        gap = gap // 2

    return lst


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return _merge(left, right)


def _merge(left, right):
    l, r = 0, 0
    rv = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            rv.append(left[l])
            l += 1
        else:
            rv.append(right[r])
            r += 1
    if left:
        rv += left[l:]
    if right:
        rv += right[r:]
    return rv


def quick_sort(lst):
    lst_len = len(lst)
    if lst_len < 2:
        return lst
    base = lst[0]
    left = []
    right = []
    for i in range(1, lst_len):
        v = lst[i]
        if v >= base:
            right.append(v)
        else:
            left.append(v)
    return quick_sort(left) + [base] + quick_sort(right)


def heap_sort(lst):
    def shift_down(start, end):
        root = start
        while True:
            child = 2*root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child+1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break
    for start in range(len(lst)/2-1, -1, -1):
        shift_down(start, len(lst)-1)

    for end in range(len(lst)-1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        shift_down(0, end-1)

    return lst
