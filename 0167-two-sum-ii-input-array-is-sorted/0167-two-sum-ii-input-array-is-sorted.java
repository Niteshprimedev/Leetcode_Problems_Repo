class Solution {
    public int[] twoSum(int[] numbers, int target) {
        /*
        // Meta Prep Time for April Hiring;
        // Optimal Solution 1
        int strt = 0;
        int end = numbers.length - 1;
        int[] result = new int[2];

        // Time Complexity -> O(N); & SC -> O(1)
        while(strt < end){
            if(numbers[strt] + numbers[end] == target){
                result[0] = strt + 1;
                result[1] = end + 1;
                break;
            }
            else if(numbers[strt] + numbers[end] > target){
                end -= 1;
            }
            else{
                strt += 1;
            }
        }

        return result;
        */

        // SubOptimal Solution:
        Map<Integer, Integer> map = new HashMap<>();
        int n = numbers.length;
        
        for(int i = 0; i < n; i++){
            int currNum = numbers[i];
            int secondNum = target - currNum;

            if(map.containsKey(secondNum)){
                return new int[]{map.get(secondNum) + 1, i + 1};
            }

            map.put(currNum, i);
        }

        return new int[]{};
    }
}