class Stack:
    def __init__(self):
        self._stack: list = []

    def is_empty(self) -> bool:
        return len(self._stack) == 0

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        # return self._stack[-1] # python way
        return self._stack[len(self._stack) - 1]

    def size(self) -> int:
        return len(self._stack)


def reverse_string(s: str) -> str:
    stack: Stack = Stack()
    for character in s:
        stack.push(character)

    result: str = ""
    while not stack.is_empty():
        result += stack.pop()

    return result


string: str = "This string will be reversed ..."
print(reverse_string(string)) # ... desrever eb lliw gnirts sihT


