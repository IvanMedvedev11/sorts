import random
def bubble_sort(unsorted):
    unordered = True
    n = len(unsorted)
    while unordered:
        unordered = False
        for i in range(1, n):
            if unsorted[i-1] > unsorted[i]:
                unordered = True
                unsorted[i-1], unsorted[i] = unsorted[i], unsorted[i-1]
        n -= 1
    return unsorted
def local_maximum_counter(list_):
    cnt = 0
    for i in range(1, len(list_) - 1):
        if list_[i-1] < list_[i] > list_[i + 1]:
            cnt += 1
    if list_[0] > list_[1]:
        cnt += 1
    if list_[-1] > list_[-2]:
        cnt += 1
    return cnt
m = int(input("Введите длину списка: "))
random_list = [random.randint(0, 1000) for i in range(m)]
loc_m_cnt = local_maximum_counter(random_list)
print(random_list)
sorted_list = bubble_sort(random_list)
print(sorted_list)
print(sorted_list[-2])
print(sorted_list[-3])
print(loc_m_cnt)
