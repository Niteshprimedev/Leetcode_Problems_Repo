class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        // Logic: Keep the asteroids in the stack
        // both negative and positive if negative comes first;

        Stack<Integer> stack = new Stack<>();

        int idxI = 0;
        int n = asteroids.length;

        while(idxI < n){
            // Case1: if negative and stack empty or stack lastEl is negative
            int asteroid = asteroids[idxI];
            if(asteroid < 0 && (stack.isEmpty() || stack.peek() < 0)){
                stack.push(asteroid);
                idxI += 1;
            }
            // Case2: if negative and stack lastEl is positive;
            else if(asteroid < 0 && stack.peek() > 0){
                int absAsteroid = Math.abs(asteroid);

                // Bigger;
                if(absAsteroid > stack.peek()){
                    stack.pop();
                }
                // Equal;
                else if(absAsteroid == stack.peek()){
                    stack.pop();
                    idxI += 1;
                }
                // Smaller
                else{
                    idxI += 1;
                }
            }
            // Case3: if positive asteroid;
            else{
                stack.push(asteroid);
                idxI += 1;
            }
        }

        int[] newAsteroids = new int[stack.size()];

        for(int idx = 0; idx < stack.size(); idx++){
            newAsteroids[idx] = stack.get(idx);
        }

        return newAsteroids;
    }
}