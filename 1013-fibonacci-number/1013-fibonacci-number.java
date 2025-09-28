class Solution {
    int fibSeq(int n, int[] memoDP){
        if(n == 0 || n == 1){
            return n;
        }

        if(memoDP[n] != -1){
            return memoDP[n];
        }

        int firstNum = fibSeq(n - 1, memoDP);
        int secondNum = fibSeq(n - 2, memoDP);

        memoDP[n] = firstNum + secondNum;
        return memoDP[n];        
    }

    public int fib(int n) {
        int[] memoDP = new int[n + 2];
        Arrays.fill(memoDP, -1);

        memoDP[0] = 0;
        memoDP[1] = 1;

        fibSeq(n, memoDP);

        return memoDP[n];
    }
}