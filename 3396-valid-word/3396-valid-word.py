class Solution:
    def isValid(self, word: str) -> bool:
        '''
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
        '''

        '''
        # Solution to check only if it contains a vowel or consonant 
        # or not?
        # Implementation and Programming Skill

        # Contains a min of 3 chars
        if len(word) >= 3:
            is_vowel_present = False
            is_cons_present = False
            for char in word:
                if char in ('aeiouAEIOU'):
                    is_vowel_present = True
                elif char.isalnum() and char not in ('0123456789'):
                    is_cons_present = True
                elif not char.isalnum():
                    return False
            
            if is_vowel_present and is_cons_present:
                return True
                
        return False
        '''

        # Solution to check only if it contains a vowel or consonant 
        # or not?
        # Implementation and Programming Skill

        # Contains a min of 3 chars
        if len(word) >= 3:
            is_vowel_present = False
            is_cons_present = False
            for char in word:
                if char in ('aeiouAEIOU'):
                    is_vowel_present = True
                elif char.isalpha():
                    is_cons_present = True
                elif not char.isalnum():
                    return False
            
            if is_vowel_present and is_cons_present:
                return True
                
        return False