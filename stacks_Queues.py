stack=[]
#to push
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

stack.pop()
#print(stack)


#QUEUE

#front -->[a,b,c,d,e] <-- rear
from collections import deque

queue = deque()
#to enqueue
queue.append('a')
queue.append('b')
queue.append('c')
print(queue.popleft())