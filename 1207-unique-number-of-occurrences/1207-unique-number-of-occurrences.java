class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> freqMap = new HashMap<>();

        for(int num : arr){
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        HashSet<Integer> uniqueOccurence = new HashSet<>();

        for(Map.Entry<Integer, Integer> entry : freqMap.entrySet()){
            int hashKey = entry.getKey();
            int hashValue = entry.getValue();

            if(uniqueOccurence.contains(hashValue)){
                return false;
            }

            uniqueOccurence.add(hashValue);
        }

        return true;
    }
}