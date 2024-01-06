from datetime import datetime
import collections

import numpy as np
class MyCircularQueue:

    def __init__(self, k: int):
        self.values = np.array((k,), dtype=int)
        self.pointer = 0
        self.beginpointer = 0
        self.endpointer = 0
        self.mod = k
        self.empty = True

    def beginpointer_decrease(self):
        if self.IsEmpty():
            return
        else:



    def enQueue(self, value: int) -> bool:
        if self.endpointer += 1
        self.values[self.endpointer % self.mod] = value
    def deQueue(self) -> bool:
        if not self.empty:


    def Front(self) -> int:

    def Rear(self) -> int:

    def isEmpty(self) -> bool:

    def isFull(self) -> bool:


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


if __name__ == "__main__":
    start_time = datetime.now()
    k = 5
    value = 1

    obj = MyCircularQueue(k)
    param_1 = obj.enQueue(value)
    param_2 = obj.deQueue()
    param_3 = obj.Front()
    param_4 = obj.Rear()
    param_5 = obj.isEmpty()
    param_6 = obj.isFull()
    print(obj, param_1, param_2, param_3, param_4, param_5, param_6)

    print(sol.bagOfTokensScore([100,200],150))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))