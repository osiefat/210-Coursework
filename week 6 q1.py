class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
 
 
def in_order(tree):
    tree1=tree # Set tree1 to root of binary tree
    stack1=[] # set up the stack
    end=0 #end of sequence
    while end!=None:#is a pointer, keeping track of your position in the tree
        if tree1!=None:# Reach the left node
            stack1.append(tree1) # end placed to node on stack, giving the location in the stack            
            tree1 = tree1.left # before traversing the node's left subtree
        else: #goes back to the top of the stack but however if the stack is empty you are done
            if(len(stack1)>0):
                tree1=stack1.pop()#returns the last items in the stack
                print(tree1.value)
                tree1 = tree1.right # finished the left side of the tree branch,  now its time for the right side 
           
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t) # call the function
