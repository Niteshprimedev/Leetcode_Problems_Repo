class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {

        HashSet<Integer> placed = new HashSet<>();

        for(int fruit : fruits){
            for(int idx = 0; idx < baskets.length; idx++){
                if(!placed.contains(idx) && fruit <= baskets[idx]){
                    placed.add(idx);
                    break;
                }
            }
        }

        int unplacedFruits = baskets.length - placed.size();
        return unplacedFruits;
    }
}