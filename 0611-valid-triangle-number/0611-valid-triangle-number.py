'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        def binary_search(strtIdx, endIdx, strtVal, midVal):
            low = strtIdx
            high = endIdx
            valid_idx = endIdx + 1

            while(low <= high):
                mid = low + (high - low) // 2
                endVal = nums[mid]

                if (strtVal + midVal) > endVal and (midVal + endVal) > strtVal and (strtVal + endVal) > midVal:
                    high = mid - 1
                    valid_idx = mid
                else:
                    low = mid + 1
            
            return (endIdx + 1) - valid_idx
        
        total_valid_triplets = 0
        # print(nums)

        for strt in range(n - 2):
            if(nums[strt] == 0):
                continue

            mid = strt + 1
            
            # all valid triplets;
            while(mid < n - 1):
                
                total_counts = binary_search(mid + 1, n - 1, nums[strt], nums[mid])

                print(total_counts, strt, mid , nums[strt], nums[mid])
                total_valid_triplets += ((total_counts + 1) * total_counts // 2)

                # if total_counts <= 0:
                #     end -= 1
                # else:
                #     break

                mid += 1
        
        return total_valid_triplets

'''

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        L = len(nums)
        # c < (a+b)
        for i in range(L-1,1,-1):
            c = nums[i]
            start = 0
            end = i-1
            while start < end:
                if nums[start] + nums[end] > c:
                    ans += end - start
                    end -= 1
                elif nums[start] + nums[end] <= c:
                    start += 1
        return ans       
