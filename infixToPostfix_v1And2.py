"""Stack"""
class ArrayStack:
    """Stack"""
    def __init__(self):
        self.size = 0
        self.data = []
    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
                    pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self):
        if (self.size):
            self.size -= 1
            return self.data.pop()
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None
    def is_empty(self):
        return self.size == 0
    def get_stack_top(self):
        if (self.size):
            return self.data[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None
    def get_size(self):
        return self.size
    def print_stack(self):
        print(f"{self.data}")

"""Infix to Postfix"""
inp = input()
def infixToPostfix(expression: str) -> str:
    precedance = {"+" : 1, "-" : 1, "*" : 2, "/" : 2}
    postfix = ""
    stack = ArrayStack()

    for i in expression:
        if i.isalnum():
            postfix += i
        
        elif i == "(":
            stack.push(i)
        
        elif i == ")":
            while (not stack.is_empty() and stack.get_stack_top() != "("):
                postfix += stack.pop()
            if stack.get_stack_top() == "(":
                stack.pop()
        
        elif i in precedance:
            while (not stack.is_empty()
                   and stack.get_stack_top() != "("
                   and precedance.get(stack.get_stack_top(), 0) >= precedance[i]):
                postfix += stack.pop()
            
            stack.push(i)
        
        else:
            continue

    while not stack.is_empty():
        postfix += stack.pop()

    return postfix

print(infixToPostfix(inp))