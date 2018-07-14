from . import stack


test = stack.Stack()

print(test.push(22))
print(test.push(1))

print(test.size())
test.view()

print("\n")
x = test.pop()
y = test.pop()
print(x)
print(y)
ans = x + y
print(str(ans))
print(test.pop())