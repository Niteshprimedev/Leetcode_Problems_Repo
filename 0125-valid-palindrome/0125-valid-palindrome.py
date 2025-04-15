class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str_s = ''.join(filter(str.isalnum, s))

        # print(new_str_s)

        def check_palindrome(str, strt_idx, end_idx):
            if (strt_idx > end_idx):
                return True
            
            if (str[strt_idx] != str[end_idx]):
                return False
            
            strt_idx += 1
            end_idx -= 1

            is_str_palindrome = check_palindrome(str, strt_idx, end_idx)
            return is_str_palindrome

        return check_palindrome(new_str_s.lower(), 0, len(new_str_s) - 1)