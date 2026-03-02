"""
    len         获取列表的长度
    reverse     反转列表中的元素
    sort        对列表中的元素进行排序
"""

#len 获取列表的长度
ls1 = [0,1,2,3,4,5,6,7]

print(f"列表的长度为：{len(ls1)}")
#reverse     反转列表中的元素
ls1.reverse()
help(ls1.reverse())
print(f"列表的长度为：{ls1}")
ls1 = [0,1,2,3,4,5,6,7]
ls  = ls1[::-1]
print(f"列表的长度为：{ls}")

#sort    对列表中的元素进行排序
list1 = [0,43,6,45,89,21,100,68]
#按升序进行排序
list1.sort()
print(list1)

list1 = [0,43,6,45,89,21,100,68]
#按降序进行排序
list1.sort(reverse=True)
print(list1)
lsp = ['asdf','dhg','as']
lsp.sort(key=len)
print(lsp)



