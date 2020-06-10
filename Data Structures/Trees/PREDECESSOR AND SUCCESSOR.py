"""
Author : Robin Singh
Implementation Of  finding Predecessor And Successor on BST using simple iterative method

"""
class SUCC_PRED:


    def __init__(self, data):
        self.dat = data
        self.left = None
        self.right = None



def pandd(root, p, s, dat):
    if root == None:
        return

    while root != None:


        if root.dat == dat:

            if root.right:
                s[0] = root.right
                while s[0].left:
                    s[0] = s[0].left


            if root.left:
                p[0] = root.left
                while p[0].right:
                    p[0] = p[0].right

            return

        elif root.dat < dat:
            p[0] = root
            root = root.right


        else:
            s[0] = root
            root = root.left


def insert(node, dat):
    if node == None:
        return SUCC_PRED(dat)
    if dat < node.dat:
        node.left = insert(node.left, dat)
    else:
        node.right = insert(node.right, dat)
    return node


if __name__ == '__main__':

    print("Insert value of Root Node")
    val = int(input("Entre Value"))
    a = None
    a = insert(a, val)

    while(1):
        p, s = [None], [None]
        print(f"\n1.Insert\t2.Finding Predecessor And Successor\t3.Exit ")
        ch = int(input("Entre Choice"))

        if ch == 3:
            break
        elif ch == 1:
            ele = int(input("Entre Your Value to be inserted"))
            insert(a, ele)

        elif ch ==2:
            key = int(input("Entre Key"))
            pandd(a, p, s, key)
            if p[0] != None:
                print(f"Predecessor :{ p[0].dat}")
            else:
                print("No Value in BST is lesser than key")


            if s[0] != None:
                print(f"Successor :  {s[0].dat}")
            else:
                print("No value in BST is greater than key")
        else:
            print("invalid option")






