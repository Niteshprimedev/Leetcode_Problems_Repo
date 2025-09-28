class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # perimeter of a triangle:
        # p = a + b + c
        # valid Triangle Condition:
        # (a + b) > c and (b + c) > a and (c + a) > b
        # Note: If two smaller sides are bigger than largest side
        # then the condition (b + c) > a and (a + c) > b will always be true;
        n = len(nums)
        nums.sort()

        for i in range(n - 3, -1, -1):
            if(nums[i] + nums[i + 1] > nums[i + 2]):
                return nums[i] + nums[i + 1] + nums[i + 2]
        
        return 0






