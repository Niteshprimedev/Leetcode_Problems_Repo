class Solution {
    public int closestTarget(String[] words, String target, int startIndex) {
        /*
        // Pure Logical;

        int n = words.length;

        int shortestDist = Integer.MAX_VALUE;

        for(int i = 0; i < n; i++){
            String currWord = words[i];

            if(currWord.equals(target)){
                int leftDist = startIndex - i;
                int rightDist = i - startIndex;
                int circularRightDist = startIndex - 0 + n - i;
                int circularLeftDist = n - 1 - startIndex + i + 1;

                leftDist = leftDist < 0 ? Integer.MAX_VALUE : leftDist;
                rightDist = rightDist < 0 ? Integer.MAX_VALUE : rightDist;

                int normalDist = Math.min(leftDist, rightDist);
                int circularDist = Math.min(circularRightDist, circularLeftDist);
                int newShortestDist = Math.min(normalDist, circularDist);

                shortestDist = Math.min(shortestDist, newShortestDist);
            }
        }

        return shortestDist == Integer.MAX_VALUE ? -1 : shortestDist;
        */

        // Meta Prep Time Practice:
        int totalWords = words.length;
        int minimumDistance = Integer.MAX_VALUE;

        for (int currentIndex = 0; currentIndex < totalWords; currentIndex++) {

            if (words[currentIndex].equals(target)) {

                // Direct distance between indices
                int directDistance = Math.abs(currentIndex - startIndex);

                // Circular distance (wrap around)
                int circularDistance = totalWords - directDistance;

                // Best possible distance
                int bestDistance = Math.min(directDistance, circularDistance);

                minimumDistance = Math.min(minimumDistance, bestDistance);
            }
        }

        return minimumDistance == Integer.MAX_VALUE ? -1 : minimumDistance;
    }
}