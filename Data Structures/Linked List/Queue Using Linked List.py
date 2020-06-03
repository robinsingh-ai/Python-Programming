"""
Author : Robin Singh
Implementation of Queue using linked list
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.start = None

    def enqueu_linkedlist(self,ele):
        new_node = Node(ele)
        if self.start == None:
            self.start=new_node
        else:
            new_node.next = self.start
            self.start = new_node

    def dequeu_linkedlist(self):
        if self.start == None:
            print("list has no elements")
            return
        n = self.start
        while n.next.next != None:
            n = n.next
        print("deleted ele", n.next.data)
        n.next = None

    def display_list(self):
        if self.start == None:
            print("Empty Queue,Entre Value")
            return True
        else:
            temp = self.start
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

    def isEmpty(self):
        if self.start == None:
            return True
        else:
            return False

    def last_element(self):
        if a.isEmpty():
            print("Empty Queue")

        else:
            n = self.start
            while n.next.next != None:
                n = n.next
            print("Last Element ", n.next.data)

    def size(self):
        curr = self.start
        count = 0
        while curr:
            count+=1
            curr = curr.next
        return count



if __name__ == '__main__':
    a = Linked_list()
    while(1):
        print(f"\n1.Insert\t2.Delete\t3.Display\t4.Exit\t5.Last Element\t6.Size")
        ch = int(input("Entre your choice"))

        if ch == 4:
            break

        elif ch ==1:
            ele = int(input("Entre ur number"))
            a.enqueu_linkedlist(ele)
            a.display_list()

        elif ch == 2:
            a.dequeu_linkedlist()

        elif ch == 3:
            a.display_list()

        elif ch == 5:
            a.last_element()

        elif ch == 6:
            c=a.size()
            print("Size of queue is = ",c)

        else:
            print("INVALID OPTION")

