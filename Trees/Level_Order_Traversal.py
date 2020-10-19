'''Visit the root
While traversing L, keep all the elements l+1 in queue
Go the next level and visit all the nodes
Repeat until all the levels are completed'''
def levelOrderTraversal(root,result):
    if root is None:
        return
    q = Queue.Queue()
    q.put(root)
    node = None

    while not q.isempty():
        node = q.get()
        result.append(node.getData())
        if node.getLeft() is not None:
            q.put(node.getLeft())
        if node.getRight is not None:
            q.put(node.getRight())