# Preorder - DLR

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


# Inorder - LDR

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
    while stack and node:
        if node:
            node = node.left
            stack.append(node)
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right

#Postorder -  LRD

def recursivePostorder(root, result):
    if not root:
        return
    recursivePostorder(root.left, result)
    recursivePostorder(root.right,result)
    result.append(root.data)


def PostorderIterative(root,result):
    if not root:
        return
    visited = set()
    stack = []
    node = root
    while stack and node:
        if node:
            stack.append(node)
            node = node.left

        else:
            node = stack.pop()
            if node.right and node.right not in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None


