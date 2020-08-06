class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    # insert data to the end
    def Push(self, data):
        self.queue.append(data)
        self.size += 1

    # remove the top data
    def Pop(self):
        if self.size == 0:
            print("Queue is empty.")
        else:
            # Remove the first element of the list
            self.queue = self.queue[1:]
            self.size -= 1

    def getFront(self):
        if self.size == 0:
            print("Queue is empty")
            return self.size
        else:
            return self.queue[0]

    # Return the last data
    def getBack(self):
        if self.size == 0:
            print("Queue is empty")
            return self.size
        else:
            return self.queue[-1]

    def isEmpty(self):
        return self.size == 0

    def getSize(self):
        return self.size


def main():
    queue = Queue()
    queue.Pop()
    queue.Push(2)
    queue.Push(9)
    print(queue.getSize())
    print(queue.getBack())
    print(queue.getFront())

if __name__ == '__main__':
    main()
    

