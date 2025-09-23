class Solution {
    public int countPrimes(int n) {
        // Seive of Eratosthenes;

        int totalPrimesCount = 0;
        if(n < 2){
            return totalPrimesCount;
        }

        boolean[] isPrimes = new boolean[n];

        Arrays.fill(isPrimes, true);

        isPrimes[0] = false;
        isPrimes[1] = false;

        int loopLen = (int) Math.floor(Math.sqrt(n + 1));

        for(int numVal = 2; numVal <= loopLen; numVal++){
            if(isPrimes[numVal] == true){
                for(int idxJ = numVal * 2; idxJ < n; idxJ += numVal){
                    isPrimes[idxJ] = false;
                }
            }
        }

        for(boolean isPrime: isPrimes){
            if(isPrime){
                totalPrimesCount += 1;
            }
        }

        return totalPrimesCount;
    }
}