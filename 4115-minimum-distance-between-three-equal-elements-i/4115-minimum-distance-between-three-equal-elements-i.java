class Solution {
    public int minimumDistance(int[] nums) {
        int n = nums.length;
        int minDistance = Integer.MAX_VALUE;
        
        for(int i = 0; i < n; i++){
            int elI = nums[i];
            HashMap<Integer, Integer> elsIdxMap = new HashMap<>();

            for(int j = n - 1; j > i; j--){
                int elJ = nums[j];

                if(elI == elJ && elsIdxMap.containsKey(elJ)){
                    int k = elsIdxMap.get(elJ);

                    int newMinDistance = Math.abs(i - j) + Math.abs(j - k) + Math.abs(i - k);
                    minDistance = Math.min(minDistance, newMinDistance);

                }
                
                elsIdxMap.put(elJ, j);
            }
        }

        return minDistance == Integer.MAX_VALUE ? -1 : minDistance;
    }
}