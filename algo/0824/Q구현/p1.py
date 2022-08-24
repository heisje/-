import sys
sys.stdin = open('input.txt')

class Q:
    def __init__(self):
        self.N = 4
        self.arr = [None] * self.N
        self.top = 0
        self.rear = 0
    def enQueue(self, a):
        if self.isFull():
            print('enQueue error')
        else:
            self.rear = (self.rear + 1) % self.N
            self.arr[self.rear] = a
    def deQueue(self):
        if self.isEmpty():
            return 'deQueue error'
        else:
            self.top = (self.top + 1) % self.N
            return self.arr[self.top]
    def isEmpty(self):
        return self.top == self.rear
    def isFull(self):
        return self.top == (self.rear + 1) % self.N
    def Qpeek(self):
        return self.arr[self.top + 1]
my_instance = Q()
my_instance.enQueue('a')
my_instance.enQueue('b')
my_instance.enQueue('c')
print(my_instance.deQueue())
print(my_instance.deQueue())
my_instance.enQueue('d')
my_instance.enQueue('e')
my_instance.enQueue('f')
print(my_instance.deQueue())
print(my_instance.deQueue())
print(my_instance.deQueue())
print(my_instance.deQueue())
my_instance.enQueue('g')
print(my_instance.Qpeek())
print(my_instance.arr)
