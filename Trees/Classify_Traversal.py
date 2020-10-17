# Preorder

def recursivePreorder(root,result):
    if not root:
        return
    result.append(root.data)
    recursivePreorder(root.left,result)
    recursivePreorder(root.right,result)


def preorderIterative(root,result):
    if not root:
        return
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right:
            stack.append(node.left)
        if node.left:
            stack.append(node.left)


# Inorder

def recursiveInorder(root,result):
    if not root:
        return
    recursiveInorder(root.left,result)
    result.append(root.data)
    recursiveInorder(root.right,result)


def InorderIterative(root,result):
    if not root:
        return
    stack = []
    node = root
    while stack:
