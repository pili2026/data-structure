class Stack:
    def __init__(self):
        self.stack = []  # 使用串列來實作
        self.size = 0

    def Push(self, data):  # 把資料放到頂端
        self.stack.append(data) # append函式 把資料加進串列的末端
        self.size +=1

    def Pop(self):  # 把頂端的資料移除
        if self.size == 0:
            print("Stack is empty.")
        else:
            self.stack.pop()  # pop函式 把串列的最後一個元素移除
            self.size -= 1

    def Top(self): # 回傳頂端的資料
        if self.size == 0:
            print("Stack is empty.")
            return 0
        else:
            return self.stack[self.size - 1]  # 抓取串列最後一個元素的位置

    def isEmpty(self): # 回傳Stack是否為空
        return self.size == 0

    def getSize(self): # 回傳Stack大小
        return self.size

def main():
    s = Stack()
    s.Pop()
    print(s.isEmpty())
    print(s.getSize())
    s.Push(2)
    print(s.isEmpty())
    print(s.getSize())
    print(s.Top())

if __name__ == "__main__":
    main()

