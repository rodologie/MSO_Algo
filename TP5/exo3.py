class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(expression):
    # base case: expression is a single variable or value
    if len(expression) == 1:
        return Node(expression)
    
    # find the first occurrence of the ternary operator "?"
    i = 0
    while i < len(expression):
        if expression[i] == "?":
            break
        i += 1
    
    # create a node for the condition and recursively build the left and right subtrees
    root = Node(expression[:i])
    root.left = build_tree(expression[i+1:expression.find(":", i)])
    root.right = build_tree(expression[expression.find(":", i)+1:])
    
    return root

expression = "a?b:c"
root = build_tree(expression)
print(root)