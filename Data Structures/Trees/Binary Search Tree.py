"""
Author : Robin Singh
IMPLEMENTATION OF BINARY SEARCH TREE

"""
class Node:
    def __init__(self,ele):
        self.element = ele
        self.left = None
        self.right = None

class Binary_Search_tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,ele):
        temp_root = self.root
        temp2_root = None

        while temp_root:
            temp2_root = temp_root
            if ele < temp_root.element:
                temp_root = temp_root.left

            elif ele > temp_root.element:
                temp_root = temp_root.right

        new_node = Node(ele)
        if self.root:
            if ele < temp2_root.element:
                temp2_root.left = new_node

            else:
                temp2_root.right = new_node
        else:
            self.root = new_node


    def recursive(self,temp,e):
        if temp == None:
            node = Node(e)
            return node
        if e < temp.element:
            temp.left = self.recursive(temp.left,e)
        elif e>temp.element:
            temp.right = self.recursive(temp.right,e)

        return temp




    def search(self,k):
        temp = self.root
        while temp:
            if k < temp.element:
                temp = temp.left

            elif k> temp.element:
                temp = temp.right

            else:

                return True



        return False


    def inorder(self,temp):
        if temp:
            self.inorder(temp.left)
            print(temp.element,end="-->")
            self.inorder(temp.right)

    def preorder(self,temp):
        if temp:
            print(temp.element, end="-->")
            self.preorder(temp.left)
            self.preorder(temp.right)


    def postorder(self,temp):
        if temp:

            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.element, end="-->")





if __name__ == '__main__':
    b = Binary_Search_tree()
    while(1):
        print(f"\n1.Insert\t2.Search\t3.Traversals\t4.Exit")
        ch = int(input("Entre Your Choice"))
        if ch == 4:
            break

        elif ch == 1:
            ele = int(input("Entre Your Value"))
            b.insert(ele)
            b.inorder(b.root)

        elif ch == 2:
            search = int(input("Entre element to be searched"))
            if b.search(search):
                print("Present")
            else:
                print("Not Present")

        elif ch == 3:
            print(f"\n1.Inorder\t2.Preorder\t3.Postorder\n")
            trav = int(input("Entre Your choice"))
            if trav == 1:
                b.inorder(b.root)
            elif trav == 2:
                b.preorder(b.root)
            elif trav == 3:
                b.postorder(b.root)
            else:
                print("Invalid Option")

        else:
            print("Invalid")












