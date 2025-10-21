class Solution {
    public int countTriplets(int[] arr) {
        /*
        int n = arr.length;

        int[] suffixXor = new int[n];
        suffixXor[n - 1] = arr[n - 1];

        for(int i = n - 2; i >= 0; i--){
            suffixXor[i] = arr[i] ^ suffixXor[i + 1];
        }

        // System.out.println(Arrays.toString(suffixXor));
        int totalTripletsCount = 0;

        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){

            }
        }

        return 3;
        */

        // Intuition: subarrXor(i, j - 1) ^ subarrXor(j, k) => 0
        // hence find all the subarrs where xor => 0;
        int n = arr.length;
        int[] prefixXOR = new int[n + 1];
        prefixXOR[0] = 0;

        for(int i = 1; i <= n; i++){
            prefixXOR[i] = prefixXOR[i - 1] ^ arr[i - 1];
        }

        int allTripletsCount = 0;

        for(int i = 0; i < n; i++){
            int prefixXORI = prefixXOR[i];

            for(int k = i + 1; k < n; k++){
                int prefixXORK = prefixXOR[k + 1];                

                if((prefixXORI ^ prefixXORK) == 0){
                    allTripletsCount += (k - i); // this is formula to count valid subarrs;
                }
            }
        }

        return allTripletsCount;
    }
}