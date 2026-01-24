"""
Docstring for stacks.reverse_stack

Input: st[] = [1, 2, 3, 4]
Output: [1, 2, 3, 4]

Recursive approach:
- remove elements from the stack until empty
- Once the stack is empty we are going back  in the recursion. 
- At each step, instead of placing the element back on top, we insert it at bottom of the stack
"""

def reverseStack(st):
    if not st:
        return
    top = st.pop()
    reverseStack(st)

