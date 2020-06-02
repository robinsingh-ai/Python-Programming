"""
Author : Robin Singh
Implementation of Circular Linked List
"""


class Node:
    def __init__(self,ele,next):
        self.element = ele
        self.next = next

class Cir_Linkedist:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def __len__(self):
        return self.size
    def is_Empty(self):
        if self.size == 0:
            return True
        else:
            return False
    def add_first(self,e):
        new_node = Node(e,None)
        if self.is_Empty():
            self.start = new_node
            self.end = new_node
            new_node.next = new_node

        else:
            self.end.next = new_node
            new_node.next = self.start
        self.start = new_node
        self.size+=1

    def add_last(self,e):
        new_node = Node(e,None)
        if self.is_Empty():
            self.start = new_node
            self.end = new_node
            new_node.next = new_node

        else:
            new_node.next = self.end.next
            self.end.next = new_node

        self.end = new_node
        self.size+=1

    def add_at_pos(self,e,pos):
        new_node = Node(e,None)
        temp = self.start
        i = 1
        while 1<pos:
            temp = temp.next
            i+=1
        new_node.next = temp.next
        temp.next = new_node
        self.size+=1

    def remove_first(self):
        if self.is_Empty():
            print("Empty List")
        head = self.end.next
        self.end.next = head.next
        self.start = head.next
        self.size-=1

        if self.is_Empty():
            self.end = None
        return head.element

    def display(self):
        temp = self.start
        i = 0
        while i<len(self):
            print(temp.element,end=" ")
            temp=temp.next
            i+=1


if __name__ == '__main__':
    a = Cir_Linkedist()
    while(1):
        print("\n1.Insert At Start\t2.Insert At End\t3.Remove\t4.Display\t5.Size\t6.Empty LL ?\t7.Exit\t8.Insert at Pos")
        ch = int(input("Entre your choice"))

        if ch == 7:
            break

        elif ch ==1:
            ele = int(input("Entre your Number"))
            a.add_first(ele)
            a.display()

        elif ch ==2:
            ele = int(input("Entre your Number"))
            a.add_last(ele)
            a.display()

        elif ch == 3:
            ele2 = a.remove_first()
            print("Deleted element is = ",ele2)

        elif ch == 4:
            a.display()

        elif ch == 5:
            print("size is ",a.__len__())

        elif ch == 6:
            if a.is_Empty():
                print("Empty List")
            else:
                a.display()

        elif ch == 8:
            pos = int(input("Entre position"))
            ele = int(input("Entre Element"))
            a.add_at_pos(ele,pos)
            a.display()

        else:
            print("invalid option")







