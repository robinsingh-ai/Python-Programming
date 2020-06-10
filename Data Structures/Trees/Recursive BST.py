"""
Author : Robin Singh
Implementation of Recursive binary tree

"""

class Node:
    def __init__(self, ele):
        self.element = ele
        self.left = None
        self.right = None


class Binary_Search_tree:
    def __init__(self):
        self.root = None
        self.size = 0


    def recursive(self, temp, e):
        if temp == None:
            node = Node(e)
            return node
        if e < temp.element:
            temp.left = self.recursive(temp.left, e)
        elif e > temp.element:
            temp.right = self.recursive(temp.right, e)

        return temp

    def search(self, k):
        temp = self.root
        while temp:
            if k < temp.element:
                temp = temp.left

            elif k > temp.element:
                temp = temp.right

            else:
                return True




        return False

    def inorder(self, temp):
        if temp:
            self.inorder(temp.left)
            print(temp.element, end="-->")
            self.inorder(temp.right)

    def preorder(self, temp):
        if temp:
            print(temp.element, end="-->")
            self.preorder(temp.left)
            self.preorder(temp.right)

    def postorder(self, temp):
        if temp:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.element, end="-->")




if __name__ == '__main__':
    b = Binary_Search_tree()
    b.root = b.recursive(None,90)
    b.recursive(b.root,12)
    b.recursive(b.root,78)
    b.recursive(b.root,900)
    b.recursive(b.root,789)
    b.recursive(b.root,102)
    b.recursive(b.root,123)
    b.recursive(b.root,30)
    b.recursive(b.root,23)
    b.recursive(b.root,1)
    b.recursive(b.root,2)
    b.inorder(b.root)
    print()
    b.postorder(b.root)
    print()
    b.preorder(b.root)
    print()

    print(b.search(45))
    print(b.search(900))












