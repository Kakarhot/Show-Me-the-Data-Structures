import sys

class Node():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def children(self):
        return (self.left, self.right)
    

def huffman_tree(node, left=1, bin_string=''):
    if type(node) == str:
        return {node: bin_string}
    
    (l, r) = node.children()
    d = {}
    d.update(huffman_tree(l, 1, bin_string + '0'))
    d.update(huffman_tree(r, 0, bin_string + '1'))
    
    return d
    

def huffman_encoding(data):
        
    f_dict = {}
    for c in data:
        f_dict[c] = f_dict.get(c, 0) + 1
    freq = sorted(f_dict.items(), key=lambda tup: tup[1], reverse=True)

    nodes = freq
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = Node(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda tup: tup[1], reverse=True)

    tree = huffman_tree(nodes[0][0])
    
    encoded_data = ''.join([tree[c] for c in data])
    
    return encoded_data, tree

def huffman_decoding(data, tree):
    inv_tree = {v: k for k, v in tree.items()}
    output = ''
    while len(data) >= 1:
        i = 1
        while data[:i] not in inv_tree:
            i += 1
        output = output + inv_tree[data[:i]]
        data = data[i:]
    return output  


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    # print(tree)
    # print(encoded_data)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))