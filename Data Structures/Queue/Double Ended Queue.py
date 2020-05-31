"""
AUTHOR: Robin Singh
IMPLEMENTATION OF DOUBLE ENDED QUEUE

"""

class DoubleEnded:
    def __init__(self,lenght = 5):#Change according to you
        self.items = []
        self.length = lenght

    def isFull(self):
        if len(self.items) == self.length:
            return True
        else:
            return False

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def Enqueue_start(self,ele):
        if (self.isFull()):
            return True
        else:
            self.items.insert(0,ele)
    def Enqueue_End(self,ele):
        if (self.isFull()):
            return True
        else:
            self.items.append(ele)

    def Dequeue_start(self):
        if (self.isEmpty()):
            return True
        else:
            return self.items.pop(0)

    def dequeue_End(self):
        if (self.isEmpty()):
            return True
        else:
            return self.items.pop()

    def display(self):
        if self.items == []:
            return True
        else:
            print(self.items)


if __name__ == '__main__':
    a = DoubleEnded()
    while (1):

        print(f"\n1.Enqueue START \t2.Enqueue End \t3.Dequeue Start \t4.Dequeue End\t5.Display\t6.Exit")
        ch = int(input("entre ur choice"))
        if ch == 6:
            break

        elif ch == 1:
            ele = int(input("Entre Element to be pushed At START"))
            if (a.Enqueue_start(ele)):
                print("Queue Overflown")
            else:
                a.display()


        elif ch == 2:

            ele = int(input("Entre Element to be pushed at END"))

            if (a.Enqueue_End(ele)):
                print("Queue Overflown")

            else:

                a.display()


        elif ch == 3:
            t = a.Dequeue_start()
            if t == 1:
                print("Queue Is Empty,Insert Number")
            else:
                print(f"Dequeued value = {t}")
                a.display()


        elif ch == 4:

            t = a.dequeue_End()

            if t == 1:

                print("Queue Is Empty,Insert Number")

            else:

                print(f"Dequeued value = {t}")

                a.display()


        elif ch == 5:
            a.display()

        else:
            print("INVALID OPTION")
