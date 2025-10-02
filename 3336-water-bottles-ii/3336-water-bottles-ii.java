class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int maxDrankBottles = numBottles;

        int emptyBottles = numBottles - numExchange;
        int fullBottles = emptyBottles >= 0 ? 1 : 0;
        numExchange += 1;

        while((fullBottles + emptyBottles) >= numExchange || fullBottles > 0){
            if(emptyBottles >= numExchange){
                emptyBottles -= numExchange;
                fullBottles += 1;
                numExchange += 1;
            }
            else{
                emptyBottles += fullBottles;
                maxDrankBottles += fullBottles;
                fullBottles = 0;
            }
        }

        return maxDrankBottles;
    }
}