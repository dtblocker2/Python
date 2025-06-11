class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

def find_next_greater_elements(arr):
    n = len(arr)
    result = [-1] * n
    stack = Stack()
    A = stack.stack

    for i in range(n):
        #print("Local Variables:", locals())
        while not stack.is_empty() and arr[i] > arr[stack.peek()]:
            index = stack.pop()
            result[index] = arr[i]
        stack.push(i)
    return result

arr1 = [4, 5, 2, 2, 8]
print(find_next_greater_elements(arr1))  # Output: [5, 10, 10, -1, -1]

arr2 = [3, 7, 1, 7, 5]
print(find_next_greater_elements(arr2))  # Output: [7, -1, 7, -1, -1]
