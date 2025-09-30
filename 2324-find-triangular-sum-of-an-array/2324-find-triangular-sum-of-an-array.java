class Solution {
    public int triangularSum(int[] nums) {
        int n = nums.length;
        int[] numsCopy = nums;

        // System.out.println(Arrays.toString(numsCopy));

        while(n > 1){
            int i = 0;
            int[] newNums = new int[n - 1];

            while (i < n - 1){
                newNums[i] = (numsCopy[i] + numsCopy[i + 1]) % 10;
                i += 1;
            }

            numsCopy = newNums;
            n -= 1;
        }

        return numsCopy[0];
    }
}