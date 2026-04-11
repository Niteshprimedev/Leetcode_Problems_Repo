class Solution {
    private int calcMinDistance(int idxK, Deque<Integer> hashValue){
        int idxI = hashValue.poll();
        int idxJ = hashValue.poll();

        int currMinDistance = Math.abs(idxI - idxJ) + Math.abs(idxJ - idxK) + Math.abs(idxK - idxI);

        hashValue.offer(idxI);
        hashValue.offer(idxJ);

        return currMinDistance;
    }

    public int minimumDistance(int[] nums) {
        /*
        int n = nums.length;
        HashMap<Integer, Integer> leftMap = new HashMap<>();
        HashMap<Integer, List<Integer>> rightMap = new HashMap<>();

        leftMap.put(nums[0], 0);

        for(int i = 2; i < n; i++){
            rightMap.putIfAbsent(nums[i], new ArrayList<>());
            rightMap.put(nums[i], rightMap.get(nums[i]).add(i));
        }

        for(int j = 1; j < n - 1; j++){
            int elJ = nums[j];

            if(leftMap.contains(elJ) && rightMap.contains(elJ)){
                int elI = leftMap.get(elJ);
                List<Integer> hashValue = rightMap.get(elJ);

                int elK = lowerBound(hashValue, j);
            }

            leftMap.put(elJ, j);
        }

        return minDistance == Integer.MAX_VALUE ? -1 : minDistance;
        */

        // Meta Prep Time Practice:
        int minDistance = Integer.MAX_VALUE;
        int n = nums.length;
        Map<Integer, Deque<Integer>> map = new HashMap<>();

        for(int idxI = 0; idxI < n; idxI++){
            map.putIfAbsent(nums[idxI], new ArrayDeque<>());
            Deque<Integer> hashValue = map.get(nums[idxI]);

            // System.out.println(nums[idxI] + " " + hashValue.toString());

            if(hashValue.size() == 2){
                int newMinDistance = calcMinDistance(idxI, hashValue);
                minDistance = Math.min(minDistance, newMinDistance);
                hashValue.poll();
            }

            hashValue.offer(idxI);
            map.put(nums[idxI], hashValue);
        }

        return minDistance == Integer.MAX_VALUE ? -1 : minDistance;
    }
}