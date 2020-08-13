import heapq
import copy


class MinimumStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def top(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
        self.stack.pop()

    def get_min(self):
        heap_stack = copy.copy(self.stack)
        heapq.heapify(heap_stack)
        return heapq.nsmallest(1, heap_stack)[0]

    def __str__(self):
        return str(self.stack)


class Main:
    if __name__ == "__main__":
        min_stack = MinimumStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        min_stack.get_min()     # Returns -3.
        min_stack.pop()
        min_stack.top()         # Returns 0.
        min_stack.get_min()     # Returns -2.
