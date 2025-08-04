class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> numsElsSet = new HashSet<>();
		int longestConsSeq = 0;
		
		for(int idx = 0; idx < nums.length; idx++){
			numsElsSet.add(nums[idx]);
		}
		
		for(int num : nums){
			int prevNum = num - 1;
			if(!numsElsSet.contains(prevNum)){
				int newLongestConsSeq = 0;
                int currNum = num;
				while(numsElsSet.contains(currNum)){
					numsElsSet.remove(currNum);
					currNum += 1;
					newLongestConsSeq += 1;
				}
				
				longestConsSeq = Math.max(longestConsSeq, newLongestConsSeq);
			}
		}
		
		return longestConsSeq;
    }
}