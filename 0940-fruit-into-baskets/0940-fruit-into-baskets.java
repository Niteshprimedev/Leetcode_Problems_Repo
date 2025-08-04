class Solution {
    public int totalFruit(int[] fruits) {
        int maxFruitsCount = 0;
        int strtIdx = 0;
        int endIdx = 0;
        HashMap<Integer, Integer> fruitsTyepeFreq= new HashMap<>();

        while(endIdx < fruits.length){
            int currFruit = fruits[endIdx];
            int hashValue = fruitsTyepeFreq.get(currFruit) == null ? 1 : fruitsTyepeFreq.get(currFruit) + 1;

            fruitsTyepeFreq.put(currFruit, hashValue);

            if(fruitsTyepeFreq.size() > 2){
                int strtFruit = fruits[strtIdx];
                hashValue = fruitsTyepeFreq.get(strtFruit);

                if(hashValue == 1){
                    fruitsTyepeFreq.remove(strtFruit);
                }
                else{
                    fruitsTyepeFreq.put(strtFruit, hashValue - 1);
                }
                
                strtIdx += 1;
            }
            
            maxFruitsCount = Math.max(maxFruitsCount, (endIdx - strtIdx + 1));
            endIdx += 1;
        }

        return maxFruitsCount;
    }
}