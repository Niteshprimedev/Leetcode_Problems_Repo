class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Create a is_palindrome function that
        # checks if the string is still a palindrome
        # or not, if left_char is deleted or right_char is deleted
        def is_palindrome(left_idx, right_idx):
            while left_idx < right_idx:
                if s[left_idx] != s[right_idx]:
                    return False
                left_idx += 1
                right_idx -= 1
            return True
        
        left_idx = 0
        right_idx = len(s) - 1

        # check if the string is a palindrome
        # without deleting any char
        while left_idx < right_idx:
            if s[left_idx] != s[right_idx]:
                # if string is not a palindrome at any point
                # try checking after deleting the left_char
                skip_left_char = is_palindrome(left_idx + 1, right_idx) # greedily delete left char
                # try checking after deleting the right_char
                skip_right_char = is_palindrome(left_idx, right_idx - 1) # greedily delete right char

                # Now, it's time to return the palindromic check
                # cause we already greedily checked by deleting the left_char
                # and then deleting the right_char
                return (skip_left_char or skip_right_char)
                
            left_idx += 1
            right_idx -= 1
        return True