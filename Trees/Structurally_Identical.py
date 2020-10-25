def StructuralComparison(root1,root2):
    node1,node2= root1,root2
    if (not node1.left) and (not node1.right) and (not node2.left) and (not node2.right) and node1.data == node2.data:
        return True
    if node1.data!=node2.data or (node1.left and not node2.left) or (node1.right and not node2.right) or (not node1.left and node2.left)or \
        (not node1.right and  node2.right):
        return False
    left = StructuralComparison(node1.left,node2.left) if node1.left and node2.left else True
    right = StructuralComparison(node1.right,node2.right) if node1.right and node2.right else True
    return left,right

