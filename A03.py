class Stack:
    def __init__(self, stack=None):
        self.stack = [] if stack is None else stack
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    
    def top(self):
        return self.stack[self.size()-1]

    def size(self):
        return len(self.stack)
    
    def empty(self):
        return len(self.stack) == 0
def invert (liste):
    st = Stack()
    ls = []
    
    for item in liste:
        if item != ' ':
            st.push(item)
        elif item == ' ':
            while not st.empty():
                ls.append(st.pop())
            ls.append(' ')
    while not st.empty():
        ls.append(st.pop())
    return ls

ls1 = [3, 5, 8, 8, 4, 1]
print(ls1)
print(invert(ls1))