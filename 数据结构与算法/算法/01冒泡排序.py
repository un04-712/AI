"""
        冒泡排序: 依次比较两个相邻的元素，如果顺序（如从大到小、首字母从从Z到A）错误就把他们交换过来。
        走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素列已经排序完成
        这个算法的名字由来是因为越大的元素会经由交换慢慢“浮”到数列的顶端（升序或降序排列），就如同碳酸饮料中二氧化碳的气泡最终会上浮到顶端一样，故名“冒泡排序”
"""
# 冒泡排序:
# 最差时间复杂度 : O(n^2)
# 最优时间复杂度 : O(n)
# 算法稳定性 : 稳定算法（两数相等时并没有发生交换）


def bubble_sort(alist):
    #如果没有交换的情况,则说明排序完成,循环结束
    for i in range(len(alist)-1):  #控制比较轮数
        flag = False
        for j in range(len(alist)-1-i): #控制比较次数
            if alist[j] > alist[j+1]:
                flag = True
                alist[j],alist[j+1] = alist[j+1],alist[j]
        if not flag:
            break

if __name__ == '__main__':
    list1 = [51,21,69,78,32,15]
    bubble_sort(list1)
    print(list1)
