class Solution {
    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) -> Integer.compare(a, b));

        for(int asteroid : asteroids){
            minHeap.add(asteroid);
        }

        long planetMass = mass;

        while(!minHeap.isEmpty()){
            int currAsteroid = minHeap.poll();

            if(planetMass >= (long) currAsteroid){
                planetMass += currAsteroid;
            }
            else{
                return false;
            }
        }

        return true;

        /*
        Type issue int to long;
        Arrays.sort(asteroids);

        long planetMass = mass;

        for(int currAsteroid : asteroids){
            if(planetMass >= (long) currAsteroid){
                planetMass += currAsteroid;
            }
            else{
                return false;
            }
        }

        return true;
        */
    }
}