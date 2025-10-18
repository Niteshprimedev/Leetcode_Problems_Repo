class FindSumPairs {
    private final HashMap<Integer, Integer> nums1Map = new HashMap<>();
    private final HashMap<Integer, Integer> nums2Map = new HashMap<>();
    private int[] nums2Arr = new int[10];

    public FindSumPairs(int[] nums1, int[] nums2) {
        this.nums2Arr = nums2;

        for(int num : nums1){
            nums1Map.put(num, nums1Map.getOrDefault(num, 0) + 1);
        }
        
        for(int num : nums2){
            nums2Map.put(num, nums2Map.getOrDefault(num, 0) + 1);
        }
    }
    
    public void add(int index, int val) {
        nums2Map.put(nums2Arr[index], nums2Map.get(nums2Arr[index]) - 1);
        nums2Arr[index] += val;

        nums2Map.put(nums2Arr[index], nums2Map.getOrDefault(nums2Arr[index], 0) + 1);
    }
    
    public int count(int tot) {
        int totalPairsCount = 0;

        for(Map.Entry<Integer, Integer> entry : nums1Map.entrySet()){
            int firstNum = entry.getKey();

            int secondNum = tot - firstNum;

            if(nums2Map.containsKey(secondNum) && nums2Map.get(secondNum) > 0){
                totalPairsCount += (entry.getValue() * nums2Map.get(secondNum));
            }
        }

        return totalPairsCount;
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs obj = new FindSumPairs(nums1, nums2);
 * obj.add(index,val);
 * int param_2 = obj.count(tot);
 */