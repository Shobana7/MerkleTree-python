import hashlib,sys

class MerkleTreeNode:
    def __init__(self,data):
        self.left_child = None
        self.right_child = None
        self.parentNode = None
        self.data = data
        self.hashValue = hashlib.sha256(data.encode('utf-8')).hexdigest()

def buildMerkleTree(leafNodes):
    mTree = []
    for i in leafNodes:
        mTree.append(MerkleTreeNode(i))

    while len(mTree)!=1:
        tempTree = []
        for i in range(0,len(mTree),2):
            Node1 = mTree[i]
            if i+1 < len(mTree):
                Node2 = mTree[i+1]
            else:
                tempTree.append(mTree[i])
                break
                
            parent = MerkleTreeNode(Node1.hashValue + Node2.hashValue)
            parent.left_child = Node1
            parent.right_child = Node2
            Node1.parentNode = parent
            Node2.parentNode = parent
            tempTree.append(parent)
        mTree = tempTree 

    return mTree[0]

def writeMerkleTree(node,fd)-> None:
    if node != None:
        if node.left_child != None:
            fd.write("Left: "+str(node.left_child.hashValue) + "\n")
            fd.write("Right: "+str(node.right_child.hashValue) +" \n")
            fd.write("ParentData: "+str(node.data) +"\n")
            fd.write("ParentHash: "+str(node.hashValue) +"\n")
            fd.write("\n")
            writeMerkleTree(node.left_child,fd)
            writeMerkleTree(node.right_child,fd)
        else:
            fd.write("Input \n")
            fd.write("Data: "+str(node.data) +"\n")
            fd.write("Hash: "+str(node.hashValue) +"\n")
            fd.write("\n")
            writeMerkleTree(node.left_child,fd)
            writeMerkleTree(node.right_child,fd)
      
if __name__ == "__main__":   
    #Input read from commandline 
    #Pass the leaf nodes enclosed in double quotes separated by commas
    inputString = sys.argv[1]
    leaves = inputString[0:len(inputString)]
    leafNodes = leaves.split(",")

    #building MerkleTree
    root = buildMerkleTree(leafNodes)

    #Output written to file
    fd = open("merkle.tree", "w")
    writeMerkleTree(root,fd)
    fd.close()
    
