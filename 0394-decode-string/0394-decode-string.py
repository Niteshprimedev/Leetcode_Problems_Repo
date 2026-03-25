'''
class Solution:
    def decodeString(self, s: str) -> str:
        # Logic: Decode the number first, and solve the 
        # subproblem using recursion => subproblem = [abc]
        # return the index and the decoded_parts as the subproblem solution;
        # Note: your recursive function would be similar to your while loop
        # but you need to resolve the deeply nested brackets;

        decoded_str = ''

        def decode_str_parts(curr_idx):
            parenthe_stack = [s[curr_idx]]

            decoded_str_parts = ''
            curr_idx += 1
            curr_str = ''

            while len(parenthe_stack) and curr_idx < len(s):
                curr_char = s[curr_idx]
                idx = curr_idx

                # solve the subproblem of one bracket: [abc]
                if curr_char == '[':
                    curr_str, idx = decode_str_parts(curr_idx)
                # Get the number to multiply or repeat the 
                # str in the bracket and solve the subproblem of one bracket: [abc]
                elif curr_char in '0123456789':
                    num_end_idx = curr_idx

                    while num_end_idx < len(s) and s[num_end_idx] in '0123456789':
                        num_end_idx += 1
                    
                    curr_num = int(s[curr_idx:num_end_idx])

                    # recursive function call;
                    curr_str, idx = decode_str_parts(num_end_idx)
                    curr_str = curr_str * curr_num
                elif curr_char == ']':
                    parenthe_stack.pop()
                    curr_str = ''
                    # continue the loop to avoid incrementing indices;
                    continue
                # else, no subproblem and only char then append directly
                else:
                    curr_str = curr_char
                
                # decode the str_parts for this subproblem
                decoded_str_parts += curr_str
                curr_idx = idx
                curr_idx += 1
            
            # return the decoded_parts of subproblem and index;
            # till where the subproblem is solved
            return (decoded_str_parts, curr_idx)
        
        idx_i = 0
        curr_str = ''

        while idx_i < len(s):
            curr_char = s[idx_i]
            idx = idx_i

            # solve the subproblem of one bracket: [abc]
            if curr_char == '[':
                # recursive function call;
                curr_str, idx = decode_str_parts(idx_i)
            # Get the number to multiply or repeat the 
            # str in the bracket and solve the subproblem of one bracket: [abc]
            elif curr_char in '0123456789':
                num_end_idx = idx_i

                while num_end_idx < len(s) and s[num_end_idx] in '0123456789':
                    num_end_idx += 1

                curr_num = int(s[idx_i:num_end_idx])

                # recursive function call;
                curr_str, idx = decode_str_parts(num_end_idx)
                curr_str = curr_str * curr_num
            # else, no subproblem and only char then append directly
            else:
                curr_str = curr_char
            
            decoded_str += curr_str
            idx_i = idx
            idx_i += 1
        
        return decoded_str
'''

'''
# Solution 2
class Solution:
    def decodeString(self, s: str) -> str:
        decoded_str = ''  # Final output string
        
        def decode_str_parts(curr_idx):
            """
            Recursive helper function to decode parts of the string.
            Returns a tuple of (decoded_substring, ending_index)
            
            Args:
                curr_idx: Current index in the string we're processing
            """
            parenthe_stack = [s[curr_idx]]  # Stack to track opening/closing brackets
            
            decoded_str_parts = ''  # Result for this recursion level
            curr_idx += 1  # Move past the opening bracket
            curr_str = ''  # Current string chunk being processed
            
            # Continue until all brackets at this level are closed or string ends
            while len(parenthe_stack) and curr_idx < len(s):
                curr_char = s[curr_idx]
                idx = curr_idx
                
                if curr_char == '[':
                    # Found a nested bracket - recursively decode its contents
                    curr_str, idx = decode_str_parts(curr_idx)
                elif curr_char in '0123456789':
                    # Found a number - extract the full number
                    num_end_idx = curr_idx
                    
                    # Find the end of the number
                    while num_end_idx < len(s) and s[num_end_idx] in '0123456789':
                        num_end_idx += 1
                    
                    # Convert the numeric string to integer
                    curr_num = int(s[curr_idx:num_end_idx])
                    
                    # Process the part that should be repeated
                    curr_str, idx = decode_str_parts(num_end_idx)
                    # Repeat the string according to the number
                    curr_str = curr_str * curr_num
                elif curr_char == ']':
                    # Closing bracket - end this recursion level
                    parenthe_stack.pop()
                    curr_str = ''
                    continue
                else:
                    # Regular character - add it directly
                    curr_str = curr_char
                
                # Add the processed string chunk to our result
                decoded_str_parts += curr_str
                curr_idx = idx
                curr_idx += 1  # Move to the next character
            
            # Return the decoded string for this level and the ending index
            return (decoded_str_parts, curr_idx)
        
        idx_i = 0  # Start from the beginning of the string
        curr_str = ''  # Current string chunk being processed
        
        # Process the entire input string
        while idx_i < len(s):
            curr_char = s[idx_i]
            idx = idx_i
            
            if curr_char == '[':
                # Start of a new group - recursively decode it
                curr_str, idx = decode_str_parts(idx_i)
            elif curr_char in '0123456789':
                # Found a number - extract the full number
                num_end_idx = idx_i
                
                # Find the end of the number
                while num_end_idx < len(s) and s[num_end_idx] in '0123456789':
                    num_end_idx += 1
                
                # Convert the numeric string to integer
                curr_num = int(s[idx_i:num_end_idx])
                
                # Process the part that should be repeated
                curr_str, idx = decode_str_parts(num_end_idx)
                # Repeat the string according to the number
                curr_str = curr_str * curr_num
            else:
                # Regular character - add it directly
                curr_str = curr_char
            
            # Add the processed string to our final result
            decoded_str += curr_str
            idx_i = idx
            idx_i += 1  # Move to the next character
        
        return decoded_str
'''

# Solution 3:
# Meta Prep Time Practice
# Moved curr_str inside the while loop instead of global variable

class Solution:
    def decodeString(self, s: str) -> str:
        decoded_str = ''  # Final output string
        
        def decode_str_parts(curr_idx):
            """
            Recursive helper function to decode parts of the string.
            Returns a tuple of (decoded_substring, ending_index)
            
            Args:
                curr_idx: Current index in the string we're processing
            """
            parenthe_stack = [s[curr_idx]]  # Stack to track opening/closing brackets
            
            decoded_str_parts = ''  # Result for this recursion level
            curr_idx += 1  # Move past the opening bracket
            curr_str = ''  # Current string chunk being processed
            
            # Continue until all brackets at this level are closed or string ends
            while len(parenthe_stack) and curr_idx < len(s):
                curr_char = s[curr_idx]
                idx = curr_idx
                
                if curr_char == '[':
                    # Found a nested bracket - recursively decode its contents
                    curr_str, idx = decode_str_parts(curr_idx)
                elif curr_char in '0123456789':
                    # Found a number - extract the full number
                    num_end_idx = curr_idx
                    
                    # Find the end of the number
                    while num_end_idx < len(s) and s[num_end_idx] in '0123456789':
                        num_end_idx += 1
                    
                    # Convert the numeric string to integer
                    curr_num = int(s[curr_idx:num_end_idx])
                    
                    # Process the part that should be repeated
                    curr_str, idx = decode_str_parts(num_end_idx)
                    # Repeat the string according to the number
                    curr_str = curr_str * curr_num
                elif curr_char == ']':
                    # Closing bracket - end this recursion level
                    parenthe_stack.pop()
                    curr_str = ''
                    continue
                else:
                    # Regular character - add it directly
                    curr_str = curr_char
                
                # Add the processed string chunk to our result
                decoded_str_parts += curr_str
                curr_idx = idx
                curr_idx += 1  # Move to the next character
            
            # Return the decoded string for this level and the ending index
            return (decoded_str_parts, curr_idx)
        
        idx_i = 0  # Start from the beginning of the string
        
        # Process the entire input string
        while idx_i < len(s):
            curr_char = s[idx_i]
            idx = idx_i
            curr_str = ''  # Current string chunk being processed
            
            if curr_char == '[':
                # Start of a new group - recursively decode it
                curr_str, idx = decode_str_parts(idx_i)
            elif curr_char in '0123456789':
                # Found a number - extract the full number
                num_end_idx = idx_i
                
                # Find the end of the number
                while num_end_idx < len(s) and s[num_end_idx] in '0123456789':
                    num_end_idx += 1
                
                # Convert the numeric string to integer
                curr_num = int(s[idx_i:num_end_idx])
                
                # Process the part that should be repeated
                curr_str, idx = decode_str_parts(num_end_idx)
                # Repeat the string according to the number
                curr_str = curr_str * curr_num
            else:
                # Regular character - add it directly
                curr_str = curr_char
            
            # Add the processed string to our final result
            decoded_str += curr_str
            idx_i = idx
            idx_i += 1  # Move to the next character
        
        return decoded_str