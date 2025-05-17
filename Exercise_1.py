# Time Complexity:
#   push(): O(1)
#   pop(): O(1)
#   peek(): O(1)
#   isEmpty(): O(1)
#   size(): O(1)
#   show(): O(n), where n is the number of elements in the stack
#
# Space Complexity:
#   O(n) for storing n elements in the stack

class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file
     def __init__(self):
         self.stack=[]
       
     def isEmpty(self):
         return len(self.stack)==0
       
     def push(self, item):
         self.stack.append(item)
         
     def pop(self):
         if len(self.stack)==0:
             return None
         return self.stack.pop()

     def peek(self):
         if len(self.stack)==0:
            return None
         return self.stack[-1]
        
     def size(self):
         return len(self.stack)
         
     def show(self):
         return self.stack
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
