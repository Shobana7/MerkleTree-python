import sys
import buildmtree as Module1

def findLeaf(node,inputString):
    if node == None:
        return None
    
    if node.data == inputString:
        return node
    
    temp = findLeaf(node.left_child,inputString)
    if(temp != None):
        return temp
    
    return findLeaf(node.right_child,inputString)
    
def constructProof(node,op,root):
    if node != root:
        if(node.parentNode.left_child != node):
            op.append(node.parentNode.left_child.hashValue)
            constructProof(node.parentNode,op,root)
        elif(node.parentNode.right_child != node):
            op.append(node.parentNode.right_child.hashValue)
            constructProof(node.parentNode,op,root)
    return op     

if __name__ == "__main__":  
    leafList = sys.argv[1]
    leaves = leafList[0:len(leafList)]
    leafNodes = leaves.split(",")

    root = Module1.buildMerkleTree(leafNodes)

    inputString = sys.argv[2]
    op = []
    lea = findLeaf(root,inputString)
    if(lea != None):
        output = constructProof(lea,op,root)
        output.append(root.hashValue)
        print("Yes",output)
    else:
        print("No")