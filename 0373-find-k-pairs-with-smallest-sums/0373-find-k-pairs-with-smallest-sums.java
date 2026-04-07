class Solution {
    class Element{
        int sum = 0;
        int idxI = 0;
        int idxJ = 0;

        public Element(int sum, int idxI, int idxJ){
            this.sum = sum;
            this.idxI = idxI;
            this.idxJ = idxJ;
        }
    }

    private String encodedIndex(int idxI, int idxJ){
        return String.valueOf(idxI + " " + idxJ);
    }

    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        /*
        int m = nums1.length;
        int n = nums2.length;

        List<List<Integer>> smallestPairs = new ArrayList<>();
        int idxI = 0;
        int idxJ = 0;
        int sumCount = k;

        Set<Pair> visitedPairs = new HashSet<>();

        // PriorityQueue<Element> minHeap = new PriorityQueue<>((el1, el2) -> el1.sum - el2.sum);
        PriorityQueue<Element> minHeap = new PriorityQueue<>((el1, el2) -> Integer.compare(el1.sum, el2.sum));
        minHeap.add(new Element(nums1[idxI] + nums2[idxJ], idxI, idxJ));
        visitedPairs.add(new Pair<>(idxI, idxJ));

        while(sumCount > 0 && !minHeap.isEmpty()){
            Element currElement = minHeap.poll();

            int currSum = currElement.sum;
            idxI = currElement.idxI;
            idxJ = currElement.idxJ;

            smallestPairs.add(Arrays.asList(nums1[idxI], nums2[idxJ]));

            if(idxI + 1 < m && !visitedPairs.contains(new Pair<>(idxI + 1, idxJ))){
                minHeap.add(new Element(nums1[idxI + 1] + nums2[idxJ], idxI + 1, idxJ));
                visitedPairs.add(new Pair<>(idxI + 1, idxJ));
            }
            if(idxJ + 1 < n && !visitedPairs.contains(new Pair<>(idxI, idxJ + 1))){
                minHeap.add(new Element(nums1[idxI] + nums2[idxJ + 1], idxI, idxJ + 1));
                visitedPairs.add(new Pair<>(idxI, idxJ + 1));
            }

            sumCount -= 1;
        }

        return smallestPairs;
        */

        // Meta Prep Time Practice:
        int m = nums1.length;
        int n = nums2.length;

        List<List<Integer>> smallestPairs = new ArrayList<>();
        int idxI = 0;
        int idxJ = 0;
        int sumCount = k;

        // Encoded index, instead of Pair
        Set<String> visitedPairs = new HashSet<>();

        PriorityQueue<Element> minHeap = new PriorityQueue<>((el1, el2) -> Integer.compare(el1.sum, el2.sum));
        minHeap.add(new Element(nums1[idxI] + nums2[idxJ], idxI, idxJ));
        visitedPairs.add(encodedIndex(idxI, idxJ));

        while(sumCount > 0 && !minHeap.isEmpty()){
            Element currElement = minHeap.poll();

            int currSum = currElement.sum;
            idxI = currElement.idxI;
            idxJ = currElement.idxJ;

            smallestPairs.add(Arrays.asList(nums1[idxI], nums2[idxJ]));

            if(idxI + 1 < m && !visitedPairs.contains(encodedIndex(idxI + 1, idxJ))){
                minHeap.add(new Element(nums1[idxI + 1] + nums2[idxJ], idxI + 1, idxJ));
                visitedPairs.add(encodedIndex(idxI + 1, idxJ));
            }
            if(idxJ + 1 < n && !visitedPairs.contains(encodedIndex(idxI, idxJ + 1))){
                minHeap.add(new Element(nums1[idxI] + nums2[idxJ + 1], idxI, idxJ + 1));
                visitedPairs.add(encodedIndex(idxI, idxJ + 1));
            }

            sumCount -= 1;
        }

        return smallestPairs;
    }
}