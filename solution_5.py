import hashlib
from time import gmtime, strftime
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):   
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8') +
                   str(self.timestamp).encode('utf-8')) 
        sha.update(hash_str)
        
        return sha.hexdigest()
    
    def __str__(self):
        return "\nBlock Hash:{}\nData:{}\nPrevious Hash:{}\nTimestamp:{}".format(self.hash, self.data, self.previous_hash, self.timestamp)


class Node:
    
    def __init__(self, data, previous_hash):
        self.block = Block(time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime()), data, previous_hash)
        self.next = None


class BlockChain():
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, data = None):   
        if data == None:
            print("Can't append empty block")
            return

        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
            return    
        
        self.tail.next = Node(data, self.tail.block.hash)
        self.tail = self.tail.next          
        
    def __str__(self):
        if self.head == None:
            return 'Block chain is empty'
        
        current = self.head
        outstring = ""
        while current:
            outstring += str(current.block)
            current = current.next
        return outstring


print('\n------------------------------\n')
block_chain = BlockChain()
block_chain.append("Some Information")
block_chain.append("new Information")
block_chain.append("3rd Block")


current_block = block_chain.head
print(block_chain)
#expected output: prints the 3 blocks

print(current_block.block)
#outputs the first blocks data

current_block = current_block.next
print(current_block.block)
#outputs the second blocks data

current_block = current_block.next
print(current_block.block)
#outputs the last blocks data

print('\n------------------------------\n')
block_chain = BlockChain()

print(block_chain)
#expected output: Block Chain is empty

print('\n------------------------------\n')
block_chain = BlockChain()

block_chain.append()
block_chain.append("only this block should be there")
block_chain.append()

print(block_chain)
#expected output: prints 1 block only