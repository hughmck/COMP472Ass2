from typing import List

from State import State


class PriorityQueue(object):
    def __init__(self):
        self.queue:List[State] = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data:State):
        self.queue.append(data)
        sortedQueue = sorted(self.queue, key=self.takeCost)
        self.queue = sortedQueue

    def insertH(self, data:State):
        self.queue.append(data)
        sortedQueue = sorted(self.queue, key=self.takeH)
        self.queue = sortedQueue

    def takeCost(self, elem:State):
        return elem.cost

    def takeH(self, elem:State):
        return elem.h

    def getState(self, state:State) -> State:
        return self.queue.remove(state)

    # for popping the leftMost state based on Priority
    # if no item, silently handle exception
    def get(self) -> State :
        try:
            item = self.queue[0]
            del self.queue[0]
            return item
        except IndexError:
            print()
            exit()

