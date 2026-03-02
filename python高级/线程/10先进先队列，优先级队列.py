import queue

# tiH Queue put get put_nowait get_nowait isempty isfull

# 后进先出队列 Lifo Last in first out

q = queue. LifoQueue ()

q.put('a')
q.put('b')
q.put('c')
print(q.get())

# 优先级Queue
q = queue.PriorityQueue() #数字越小,优先级越高
q.put((18,'a'))
q.put((89,'b'))
q.put((-1,'d'))
q.put((36,'c'))

print(q.get())
print(q.get())