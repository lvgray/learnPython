"""各种排序算法的具体实现"""


# 比较大小
def less(cmp_v, cmp_w):
    if cmp_v > cmp_w:
        return False
    else:
        return True


def bigger(cmp_v, cmp_w):
    if cmp_v > cmp_w:
        return True
    else:
        return False


# 交换2个值
def exch(comparables, i, j):
    value_1 = comparables[i]
    value_2 = comparables[j]
    comparables[i] = value_2
    comparables[j] = value_1


values = [1, 2, 34, 45, 66, 7]


# select sort 选择排序
def select_sort(comparables):
    length = len(comparables)
    for i in range(length):
        min = i
        for j in range(i + 1, length):
            if less(comparables[j], comparables[i]):
                exch(comparables, i, j)


# select_sort(values)
print(values)


# insert sort 插入排序 对 输入是有序数组来说,是个比较快速的排序算法
# 但是也逃脱不了相邻元素之间的比较
def insert_sort(comparables):
    length = len(comparables)
    for i in range(length):
        for j in range(i, 0, -1):
            if less(comparables[j], comparables[j - 1]):
                exch(comparables, j, j - 1)


insert_sort(values)
print(values)


# 希尔排序 todo
def shell_sort(comparables):
    pass
