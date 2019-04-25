def binary_search(list, item):
    # low and high 限定在列表中查找的范围.  
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        # 查找到指定项，返回下标.  
        if guess == item:
            return mid
            # 当前数值过大时，降低上限值.
        if guess > item:
            high = mid - 1
            # 当前数值过小时，提高下限值.
        else:
            low = mid + 1
            # 查找项不存在返回None
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))  # => 1
# 查找项不存在返回None.  
print(binary_search(my_list, -1))  # => None
