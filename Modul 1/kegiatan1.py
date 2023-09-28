def minus(left, right):
    return left - right

def mult(left, right):
    return left * right

def div(left, right):
    if right != 0:
        return left / right
    else:
        return "ERROR"
    
def tree(expression):
    if isinstance(expression, tuple):
        left, operator, right = expression
        if operator == '-':
            return minus(tree(left), tree(right))
        if operator == '*':
            return mult(tree(left), tree(right))
        if operator == '/':
            return div(tree(left), tree(right))
        if operator == '+':
            return tree(left) + tree(right)
    else:
        return expression
    
expression_tree = ((2, '+', 3), '*', (5, '-', 1))
result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi:", result)