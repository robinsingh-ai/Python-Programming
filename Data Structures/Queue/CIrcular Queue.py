class CirQueue:
    def __init__(self,length = 5):
        self.items = []
        self.rear = 0
        self.front = 0
        self.length = length

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False


    def fullqueue(self):
        if len(self.items) == self.length:
            return True
        else:
            return False

    def enqueue(self, data):
        if (self.fullqueue()):
            # print('Queue is Full!')
            return True
        elif self.isEmpty():
            self.front = self.rear = 0
            self.items.append(data)
        else:
            self.rear += 1
            self.items.append(data)

    def dequeue(self):
        if self.isEmpty():

            return 1

        else:
            self.front += 1
            return self.items.pop(0)

    def display(self):
        if self.items == []:
            return True
        else:
            print(self.items)

if __name__ == '__main__':
    a = CirQueue()
    while (1):

        print(f"\n1.Enqueue\t2.Dequeue\t3.Display\t4.Queue Empty\t5.Exit")
        ch = int(input("entre ur choice"))
        if ch == 5:
            break

        elif ch == 1:
            ele = int(input("Entre Element to be pushed"))
            if (a.enqueue(ele)):
                print("Queue Overflown")
            else:
                a.display()

        elif ch == 2:
            t = a.dequeue()
            if t == 1:
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


        else:
            print("INVALID OPTION")












