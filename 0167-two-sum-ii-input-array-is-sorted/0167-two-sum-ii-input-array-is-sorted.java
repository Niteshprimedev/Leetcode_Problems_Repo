class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int strt = 0;
        int end = numbers.length - 1;
        int[] result = new int[2];

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
    }
}