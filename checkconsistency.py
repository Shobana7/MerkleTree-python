import hashlib,sys
import checkinclusion as Module2
import buildmtree as Module1

def nodeExists(node,inputString):
    if node == None:
        return None
    
    if node.hashValue == inputString:
        return node
    
    temp = nodeExists(node.left_child,inputString)
    if(temp != None):
        return temp
    
    return nodeExists(node.right_child,inputString)

def getHashValue(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()
    
def checkConsistency(leaves1,leaves2,root1,root2):
    i=0
    while i < len(leaves1):
        if leaves1[i]!=leaves2[i]:
            break
        i+=1
    if i < len(leaves1):
        return []
    
    op = []
    temp = nodeExists(root2,root1.hashValue)
    if(temp != None):
        op.append(root1.hashValue)
        op = Module2.constructProof(temp,op,root2)
        op.append(root2.hashValue)
    else:
        leftChild = root1.left_child.hashValue
        rightChild = root1.right_child.hashValue
        temp = nodeExists(root2,rightChild)
        rightChildSibling = temp.parentNode.right_child.hashValue
        op.append(leftChild)
        op.append(rightChildSibling)
        combinedHash = getHashValue(rightChild + rightChildSibling)
        parentHash = getHashValue(leftChild + combinedHash)
        node = nodeExists(root2,parentHash)
        op = Module2.constructProof(node,op,root2)
        op.append(root2.hashValue)
    
    return op 

if __name__ == "__main__":  
    leafList_Tree1 = sys.argv[1]
    leafList_Tree2 = sys.argv[2]
    leaves_Tree1 = leafList_Tree1[0:len(leafList_Tree1)]
    leaves1 = leaves_Tree1.split(",")
    leavesString2 = leafList_Tree2[0:len(leafList_Tree2)]
    leaves2 = leavesString2.split(",")

    root1 = Module1.buildMerkleTree(leaves1)
    root2 = Module1.buildMerkleTree(leaves2)

    fd = open("merkle.trees","w")
    fd.write("Merkle Tree 1 \n\n")
    Module1.writeMerkleTree(root1,fd)
    fd.write("\n\n")
    fd.write("Merkle Tree 2 \n\n")
    Module1.writeMerkleTree(root2,fd)
    fd.close()
    
    op = checkConsistency(leaves1,leaves2,root1,root2)
    if(len(op)>0):
        print('Yes',op)
    else:
        print('No')