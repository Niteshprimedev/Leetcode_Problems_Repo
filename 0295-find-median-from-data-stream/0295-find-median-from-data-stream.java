class MedianFinder {

    PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b)->b - a);
    PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b)->a - b);

    public MedianFinder() {
        
    }
    
    public void addNum(int num) {
        maxHeap.add(num);
        minHeap.add(maxHeap.poll());

        if(minHeap.size() > maxHeap.size()){
            maxHeap.add(minHeap.poll());
        }
    }
    
    public double findMedian() {
        int totalSize = maxHeap.size() + minHeap.size();

        double medianVal = 0;
        if(totalSize % 2 == 0){
            medianVal = (double) (maxHeap.peek() + minHeap.peek()) / 2.0;
        }
        else{
            medianVal = maxHeap.peek();
        }

        return medianVal;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */