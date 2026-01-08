"""
LeetCode: 2025 12 17 17.19.47 Accepted Runtime 8ms Memory 21.3MB

Algorithm:
Maintain two stacks: one for all values, one for minimum values. push(): add to main stack, and if minStack is empty or new value <= current minimum, add to minStack. pop(): remove from main stack, and if the removed value equals the top of minStack, remove from minStack. top() returns main stack top. getMin() returns minStack top.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack or val <= self.minStack[-1]: 
            self.minStack.append(val)

    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]: 
            self.minStack.pop()

        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()