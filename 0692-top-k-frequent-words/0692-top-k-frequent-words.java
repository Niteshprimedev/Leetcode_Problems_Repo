class Pair {
    String word;
    Integer freq;

    Pair(String word, Integer freq){
        this.word = word;
        this.freq = freq;
    }

    public String getWord(){
        return word;
    }

    public Integer getFreq(){
        return freq;
    }
}

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Long> wordFreqMap = Arrays.stream(words).collect(Collectors.groupingBy(word -> word, Collectors.counting()));
        PriorityQueue<Pair> minHeap = new PriorityQueue<>(Comparator.comparing(Pair::getFreq).thenComparing(Pair::getWord, Comparator.reverseOrder()));

        for(Map.Entry<String, Long> entry : wordFreqMap.entrySet()){
            String key = entry.getKey();
            Integer value = entry.getValue().intValue();

            minHeap.add(new Pair(key, value));

            if(minHeap.size() > k){
                minHeap.poll();
            }
        }

        List<String> topKFreqWordsList = new ArrayList<>();

        while(!minHeap.isEmpty()){
            Pair currPair = minHeap.poll();

            topKFreqWordsList.add(currPair.word);
        }

        Collections.reverse(topKFreqWordsList);
        return topKFreqWordsList;
    }
}