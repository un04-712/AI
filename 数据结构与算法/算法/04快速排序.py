"""
        快速排序:基本思想是通过一趟排序将要排序的数据分割成独立的两部分，
        一般以要排序第一个元素为基准，
        其中一部分的所有数据都比另外一部分的所有数据都要小，
        然后再按此方法对这两部分数据分别进行快速排序，
        整个排序过程可以递归进行，以此达到整个数据变成有序序列。

"""


def quick_sort(alist):
    #终止递归的条件
    if len(alist)<=1:
        return alist

    #选择基准值
    pivot = alist[0]
    left = []
    mid = []
    right = []
    for i in alist:
        if i<pivot:
            left.append(i)
        elif i==pivot:
            mid.append(i)
        else:
            right.append(i)
    return quick_sort(left) + mid + quick_sort(right)


if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    print(quick_sort(alist))






