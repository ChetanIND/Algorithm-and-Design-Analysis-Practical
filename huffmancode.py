# Write a program to implement huffman algorithm given a table of characters and fequencies
class Node:
    def __init__(self, char, freq, left=None, right=None):
        # setting the character
        self.char = char

        # setting the frequency
        self.freq = freq

        # setting the left child
        self.left = left

        # Setting the right child
        self.right = right

        # setting the huffman code
        self.huffman = ""


def frequency_node(chars):
    # inserting all the frequencies into the frequency array
    f_table = {}
    for i in chars:
        if i not in f_table:
            f_table[i] = 1
        else:
            f_table[i] += 1

    return f_table


# utility function to print the huffman code
def printNodes(node, val=""):
    newVal = val + str(node.huffman)

    # checking if left child is present
    if node.left:
        printNodes(node.left, newVal)

    # chekcing if right child is present
    if node.right:
        printNodes(node.right, newVal)

    # if the node is terminal node then printing the huffman code
    if not node.left and not node.right:
        print(f"{node.char}    |     {node.freq}     |     {newVal}")


if __name__ == "__main__":
    chars = input("Enter the string: ")
    f_table = frequency_node(chars)

    # list of unused nodes
    nodes = []

    # appending the Node into the list of nodes
    for key, value in f_table.items():
        nodes.append(Node(key, value))

    # main loop to generate the tree
    while len(nodes) > 1:
        # sorting the nodes by the frequency where the node with lowest frequency
        # would appear first and the one with higher frequency will appear later
        nodes = sorted(nodes, key=lambda x: x.freq)

        # extract the two smallest nodes
        left = nodes[0]
        right = nodes[1]

        # also setting the huffman code
        left.huffman = 0
        right.huffman = 1

        # add the smallest node into a new node
        newNode = Node(left.char + right.char, left.freq + right.freq, left, right)

        # remove the two extracted nodes
        nodes.remove(left)
        nodes.remove(right)

        # insert the node into the list of nodes
        nodes.append(newNode)

    # main function here
    print("Char | Frequency | Huffman Code")
    print("--------------------------------")
    printNodes(nodes[0])
