class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x) # add from right side (Queue - FIFO)

    def pop(self) -> int:
        size = len(self.queue)   
        for _ in range(size-1):  # Shift current top node to the left-most side
            self.queue.append(self.queue.pop(0))  # remove from left & add to right
        return self.queue.pop(0) # remove from left side (Queue - FIFO)

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not bool(self.queue)