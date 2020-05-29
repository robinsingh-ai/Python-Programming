"""
AUTHOR : Robin Singh
IMPLEMENTATION OF SIMPLE QUEUE

"""

class arrQueue:
    def __init__(self,length=5): #change value of lenth according to you
        self.items = []
        self.size = 0
        self.front = 0
        self.rear = 0
        self.limit = length

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    def enqueue(self,data):
        if self.size >=self.limit:
            return -1
        else:
            self.items.append(data)

        if self.front ==None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size+=1

    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            return self.items.pop(0)
            self.size =self.size-1
            if self.size == 0:
                self.front = self.rear = 0
            else:
                self.rear = self.size - 1

    def Size(self):
        return self.size

    def display(self):
        if self.items == []:
            return True
        else:
            print(self.items)






if __name__ == '__main__':

        a = arrQueue()
        while (1):

            print(f"\n1.Enqueue\t2.Dequeue\t3.Display\t4.Stack Empty\t5.Size\t6.Exit")
            ch = int(input("entre ur choice"))
            if ch == 6:
                break

            elif ch == 1:
                ele = int(input("Entre Element to be pushed"))
                if (a.enqueue(ele)):
                    print("Queue Overflown")
                else:
                    a.display()

            elif ch == 2:
                t = a.dequeue()
                if t ==-1:
                    print("Queue Is Empty,Insert Number")
                else:
                    print(f"Dequeued value = {t}")
                    a.display()

            elif ch == 3:
                a.display()

            elif ch == 4:
                if (a.isEmpty()):
                    print("Empty Queue")
                else:
                    print("Not Empty")

            elif ch == 5:
                t = a.Size()
                print("size of stack is ", t)

            else:
                print("INVALID OPTION")





