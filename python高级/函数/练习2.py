def demo(s):
    bigger=[ ]
    smaller=[ ]
    for i in s:
        if i%2==0:
            smaller.append( i )
        else:
            bigger.append( i )
    dic={"k2":smaller,"k1":bigger}
    print(dic)
lst=[11,22,33,44,55,66,77,88,99,90]
demo(lst)


def fun(a,*num):
    print(a,num)
fun(1,2,3,4)
def func(a):
  sum1 =0
  for k in range(3):
    sum1=sum1+a[k][2]
  return sum1
obj= func ([[1,2,3],[4,5,6],[7,8,9]])
print(obj)
