class BSTNode:
    def __init__(self, data: int = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.deleted = None
    def is_empty(self):
        if self.root is None:
            return True
        return False
    def insert(self, data):
        new_node = BSTNode(data)
        if self.root is None:
            self.root = new_node
        cur = self.root
        while True:
            if data < cur.data:
                if cur.left is None:
                    cur.left = new_node
                    return
                cur = cur.left
            elif data > cur.data:
                if cur.right is None:
                    cur.right = new_node
                    return
                cur = cur.right
            else:
                return
        
    def preorder(self):
        def _pre(node):
            if node is None:
                return
            print("-> " + str(node.data), end=" ")
            _pre(node.left)
            _pre(node.right)
        _pre(self.root)
    
    def is_empty(self):
        if self.root is None:
            return True
        return False
    
    def inorder(self):
        def _in(node):
            if node is None:
                return
            _in(node.left)
            print("-> " + str(node.data),end=" ")
            _in(node.right)
        _in(self.root)
    
    def postorder(self):
        def _post(node):
            if node is None:
                return
            _post(node.left)
            _post(node.right)
            print("-> " + str(node.data),end=" ")
        _post(self.root)

    def traverse(self):
        if self.root is None:
            print("This is an empty binary search tree.")
            return
        print("Preorder: ",end="")
        self.preorder()
        print()
        print("Inorder: ",end="")
        self.inorder()
        print()
        print("Postorder: ",end="")
        self.postorder()
        print()

    def find_min(self):
        if self.root is None:
            return None
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        return cur.data
    
    def find_max(self):
        if self.root is None:
            return None
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur.data
    
    def delete(self, data):
        self.deleted = None
        self.root = self._delete(self.root, data)
        if self.deleted is None:
            print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
        return self.deleted
    
    def _delete(self, now, data):
        if now is None:
            return None
        if data < now.data:
            now.left = self._delete(now.left, data)
            return now
        if data > now.data:
            now.right = self._delete(now.right, data)
            return now
        
        self.deleted = now.data
        if now.left is None and now.right is None:
            return None
        if now.right is None:
            return now.left
        if now.left is None:
            return now.right
        max_left = self._max_node(now.left)
        now.data = max_left.data
        now.left = self._delete(now.left, max_left.data)
        return now
        
    def _max_node(self, node):
        cur = node
        while cur.right is not None:
            cur = cur.right
        return cur


def main():
  my_bst = BST()
  while 1:
    text = input()
    if text == "Done":
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse()

main()