class Pair{
    public int val;
    public int idx;

    public Pair(int val, int idx) {
        this.val = val;
        this.idx = idx;
    }
};

class Solution { 
    // 8 6 4 12 3 2 1 1 , k=3 || max = 8 , 12 , 12  , 12 ,  3 ,2 
    // i = 7  
    // pq = (8,0) (6,1) (4,2) => (12,3) (6,1) (4,2) (3,4) (2,5) => (3,4) (2,5) (1,6) => (2,5) (1,6) (1,7) 
    // while(!pq.isEmpty() && i-pq.peek()[1]>=k) {pq.poll();}


    public int[] maxSlidingWindow(int[] nums, int k) { 
        int n = nums.length;
        int[] ans = new int[n - k + 1];
        PriorityQueue<Pair> pq = new PriorityQueue<>((p1, p2) -> p2.val - p1.val); // desc sorting
        for(int i=0;i<nums.length;i++){
            pq.add(new Pair(nums[i],i));
            while(!pq.isEmpty() && i-pq.peek().idx >=k ){
                pq.poll();
            }
            if(i>=k-1){
                ans[i-k+1] = pq.peek().val;
            }
            // System.out.println(Arrays.toString(ans));
        }
        return ans;
    }
}