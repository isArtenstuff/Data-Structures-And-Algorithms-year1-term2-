class BSTNode:
    def __init__(self, data: int = None):
        self.data = data
        self.left = None
        self.right = None


def main():
    data = int(input())
    p_new = BSTNode(data)
    print(p_new.data)
    print(p_new.left)
    print(p_new.right)
main()