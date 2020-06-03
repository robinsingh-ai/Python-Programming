"""
Author : Robin Singh
IMPLEMENTAION OF STACK USING LINKED LIST
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack_Using_Linked_list:
    def __init__(self):
        self.start = None

    def push(self,ele):
        new_node = Node(ele)
        if self.start==None:
            self.start=new_node
        else:
            temp = self.start
            while temp.next != None:
                temp=temp.next
            temp.next = new_node

    def pop(self):
        if a.isEmpty():
            print("Empty Stack")

        n = self.start
        while n.next.next is not None:
            n = n.next
        print("deleted ele",n.next.data)
        n.next = None

    def isEmpty(self):
        if self.start == None:
            return True
        else:
            return False

    def top_of_stack(self):
        if a.isEmpty():
            print("Empty Stack")

        else:
            n = self.start
            while n.next.next != None:
                n = n.next
            print("Top Element ", n.next.data)



    def display_stack(self):
        if a.isEmpty():
            print("Empty Stack")
        else:
            temp = self.start
            while temp:
                print(temp.data,end=" ")
                temp = temp.next


if __name__ == '__main__':
    a = Stack_Using_Linked_list()
    while(1):
        print(f"\n1.Push\t2.Pop\t3.Display\t4.Top Element\t5.Exit")
        ch = int(input("Entre Choice"))
        if ch == 5:
            break
        elif ch == 1:
            ele = int(input("Entre value"))
            a.push(ele)
            a.display_stack()
        elif ch == 2:
            a.pop()

        elif ch == 3:
            a.display_stack()

        elif ch == 4:
            a.top_of_stack()

        else:
            print("Invalid Option")


