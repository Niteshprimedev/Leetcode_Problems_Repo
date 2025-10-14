class Solution {
    public long minimumTotalCost(int[] nums1, int[] nums2) {
        int n = nums1.length;
        long totalCost = 0;
        int badCount = 0;
        Map<Integer, Integer> freq = new HashMap<>();
        int maxFreq = 0, dominantValue = -1;
        
        // Step 1: Identify bad positions
        for (int i = 0; i < n; i++) {
            if (nums1[i] == nums2[i]) {
                badCount++;
                totalCost += i;
                freq.put(nums1[i], freq.getOrDefault(nums1[i], 0) + 1);
                if (freq.get(nums1[i]) > maxFreq) {
                    maxFreq = freq.get(nums1[i]);
                    dominantValue = nums1[i];
                }
            }
        }

        // Step 2: Balance condition
        int i = 0;
        while (maxFreq > (badCount / 2)) {
            // Need to include more indices that break dominance
            while (i < n && (nums1[i] == nums2[i] ||
                    nums1[i] == dominantValue || nums2[i] == dominantValue)) {
                i++;
            }
            if (i == n) return -1; // Not enough balancing indices

            totalCost += i;
            badCount++;
            i++;
        }

        return totalCost;
    }
}