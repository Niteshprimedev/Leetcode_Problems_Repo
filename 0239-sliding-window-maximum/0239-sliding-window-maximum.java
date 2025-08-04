class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
		int[] slidingWindowMaxs = new int[n - k + 1];
		Deque <Integer> queue = new ArrayDeque<>();
		
		int strtIdx = 0;
		int endIdx = 0;
		
		while (endIdx < nums.length){
			int currNum = nums[endIdx];
			
			while(!queue.isEmpty() && nums[queue.getLast()] <= currNum){
				queue.pollLast();
			}
			
			while(!queue.isEmpty() && (endIdx - queue.getFirst()) >= k){
				queue.pollFirst();
			}
			
			queue.offerLast(endIdx);
			
			if(endIdx - strtIdx + 1 == k){
				slidingWindowMaxs[strtIdx] = nums[queue.getFirst()];
				strtIdx += 1;
			}
			
			endIdx += 1;
		}
		
		return slidingWindowMaxs;
    }
}