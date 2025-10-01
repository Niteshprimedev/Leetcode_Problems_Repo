class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int maxDrankBottles = numBottles;
        int bottlesCount = numBottles;

        while(bottlesCount >= numExchange){
            maxDrankBottles += bottlesCount / numExchange;
            bottlesCount = bottlesCount / numExchange + (bottlesCount % numExchange);
        }

        return maxDrankBottles;
    }
}