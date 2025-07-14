class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Edge Case
        if k > len(s):
            return False # we can't construct k palindromes 

        str_letters_freq_map = defaultdict(int)
        total_odd_letters_count = 0

        for char in s:
            str_letters_freq_map[char] += 1
        
        for letter_key, letter_val in str_letters_freq_map.items():
            if letter_val % 2 == 1:
                total_odd_letters_count += 1
        
        if total_odd_letters_count <= k:
            return True
        
        return False

