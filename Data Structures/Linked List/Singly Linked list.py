"""
AUTHOR : Robin Singh
IMPLEMENTATION OF SINGLY LINKED LIST OR DOUBLY LINKED  LIST

"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.start = None

    def insert_start(self,ele):
        new_node = Node(ele)
        if self.start == None:
            self.start=new_node
        else:
            new_node.next = self.start
            self.start = new_node

    def insert_end(self,ele):
        new_node = Node(ele)
        if self.start==None:
            self.start=new_node
        else:
            temp = self.start
            while temp.next != None:
                temp=temp.next
            temp.next = new_node

    def delete(self):
        if self.start ==None:
            print("Empty")
        else:
            temp = self.start
            self.start = self.start.next
            return temp.data

    def delete_end(self):
        if self.start == None:
            print("list has no elements")
            return
        n = self.start
        while n.next.next != None:
            n = n.next
        print("deleted ele",n.next.data)
        n.next = None




    def display_list(self):
        if self.start == None:
            return True
        else:
            temp = self.start
            while temp:
                print(temp.data,end=" ")
                temp = temp.next

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
        print(f"\n1.Insert At Start\t2.Insert At End\t3.Delete start\t4.Delete End\t5.Display\t6.Size\t7.Exit")
        ch = int(input("Entre your choice"))

        if ch == 7:
            break

        elif ch == 1:
            ele = int(input("Entre YOur Number To be Inserted at start"))
            a.insert_start(ele)
            a.display_list()


        elif ch == 2:
            ele = int(input("Entre YOur Number To be Inserted at end"))
            a.insert_end(ele)
            a.display_list()



        elif ch == 3:
            ele2 = a.delete()
            print("deleted element is ",ele2)


        elif ch == 5:
            if (a.display_list()):
                print("print")

        elif ch == 6:
            c=a.size()
            print("size of linked list is ",c)

        elif ch == 4:
            a.delete_end()


        else:
            print("Invalid Option")






