class Stack():

    def __init__(self):
        self._length = 0
        self._top = None

    def push(self, value):
        new_node = ListNode(value)

        new_node.change_link(self._top)

        self._top = new_node

        self._length += 1

    def pop(self):
        if self._top != None:
            node = self._top
            lower_node = node.link()
            self._top = lower_node

            self._length -= 1

            return node.value()
        
        
        else:
            return None
        
    def peek(self):
        return self._top.value()
    
    def empty(self):
        if self._top == None:
            return True
        else:
            return False
        
    def __str__(self):
        list_to_print = []

        node = self._top

        for i in range(self._length):
            list_to_print.append(node.value())
            node = node.link()

        return str(list_to_print)


class ListNode:
    def __init__(self, value):
        self._value = value
        self._link = None

    def value(self):
        return self._value
    
    def change_link(self, new_link):
        self._link = new_link

    def link(self):
        return self._link
    
    def __str__(self):
        return str(self._value)


my_stack = Stack()

my_stack.push(22)

print(my_stack.pop())
print(my_stack)


someStack = Stack()
someStack.push('a')
someStack.push('b')
someStack.push('c')
someStack.push('d')
someStack.pop()
someStack.pop()
someStack.pop()
someStack.pop()
someStack.push('e')

someStack.push('a')

someStack.push('b')
someStack.pop()
someStack.push('c')

someStack.push('d')

someStack.push('e')
someStack.push('a')
someStack.pop()
someStack.pop()
someStack.push('b')

print(someStack)



stack1 = Stack()
stack1.push("D")
stack1.push("C")
stack1.push("B")
stack1.push("A")

stack2 = Stack()

stack3 = Stack()

print(stack1)
print(stack2)
print(stack3)

stack2.push(stack1.pop())
stack2.push(stack1.pop())

stack3.push(stack1.pop())

stack2.push(stack1.pop())

stack3.push(stack2.pop())
stack3.push(stack2.pop())
stack3.push(stack2.pop())

print(stack1)
print(stack2)
print(stack3)