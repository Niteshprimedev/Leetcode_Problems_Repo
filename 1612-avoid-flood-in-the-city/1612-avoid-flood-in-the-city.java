import java.util.PriorityQueue;
import java.util.Comparator;

class NextLake{
    int lake;
    int nextRainyDay;

    public NextLake(int lake, int nextRainyDay){
        this.lake = lake;
        this.nextRainyDay = nextRainyDay;
    }
}

class Solution {
    public int[] avoidFlood(int[] rains) {
        /*
        // Brute Force Solution:

        int n = rains.length;
        int[] ans = new int[n];

        HashMap<Integer, Integer> leftMap = new HashMap<>();

        for(int i = 0; i < n; i++){
            if(rains[i] > 0){
                leftMap.put(rains[i], leftMap.getOrDefault(rains[i], 0) + 1);
                ans[i] = -1;
            }
            else{
                boolean isLakeDried = false;

                if(!leftMap.isEmpty()){
                    for(int j = i + 1; j < n; j++){
                        if(rains[j] > 0 && leftMap.containsKey(rains[j])){
                            leftMap.remove(rains[j]);
                            ans[i] = rains[j];
                            isLakeDried = true;
                            break;
                        }
                    }
                }
                
                if(!isLakeDried){
                    ans[i] = 1;
                }
            }

            // System.out.println(leftMap.getOrDefault(rains[i],0) + "i" + i + "rains[i]" + rains[i]);
            if(leftMap.getOrDefault(rains[i], 0) > 1){
                return new int[]{};
            }
        }

        return ans;
        */

        /*
        // Better Solution using Priority Queue on the earliest day;
        int n = rains.length;
        int[] ans = new int[n];

        HashMap<Integer, Integer> leftMap = new HashMap<>();
        PriorityQueue<NextLake> minHeap = new PriorityQueue<>(Comparator.comparingInt(nxtLake -> nxtLake.nextRainyDay));

        for(int i = 0; i < n; i++){
            if(rains[i] == 0) continue;
            minHeap.add(new NextLake(rains[i], i));
        }

        for(int i = 0; i < n; i++){
            while(!minHeap.isEmpty() && minHeap.peek().nextRainyDay <= i){
                System.out.println("Hello! " + "why at " + i + " it's " + rains[i] + "day " + minHeap.peek().nextRainyDay);
                // remove today's day;
                minHeap.poll();
            }

            if(rains[i] > 0){
                leftMap.put(rains[i], leftMap.getOrDefault(rains[i], 0) + 1);
                ans[i] = -1;
            }
            else{
                // dry day;
                if(!minHeap.isEmpty() && leftMap.containsKey(minHeap.peek().lake)){
                    NextLake nextLake = minHeap.poll();
                    ans[i] = nextLake.lake;
                    leftMap.remove(nextLake.lake);
                    System.out.println("i" + i + "nextLake" + nextLake.lake + "day" + nextLake.nextRainyDay);
                    System.out.println("\n");
                }
                else{
                    ans[i] = 1;
                }
            }
            System.out.println("size" + minHeap.size());
            System.out.println(leftMap.getOrDefault(rains[i],0) + "i" + i + "rains[i]" + rains[i]);
            if(leftMap.getOrDefault(rains[i], 0) > 1){
                return new int[]{};
            }
        }

        return ans;
        */

        // Solution using TreeSet and HashMap;
        TreeSet<Integer> drySet = new TreeSet<>();
        HashMap<Integer, Integer> lastDayMap = new HashMap<>();
        int n = rains.length;

        int[] ans = new int[n];
        Arrays.fill(ans, 1);

        for(int i = 0; i < n; i++){
            if(rains[i] == 0){
                drySet.add(i);
            }
            else{
                if(lastDayMap.containsKey(rains[i])){
                    Integer higherBound = drySet.higher(lastDayMap.get(rains[i]));

                    if(higherBound == null){
                        return new int[]{};
                    }
                    else{
                        drySet.remove(higherBound);
                        ans[higherBound] = rains[i];
                    }
                }

                ans[i] = -1;
                lastDayMap.put(rains[i], i);
            }
        }

        return ans;
    }
}