class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        int n = nums.length;
		List<List<Integer>> allUniqueQuadruplets = new ArrayList<>();

		Arrays.sort(nums);

		for(int firstIdx = 0; firstIdx < n; firstIdx++){
			int firstNum = nums[firstIdx];

			if(firstIdx > 0 && nums[firstIdx - 1] == firstNum){
				continue;
			}

			for(int secondIdx = firstIdx + 1; secondIdx < n; secondIdx++){
				int secondNum = nums[secondIdx];
				
				if((secondIdx - 1) > firstIdx && nums[secondIdx - 1] == secondNum){
					continue;
				}
				
				int thirdIdx = secondIdx + 1;
				int forthIdx = n - 1;

				while(thirdIdx < forthIdx){
					int thirdNum = nums[thirdIdx];
					int forthNum = nums[forthIdx];

					long tripletsSum = (long)firstNum + secondNum + thirdNum + forthNum;

                    // System.out.println(tripletsSum);
					if(tripletsSum == target){
						allUniqueQuadruplets.add(Arrays.asList(firstNum, secondNum, thirdNum, forthNum));

						thirdIdx += 1;
						forthIdx -= 1;

						while(thirdIdx < forthIdx && nums[thirdIdx] == thirdNum){
							thirdIdx += 1;
						}
					}
					else if(tripletsSum < target){
						thirdIdx += 1;
					}
					else{
						forthIdx -= 1;
					}
				}
			}
		}
		
		return allUniqueQuadruplets;
    }
}