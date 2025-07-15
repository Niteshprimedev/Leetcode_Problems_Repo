class Solution:
    def isValid(self, word: str) -> bool:
        # Implementation and Programming Skill

        # Contains a min of 3 chars
        if len(word) >= 3:
            valid_word = [False, False]
            for char in word:
                if char in ('aeiouAEIOU'):
                    valid_word[0] = True
                elif char.isalnum() and char not in ('0123456789'):
                    valid_word[1] = True
                elif not char.isalnum():
                    return False
            
            for is_valid in valid_word:
                if not is_valid:
                    return False
                
            return True

        return False