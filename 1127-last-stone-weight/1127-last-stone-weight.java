class Solution {
    public int lastStoneWeight(int[] stones) {
        /*
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        maxHeap.addAll(Arrays.stream(stones).boxed().toList());

        while(maxHeap.size() > 1){
            int x = maxHeap.poll();
            int y = maxHeap.poll();

            if(x > y){
                y ^= x;
                x ^= y;
                y ^= x;
            }

            if(x == y){
                continue;
            }
            else{
                maxHeap.add(Integer.valueOf(y - x));
            }
        }

        if(maxHeap.isEmpty()){
            return 0;
        }
        else{
            return maxHeap.peek().intValue();
        }
        */

        // Solution 2:
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        maxHeap.addAll(Arrays.stream(stones).boxed().toList());

        while(maxHeap.size() > 1){
            int y = maxHeap.poll();
            int x = maxHeap.poll();

            if(x != y){
                maxHeap.add(y - x);
            }
        }

        return maxHeap.isEmpty() ? 0 : maxHeap.peek();
    }
}