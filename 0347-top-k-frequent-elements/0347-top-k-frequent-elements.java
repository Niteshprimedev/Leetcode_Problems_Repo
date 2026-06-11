class Solution {
    class PairKeyValue{
        int key;
        int value;

        PairKeyValue(int key, int value){
            this.key = key;
            this.value = value;
        }
    }

    public int[] topKFrequent(int[] nums, int k) {
        int[] topKFreqEls = new int[k];

        PriorityQueue<PairKeyValue> minHeap = new PriorityQueue<>((p1, p2) -> Integer.compare(p1.value, p2.value));

        HashMap<Integer, Integer> freqMap = new HashMap<>();

        for(int num : nums){
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        for(Map.Entry<Integer, Integer> entry : freqMap.entrySet()){
            Integer hashKey = entry.getKey();
            Integer hashValue = entry.getValue();

            PairKeyValue maxPair = new PairKeyValue(hashKey, hashValue);

            if(minHeap.size() == k){
                PairKeyValue currPair = minHeap.poll();

                if(currPair.value > hashValue){
                    maxPair = new PairKeyValue(currPair.key, currPair.value);
                }
            }
            minHeap.add(maxPair);
        }

        // System.out.println(minHeap.size());

        int i = 0;
        while(!minHeap.isEmpty()){
            PairKeyValue currPair = minHeap.poll();
            topKFreqEls[i++] = currPair.key;
        }

        return topKFreqEls;
    }
}