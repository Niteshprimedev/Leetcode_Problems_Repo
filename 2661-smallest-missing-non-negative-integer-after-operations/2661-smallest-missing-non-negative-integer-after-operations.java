class Solution {
    public int findSmallestInteger(int[] nums, int value) {
        /*
        TreeSet<Integer> treeSet = new TreeSet<>();

        for(int num : nums){
            int newNum = num % value;

            if(newNum < 0){
                newNum += value;
            }

            treeSet.add(newNum);
        }

        System.out.println(treeSet.size());
        int mexVal = 0;

        while(treeSet.contains(mexVal)){
            treeSet.remove(mexVal);
            mexVal += 1;
        }

        return mexVal;
        */

        HashMap<Integer, Integer> freqMap = new HashMap<>();

        for(int num : nums){
            int newNum = num % value;

            if(newNum < 0){
                newNum += value;
            }

            freqMap.put(newNum, freqMap.getOrDefault(newNum, 0) + 1);
        }

        TreeSet<Integer> treeSet = new TreeSet<>();

        for(Map.Entry<Integer, Integer> entry : freqMap.entrySet()){
            int numKey = entry.getKey();
            int freqValue = entry.getValue() - 1;

            treeSet.add(numKey);

            while(freqValue > 0){
                int newNum = freqValue * value;
                newNum += numKey;

                treeSet.add(newNum);
                freqValue -= 1;
            }
        }

        int mexVal = 0;

        while(treeSet.contains(mexVal)){
            treeSet.remove(mexVal);
            mexVal += 1;
        }

        return mexVal;
    }
}