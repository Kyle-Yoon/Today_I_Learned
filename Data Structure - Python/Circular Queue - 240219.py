class CQueue:
    MAXSIZE = 10
    
    def __init__(self):
        self.container = [None for _ in range(CQueue.MAXSIZE)]
        self.front = 0
        self.rear = 0
        
    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
    
    def __step_forward(self, x):
        x += 1
        if x >= CQueue.MAXSIZE:
            x = 0
        return x
    
    def is_full(self):
        next = self.__step_forward(self.rear)
        if next == self.front:
            return True
        return False
    
    def enqueue(self, data):
        if self.is_full():
            raise Exception("The queue is full")
        self.container[self.rear] = data
        self.rear = self.__step_forward(self.rear)
        
    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        ret = self.container[self.front]
        self.front = self.__step_forward(self.front)
        return ret
    
    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        return self.container[self.front]