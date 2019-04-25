# 最优时间复杂度：O(n2)
# 最坏时间复杂度：O(n2)
# 稳定性：不稳定（考虑升序每次选择最大的情况

def select_sort(alist):
    n = len(alist)
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist

alist = [54,226,93,17,77,31,44,55,20]
if "__main__" == __name__:
    print(select_sort(alist))

