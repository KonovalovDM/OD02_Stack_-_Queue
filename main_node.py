class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функция для добавления нового узла
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Пример использования
root = Node(72)
root = insert(root, 52)
root = insert(root, 42)
root = insert(root, 64)
root = insert(root, 94)
root = insert(root, 81)
root = insert(root, 106)
