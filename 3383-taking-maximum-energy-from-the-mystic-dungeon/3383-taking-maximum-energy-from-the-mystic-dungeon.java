class Solution {
    private int findMaxEnergy(int currIdx, int prevIdx, int[] energy, int k, int[][] memoDP){
        // Base Case:
        if(currIdx >= energy.length){
            return prevIdx == -1 ? Integer.MIN_VALUE : 0;
        }

        if(memoDP[currIdx][prevIdx + 1] != 0){
            return memoDP[currIdx][prevIdx + 1];
        }

        // pick case;
        int pickCase = energy[currIdx] + findMaxEnergy(currIdx + k, 0, energy, k, memoDP);

        int notPickCase = Integer.MIN_VALUE;
        if(prevIdx == -1){
            notPickCase = findMaxEnergy(currIdx + 1, -1, energy, k, memoDP);
        }

        memoDP[currIdx][prevIdx + 1] = Math.max(pickCase, notPickCase);
        // System.out.println(pickCase + " " + notPickCase + " " + memoDP[currIdx][prevIdx + 1]);
        // System.out.println(currIdx + "currIdx" + prevIdx + " prevIdx");
        return memoDP[currIdx][prevIdx + 1];
    }
    public int maximumEnergy(int[] energy, int k) {
        int n = energy.length;
        return findMaxEnergy(0, -1, energy, k, new int[n][2]);
    }
}