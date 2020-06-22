"""
Author : Robin Singh
Implementation Of Huffman Coding
Huffman coding is a lossless data compression algorithm. In this algorithm, a variable-length code is
assigned to input different characters. The code length is related to how frequently characters are used
Most frequent characters have the smallest codes and longer codes for least frequent characters


Time Complexity : O(nLogn)
"""


class NodeTree:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def nodes(self):
        return self.left, self.right

    def __str__(self):
        return  self.left, self.right



def huffman_coding_greedy(node, left=True, string=''):
    if type(node) is str:
        return {node: string}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_coding_greedy(l, True, string + '0'))
    d.update(huffman_coding_greedy(r, False, string + '1'))
    return d
freq = {}
string = input("Entre Your String")
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
nodes = freq
while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    Code = huffman_coding_greedy(nodes[0][0])
    print("Huffman Encoding\nLetter\tFrequency\tCode")
    i=0
    for (char, frequency) in freq:
        print(f" {char}\t\t{freq[i][1]}\t\t\t{Code[char]}")
        i+=1

