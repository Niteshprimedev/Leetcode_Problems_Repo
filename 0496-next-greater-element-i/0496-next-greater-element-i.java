class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        HashMap <Integer, Integer> nums2GreaterElsMap = new HashMap<>();

        int n = nums2.length;

        int[] nextGreaterEls = new int[nums1.length];
		
		Deque<Integer> nextGreaterStack = new ArrayDeque<>();
		
		for(int idx = n - 1; idx >= 0; idx--){
			int currEl = nums2[idx];
			
			while(!nextGreaterStack.isEmpty() && nextGreaterStack.peek() <= currEl){
				nextGreaterStack.pop();
			}
			
			if(!nextGreaterStack.isEmpty()){
				nums2GreaterElsMap.put(currEl, nextGreaterStack.peek());
			}
			else{
				nums2GreaterElsMap.put(currEl, -1);
			}
			
			nextGreaterStack.push(currEl);
		}

        // int idx = 0;
        // for(int num : nums1){
        //     // nums1 is a subset so no need of else & if;
        //     if(nums2GreaterElsMap.containsKey(num)){
        //         nextGreaterEls[idx++] = nums2GreaterElsMap.get(num);
        //     }
        // }

        // OR;
        int idx = 0;
        for(int num : nums1){
            // nums1 is a subset so no need of else & if;
            nextGreaterEls[idx++] = nums2GreaterElsMap.get(num);
        }
		
		return nextGreaterEls;

        // Dry Run:
        // nums2Map = {2: -1, 4: -1, 3: 4, 1: 3}
        // nums2Stack = []
        // nums2Stack = [2] => [] then 4 
        // numsStack = [4] => [4, 3] => [4, 3, 1]
        // nums1 => 4 in map => ans is -1,
        // nums1 => 1 in map => ans is 3
        // nums1 => 2 in map => ans is -1
    }
}