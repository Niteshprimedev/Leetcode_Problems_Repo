class Solution {
    public int minimumCardPickup(int[] cards) {
        int minConsCards = Integer.MAX_VALUE;
        int windowEndIdx = 0;
        int n = cards.length;
        HashMap<Integer, Integer> cardsSeenMap = new HashMap<>();

        while(windowEndIdx < n){
            if(cardsSeenMap.containsKey(cards[windowEndIdx])){
                int newMinConsCards = windowEndIdx - cardsSeenMap.get(cards[windowEndIdx]) + 1;
                minConsCards = Math.min(minConsCards, newMinConsCards);
            }

            cardsSeenMap.put(cards[windowEndIdx], windowEndIdx);
            windowEndIdx += 1;
        }

        if(minConsCards == Integer.MAX_VALUE){
            return -1;
        }

        return minConsCards;
    }
}