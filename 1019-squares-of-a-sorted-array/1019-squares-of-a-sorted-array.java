class Solution {
    public int[] sortedSquares(int[] nums) {
        return Arrays.stream(nums).map(num -> num * num).sorted().toArray();
    }
}