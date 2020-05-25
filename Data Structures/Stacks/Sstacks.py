"""
AUTHOR :Robin Singh
STACK IMPLEMENTATION

"""

class Stack:

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.items == []:
            return True
        else:

            return self.items.pop()

    def tos(self):

        if self.items:
            return self.items[-1]
        else:
            return None

    def size(self):
        if self.items:
            return len(self.items)
        else:
            return None

    def isEmpty(self):
        if self.items == []:

            return True
        else:

            return False
    def display(self):
        if self.items == []:
            return true
        else:
            print(self.items)




if __name__ == '__main__':

    a = Stack()
    while (1):

        print(f"\n1.Push\n2.Pop\n3.StackTop\n4.Display\n5.Stack Empty\n6.Size\n7.Exit")
        ch = int(input("entre ur choice"))

        if ch == 7:
            break

        elif ch == 1:
            ele = int(input("Entre Element to be pushed"))
            a.push(ele)
            a.display()

        elif ch == 2:
            t = a.pop()
            print(f"poped value = {t}")
            a.display()

        elif ch == 3:
            print(a.tos())


        elif ch == 4:
            a.display()

        elif ch == 5:
            if (a.isEmpty()):
                print("empty stack")
            else:
                print("Not Empty")

        elif ch == 6:
            t = a.size()
            print("size of stack is ",t)

        else:
            print("invalid option")







