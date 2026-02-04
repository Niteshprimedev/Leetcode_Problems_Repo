class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:

        l = p = q = 0
        n, ans = len(nums), -inf
        tally, prevLeft = nums[0], inf
        
        for r, (left, rght) in enumerate(pairwise(nums)):
            
            if left > rght:                     # states 1) and 2)
                tally+= rght

                if prevLeft > left: continue    # state 1)

                p = r                           # state 2)
                while (l < q) or (l < p - 1 and nums[l] < 0):
                    tally-= nums[l]
                    l+= 1

            elif left < rght:                   # states 3) and 4)
                tally+= rght

                if prevLeft > left: q = r       # state 4)
                if l < p < q <= r and tally > ans:
                    ans = tally

            elif left == rght:                  # state 5)
                tally, l = rght, r + 1 

            prevLeft = left

        return ans