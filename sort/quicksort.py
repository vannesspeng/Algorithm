# 快速排序算法
# 最优时间复杂度：O(nlogn)
# 最坏时间复杂度：O(n2)
# 稳定性：不稳定
def quick_sort_new(arr):
    if len(arr) < 2:
        return arr
    else:
        # 选取第一个元素作为基准元素
        pivot = arr[0]
        # 获取数组中小于基准元素的序列less
        less = [i for i in arr[1:] if i < pivot]
        # 获取数组中大于基准元素的序列greater
        greater = [i for i in arr[1:] if i > pivot]
        # 对序列less和greater分别使用递归来进行再次排序
        return quick_sort_new(less) + [pivot] + quick_sort_new(greater)


def quick_sort(alist, start, end):
    # 找到边界
    if start < end:
        i, j = start, end
        # 设置基准数
        base = alist[i]

        while i < j:
            while i < j and alist[j] > base:
                j = j - 1
            alist[i] = alist[j]

            while i < j and alist[i] < base:
                i = i + 1
            alist[j] = alist[i]
        alist[i] = base
        quick_sort(alist, start, i-1)
        quick_sort(alist, j+1, end)

        return alist


print(quick_sort([10, 5, 16, 1, 8, 9, 6], 0, 6))
