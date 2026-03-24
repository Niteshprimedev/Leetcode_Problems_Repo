class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        VOWELS = set('aeiou')

        chars_list = list(s)

        left_idx = 0
        right_idx = len(chars_list) - 1

        while(left_idx < right_idx):
            left_char = chars_list[left_idx]
            right_char = chars_list[right_idx]

            while left_idx < right_idx and left_char.lower() not in VOWELS:
                left_idx += 1
                left_char = chars_list[left_idx]

            while right_idx > left_idx and right_char.lower() not in VOWELS:
                right_idx -= 1
                right_char = chars_list[right_idx]
            
            # Swap the Vowels: at left_idx & right_idx
            chars_list[left_idx], chars_list[right_idx] = chars_list[right_idx], chars_list[left_idx]

            left_idx += 1
            right_idx -= 1
            
            # print(left_idx, right_idx, chars_list)
            
        return ''.join(chars_list)
        '''

        # Meta Prep Time Practice
        # Solution using Conditionals and While loop;
        VOWELS = set('aeiou')

        chars_list = list(s)

        left_idx = 0
        right_idx = len(chars_list) - 1

        while(left_idx < right_idx):
            left_char = chars_list[left_idx]
            right_char = chars_list[right_idx]

            if left_char.lower() not in VOWELS:
                left_idx += 1
            elif right_char.lower() not in VOWELS:
                right_idx -= 1
            else:
                # Swap the Vowels: at left_idx & right_idx
                chars_list[left_idx], chars_list[right_idx] = chars_list[right_idx], chars_list[left_idx]
                left_idx += 1
                right_idx -= 1
            
            # print(left_idx, right_idx, chars_list)
            
        return ''.join(chars_list)
