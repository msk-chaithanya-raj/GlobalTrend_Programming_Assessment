class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self, val):
        try:
            index = self.heap.index(val)
            self.heap[index] = self.heap[-1]
            self.heap.pop()
            self._heapify_down(index)
        except ValueError:
            pass  # Value not in heap

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)
def max_heap_operations():
    heap = MaxHeap()
    while True:
        print("\nMaxHeap Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Get Max")
        print("4. Exit")
        choice = input("Choose an operation: ")
        if choice == '1':
            val = int(input("Enter value to insert: "))
            heap.insert(val)
            print(f"Heap: {heap.heap}")
        elif choice == '2':
            val = int(input("Enter value to delete: "))
            heap.delete(val)
            print(f"Heap: {heap.heap}")
        elif choice == '3':
            print(f"Max Value: {heap.get_max()}")
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")
max_heap_operations()
