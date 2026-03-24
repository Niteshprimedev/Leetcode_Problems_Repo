class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] dailyTemps = new int[n];

        Stack<Integer> nextGreaterElsStack = new Stack<>();

        for(int i = n - 1; i >= 0; i--){
            while(nextGreaterElsStack.size() > 0 && temperatures[nextGreaterElsStack.peek()] <= temperatures[i]){
                nextGreaterElsStack.pop();
            }

            int warmerDays = 0;

            if(nextGreaterElsStack.size() > 0){
                warmerDays = nextGreaterElsStack.peek() - i;
            }

            dailyTemps[i] = warmerDays;
            nextGreaterElsStack.push(i);
        }

        return dailyTemps;
    }
}