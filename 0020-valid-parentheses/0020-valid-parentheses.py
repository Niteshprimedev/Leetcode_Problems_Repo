class Solution:
    def isValid(self, s: str) -> bool:
        '''
        # During DSA Session 8 on May 25
        if (len(s) & 1):
            return False
            
        valid_parenthe_map = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        
        open_parenthe = '([{'
        open_parenthe_stack = []
        
        for parenthe in s:
            if parenthe in open_parenthe:
                open_parenthe_stack.append(parenthe)
            else:
                if (len(open_parenthe_stack) == 0):
                    return False
                    
                closed_parenthe = open_parenthe_stack.pop()
                
                if valid_parenthe_map[closed_parenthe] != parenthe:
                    return False
        
        if (len(open_parenthe_stack) > 0):
            return False
            
        return True
        '''

        # Solution by DK Sir DSA mentor:
        if(len(s) & 1):
            return False

        parenthe_stack = []

        for parenthe in s:
            if not parenthe_stack or parenthe in ("([{"):
                parenthe_stack.append(parenthe)
            elif parenthe == ')' and parenthe_stack[-1] == '(':
                parenthe_stack.pop()
            elif parenthe == ']' and parenthe_stack[-1] == '[':
                parenthe_stack.pop()
            elif parenthe == '}' and parenthe_stack[-1] == '{':
                parenthe_stack.pop()
            else:
                return False

        if len(parenthe_stack) > 0:
            return False
        
        return True

        # @To-Do: Try to solve this problem after this one:
        # Backtracking -> https://leetcode.com/problems/generate-parentheses/