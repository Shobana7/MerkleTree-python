# MerkleTree-
The Merkle Tree implementation contains 3 modules:
1. buildmtree.py
This module builds the Merkle Tree and writes the output to a text file named “merkle.tree”. It takes the input from the command line. The leaf nodes in the input are enclosed in double-quotes separated by commas. This file imports sys and hashlib. It has the following components:

● MerkleTreeNode: This class is used to create the nodes of the Merkle tree. It has 5 attributes:

  ○ left_child - points to left child of the current node

  ○ right_child - points to right child of the current node

  ○ parentNode - points to the parent node of the current node

  ○ data - contains the original data

  ○ hashValue - contains the SHA256 hash of the data 

● buildMerkleTree(): This function is called to build the Merkle tree. The leaf nodes are fed as input and a binary tree is constructed in a bottom-up fashion. It first pairs up the leaf nodes. Hashes of the leaf nodes are concatenated and hashed again to find the parent node. This process is continued for all the nodes until a single root hash is computed. If a node is found to not have a pair, its hash is appended to the root.

● writeMerkleTree(): This function takes into input the root of the Merkle Tree and writes the tree to the output file.
   
 2. checkinclusion.py: This module verifies whether the given data is included in the Merkle Tree. If it is present then it outputs “Yes” along with the proof of inclusion. If the data is not present, the program outputs “No”. This module imports buildmtree.py to construct the tree. It has the following components:

● findLeaf(): This function takes the tree and the input data as arguments. It returns the node where the data is found. Null is returned if data is not present in the tree. It calls itself recursively to search the left and right subtrees.

● constructProof(): This function returns the proof of inclusion if the data is present in the tree. The hash of the sibling of the leaf node is added to the list. Then the hash of the sibling of the parent node is added to the list. This process is continued until the root node is reached. The root hash is appended to the list at last.

3. checkconsistency.py: It takes in two lists as input and checks whether the second list is a proper subset and an extension of the first list. If they are consistent, the program outputs “Yes” along with the consistency proof. If not, the program outputs “No”. It also writes the two Merkle trees to an output text file “merkle.trees”. This module imports buildmtree.py and checkInclusion.py. It has the following components:

● nodeExists(): This function takes in input the tree and data as arguments and returns the node where the data is present. If not, null is returned.

● getHashValue(): This function returns the SHA256 hash of the argument.

● checkConsistency(): It first checks if the first input list is a proper subset of the
second list. If not, an empty list is returned. If it is, consistency proof is constructed as follows:

  ○ We first check if the root hash of the first Merkle tree is present in the second Merkle tree. If it is, then the sibling hash value is found and added to the output list. We then compute its parent and then repeat the process until the root of the second tree is reached. This will give the list of hashes of the intermediate nodes and the root hashes needed to validate.

  ○ If the root hash of the first Merkle tree is not present in the second Merkle tree, then we store the left child of the first Merkle tree. We then compute the combined hash of the right child of the first Merkle tree and its sibling found in the second Merkle tree. We then follow the procedure mentioned in the previous step to generate the consistency proof.

 
