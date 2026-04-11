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

        /*
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
        */

        /*
        // Solution 3:
        Map<Integer, int[]> map = new HashMap<>();

        int n = nums.length;
        int minDistance = Integer.MAX_VALUE;

        for(int idxI = 0; idxI < n; idxI++){
            if(!map.containsKey(nums[idxI])){
                map.put(nums[idxI], new int[]{-1, idxI});
            }
            else{
                int[] pair = map.get(nums[idxI]);
                int prev = pair[0];
                int second = pair[1];

                if(prev != -1){
                    int a = prev, b = second, c = idxI;

                    int newMinDistance = Math.abs(a - b) + Math.abs(b - c) + Math.abs(c - a);
                    minDistance = Math.min(minDistance, newMinDistance);
                }

                pair[0] = second;
                pair[1] = idxI;
            }
        }

        return minDistance == Integer.MAX_VALUE ? -1 : minDistance;
        */

        // ChatGPT Commented Code:
        // Solution 3: Track last two occurrences of each number
        Map<Integer, int[]> map = new HashMap<>();

        int n = nums.length;

        // Initialize min distance as max possible
        int minDistance = Integer.MAX_VALUE;

        for (int idxI = 0; idxI < n; idxI++) {

            // If this number is seen for the first time
            if (!map.containsKey(nums[idxI])) {
                // Store as: {previous index, latest index}
                // -1 means no previous occurrence yet
                map.put(nums[idxI], new int[]{-1, idxI});
            } 
            else {
                // Retrieve last two occurrences
                int[] pair = map.get(nums[idxI]);
                int prev = pair[0];    // older index
                int second = pair[1];  // most recent index

                // If we already have 2 previous occurrences
                if (prev != -1) {
                    int a = prev;
                    int b = second;
                    int c = idxI;

                    // Compute total pairwise distance
                    // |a-b| + |b-c| + |c-a|
                    int newMinDistance = Math.abs(a - b) 
                                    + Math.abs(b - c) 
                                    + Math.abs(c - a);

                    // Update minimum distance
                    minDistance = Math.min(minDistance, newMinDistance);
                }

                // Shift window:
                // second becomes previous, current becomes second
                pair[0] = second;
                pair[1] = idxI;
            }
        }

        // If no valid triplet found → return -1
        return minDistance == Integer.MAX_VALUE ? -1 : minDistance;
    }
}