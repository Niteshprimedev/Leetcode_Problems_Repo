class Solution {
    public int maxScore(int[] cardPoints, int k) {
        /*
        int totalPoints = 0;

        for(int card : cardPoints){
            totalPoints += card;
        }

        int n = cardPoints.length;
        int windowSize = n - k;

        if(windowSize == 0){
            return totalPoints;
        }

        int maxPoints = 0;

        int strtIdx = 0;
        int endIdx = 0;

        while(endIdx < n){
            totalPoints -= cardPoints[endIdx];

            // System.out.println(maxPoints + " " + totalPoints);

            if((endIdx - strtIdx + 1) == windowSize){
                maxPoints = Math.max(maxPoints, totalPoints);

                totalPoints += cardPoints[strtIdx];
                strtIdx += 1;
            }

            endIdx += 1;
        }

        return maxPoints;
        */

        // Solution:

        int totalPoints = 0;

        int maxPoints = 0;
        
        // Maximum points from strt window;
        for(int i = 0; i < k; i++){
            totalPoints += cardPoints[i];
        }

        maxPoints = totalPoints;

        int n = cardPoints.length;
        int strt = k - 1;

        // Maximum points from both strt & end and end window;
        for(int i = n - 1; i >= (n - k); i--){
            // remove from strt;
            totalPoints -= cardPoints[strt--];
            totalPoints += cardPoints[i];

            maxPoints = Math.max(maxPoints, totalPoints);
        }

        return maxPoints;
    }
}