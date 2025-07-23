class Stack:
    def __init__(self):
        self.stack= []
        self.top= -1

    def push(self, element):
        #increment the top value from -1 by +1
        self.top += 1
        #check if the index of the top if less than the max size of the stack
        if self.top < len(self.stack):
            self.stack[self.top]=element # overwrite the existing top value - Time:O(1)
        else:
            self.stack += [element]
    def pop(self):
        #check for underflow condition
        if self.top == -1:
            print("Stack underflow")
            return None
        element = self.stack[self.top] #store the top index value in a variable
        self.top -= 1 #decrement the top position- Time:O(1)
        return element #return the popped value
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        return self.stack[self.top]
    def empty(self):
        return self.top == -1


s= Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.peek())
s.pop()
print(s.peek())