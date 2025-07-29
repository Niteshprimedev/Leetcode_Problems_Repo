class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Solution 1:
		int n = nums.length;
		HashMap<Integer, Integer> numsElsMap = new HashMap<>();
		List<Integer> twoSumIndices = new ArrayList<>();
			
		for(int idx = 0; idx < n; idx++){
			int firstNum = nums[idx];
			int secondNum = target - firstNum;
			
			if(numsElsMap.containsKey(secondNum)){
				twoSumIndices.add(numsElsMap.get(secondNum));
				twoSumIndices.add(idx);
			}
			
			numsElsMap.put(firstNum, idx);
		}
		
		// return twoSumIndices;
		return twoSumIndices.stream().mapToInt(i -> i).toArray();
    }
}