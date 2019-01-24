from stack import Stack
def reverse(s): # Reverses a string using the stack
    n = Stack()
    for x in s:
        n.push(x)
    result = ""
    while n.size > 0:
        result += str(n.pop())
    return result 

def test_reverse():
    x = input("Enter a string to be reversed: ")
    print("Before: {}".format(x))
    y = reverse(x)
    print("After: {}".format(y))

#test_reverse()

def eval_postfix(postfix_str):
    stk = Stack()
    for c in postfix_str:
        if  c =='+' or c=='-' or c=='*' or c=='/':
            operand_right = stk.pop()
            operand_left = stk.pop()
            result = None
            if c =='+':
                result = operand_left + operand_right
            elif c=='-':
                result = operand_left - operand_right
            elif c=='*': 
                result = operand_left * operand_right
            else:
                result = operand_left / operand_right
            stk.push(result)
        else:
            #Pushes any numbers to the stack
            stk.push(float(c))
    return stk.pop() #Should be left w/ a num that can be returned as the answer 

def test_eval_postfix():
    x = input("Enter a postfix expression to be evaluated: ")
    print(eval_postfix(x))

test_eval_postfix()