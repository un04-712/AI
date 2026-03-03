

# 最差时间复杂度: O(logn)
# 最优时间复杂度: O(1)

def binart_search(alist,item):

    # 数列长度
    n = len(alist)
    # 递归的结束条件
    if n == 0:
        return False

    # 中间值
    mid = n//2

    if item == alist[mid]:
        return True
    elif item < alist[mid]:
        return binart_search(alist[0:mid],item)
    else:
        return binart_search(alist[mid+1:],item)


if __name__ == '__main__':
    alist = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binart_search(alist,26))
