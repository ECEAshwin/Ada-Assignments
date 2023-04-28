def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)
 
 
def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)
 
 
def createStack():
    stack = []
    return stack
 
 
def isEmpty(stack):
    return len(stack) == 0
 
 
def push(stack, item):
    stack.append(item)

 
 
def pop(stack):
 
    if(isEmpty(stack)):
        print("Stack Underflow ")
        exit(1)
 
    return stack.pop()
 
 
def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end=' ')
    print()
 
 
stack = createStack()
I = int(input("Enter Number of Integer : "))
print("Enter Integers")
for i in range(I):
    push(stack, str(int(input(""))))

print("Original Stack ")
prints(stack)
 
reverse(stack)
 
print("Reversed Stack ")
prints(stack)