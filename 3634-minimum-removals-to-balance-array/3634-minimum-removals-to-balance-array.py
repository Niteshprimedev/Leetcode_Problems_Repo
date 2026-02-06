class Solution:
    def minRemoval(self, A: List[int], k: int) -> int:
        A.sort()
        i = 0
        for j, a in enumerate(A):
            i += a > A[i] * k
        return i
        