# Date: Wed, 8/12/20
# Question: List representation of a min heap

class MinHeapList:

    def __init__(self):
        self.list = []

    def push(self, x: int):
        self.list.append(x)
        self._bubble_up(len(self.list)-1)

    def peek(self) -> int:
        return list[0]

    def pop(self):
        self._swap(0, len(self.list)-1)
        self.list.pop()
        self._bubble_down(0)

    def _swap(self, index_i: int, index_j: int):
        i = self.list[index_i]
        self.list[index_i] = self.list[index_j]
        self.list[index_j] = i

    def _bubble_up(self, index_i: int):
        parent_index = index_i // 2
        if parent_index != index_i and self.list[parent_index] > self.list[index_i]:
            self._swap(parent_index, index_i)
            self._bubble_up(parent_index)
        return

    def _bubble_down(self, index_i: int):
        left_child_index = 2*index_i + 1
        right_child_index = 2*index_i + 2
        if left_child_index < len(self.list) and self.list[left_child_index] < self.list[index_i]:
            self._swap(left_child_index, index_i)
            self._bubble_down(left_child_index)
        elif right_child_index < len(self.list) and self.list[right_child_index] < self.list[index_i]:
            self._swap(right_child_index, index_i)
            self._bubble_down(right_child_index)
        return


def main():
    minHeapList = MinHeapList()
    minHeapList.push(5)
    minHeapList.push(3)
    minHeapList.push(4)
    minHeapList.push(12)
    minHeapList.push(2)
    minHeapList.pop()
    minHeapList.push(4)
    minHeapList.push(53)
    minHeapList.push(2)
    minHeapList.pop()
    minHeapList.push(34)
    minHeapList.pop()
    print(minHeapList.list)


if __name__ == '__main__':
    main()
