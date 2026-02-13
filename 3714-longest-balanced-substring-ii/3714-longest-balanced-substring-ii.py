'''
class Solution:
    def longestBalanced(self, s: str) -> int:
        def isBalanced(freq):
            counts = [f for f in freq if f > 0]
            return len(counts) and max(counts) == min(counts)
            
        n = len(s)

        freq = [0] * 26
        left = 0

        long_substr = 0

        for right in range(n):
            c_idx = ord(s[right]) - ord('a')

            freq[c_idx] += 1

            while not isBalanced(freq) and left <= right:
                l_idx = ord(s[left]) - ord('a')
                freq[l_idx] -= 1
                
                left += 1

            if isBalanced(freq):
                long_substr = max(long_substr, right - left + 1)

        return long_substr
        '''

class Solution:
    def longestBalanced(self, S: str) -> int:
        N = len(S)
        P = [[0, 0, 0]]
        for c in S:
            P.append(P[-1][:])
            P[-1]["abc".index(c)] += 1

        ans = 0
        first = {}
        for i, (a, b, c) in enumerate(P):
            for key in [
                ("abc", a - b, a - c),
                ("ab", a - b, c),
                ("bc", b - c, a),
                ("ca", c - a, b),
                ("a", b, c),
                ("b", c, a),
                ("c", a, b),
            ]:
                ans = max(ans, i - first.get(key, i))
                first.setdefault(key, i)

        return ans