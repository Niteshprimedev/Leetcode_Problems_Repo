class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1_chars_map = Counter(word1)
        word2_chars_map = Counter(word2)

        if len(word1_chars_map) != len(word2_chars_map):
            return False

        arr1 = []
        arr2 = []

        for key, value in word1_chars_map.items():
            if key not in word2_chars_map:
                return False
            
            arr1.append(value)
            arr2.append(word2_chars_map[key])
        
        arr1.sort()
        arr2.sort()

        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        
        return True