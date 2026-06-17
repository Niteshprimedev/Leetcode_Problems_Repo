class Solution:
    def processStr(self, s: str, k: int) -> str:

        length = 0

        for char in s:
            if char.isalpha():
                length += 1
            elif char == '*':
                if length > 0:
                    length -= 1
            elif char == '#':
                length *= 2
            elif char == '%':
                pass

        if k >= length:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char.isalpha():
                if k == length - 1:
                    return char
                length -= 1
            elif char == '*':
                length += 1
            elif char == '#':
                half = length // 2
                if k >= half:
                    k -= half
                length = half
            elif char == '%':
                k = length - 1 - k

        return '.'