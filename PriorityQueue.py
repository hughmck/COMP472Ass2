from typing import List

from State import State


class PriorityQueue(object):
    def __init__(self):
        self.queue:List[State] = []
    def queueIsEmpty(self) -> bool:
        return len(self.queue) == 0

    def appendState(self, data:State):
        self.queue.append(data)



