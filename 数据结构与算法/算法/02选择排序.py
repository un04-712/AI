"""
        选择排序的工作原理:第一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，然后再从剩余的未排序元素中寻找到最小（大）元素，然后放到已排序的序列的末尾. 以
此类推，直到全部待排序的数据元素的个数为零.

"""
# 选择排序:
# 最差时间复杂度 : O(n2)
# 最优时间复杂度 : O(n2)
# 算法稳定性 : 不稳定算法  在升序情况下去将最大值放在右边的时候相等的元素会出现次序不对情况


def select_sort(alist):
    for i in range(len(alist)-1):
        #假定一个最小元素值的下标
        min_index = i
        #判断当前值是否比最小元素值小
        for j in range(i+1,len(alist)):
            #如果最小元素值比当前最小元素值小，则将的当前元素下标给到最小元素下标
            if alist[j] < alist[min_index]:
                min_index = j
        #如果最小元素值下标发生变化，交换两个值的下标
        if min_index != i:
            alist[i],alist[min_index] = alist[min_index],alist[i]


if __name__ == '__main__':
    list1 = [2,45,8,63,7,5]
    select_sort(list1)
    print(list1)
