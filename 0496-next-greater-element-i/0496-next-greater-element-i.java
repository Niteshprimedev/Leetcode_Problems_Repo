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

        int idx = 0;
        for(int num : nums1){
            if(nums2GreaterElsMap.containsKey(num)){
                nextGreaterEls[idx++] = nums2GreaterElsMap.get(num);
            }
        }
		
		return nextGreaterEls;
    }
}