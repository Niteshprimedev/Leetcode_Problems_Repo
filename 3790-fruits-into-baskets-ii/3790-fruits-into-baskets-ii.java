class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        int unplacedFruits = 0;

        HashSet<Integer> placed = new HashSet<>();

        for(int fruit : fruits){
            for(int idx = 0; idx < baskets.length; idx++){
                if(!placed.contains(idx) && fruit <= baskets[idx]){
                    placed.add(idx);
                    break;
                }
            }
        }

        return baskets.length - placed.size();
    }
}