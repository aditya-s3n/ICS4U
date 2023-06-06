import Stacks_Implementation as s

numbers_stack = s.Stack()
numbers_stack.push(3)
numbers_stack.push(14)
numbers_stack.push(-8)
numbers_stack.push(1)

print(f"State of the stack after 4 pushes: {numbers_stack}")

value = numbers_stack.pop()
print("\nState of the stack after 1 pop", numbers_stack)
print("Valuethat was popped", value)

value = numbers_stack.peek()
print("\nState of the stack after 1 pop", numbers_stack)
print("Valuethat was popped", value)

print(f"\nTesting if the numbers stack is empty: {numbers_stack.empty()}")
numbers_stack.pop()
numbers_stack.pop()
numbers_stack.pop()
print(numbers_stack.empty())