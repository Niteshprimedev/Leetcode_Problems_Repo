class Pair<C, I extends Comparable<I>>{
    C strChar;
    I charFreq;

    Pair(C strChar, I charFreq){
        this.strChar = strChar;
        this.charFreq = charFreq;
    }

    public I getCharFreq(){
        return charFreq;
    }
}

class Solution {
    public String reorganizeString(String s) {
        StringBuilder reorganizedSB = new StringBuilder("");
        HashMap<Character, Integer> freqMap = new HashMap<>();

        // One way to compare using Integer.compare and extends;
        // PriorityQueue<Pair<Character, Integer>> maxHeap = new PriorityQueue<>((p1, p2) -> Integer.compare(p2.charFreq, p1.charFreq));

        // Another way to compare;
        // PriorityQueue<Pair<Character, Integer>> maxHeap = new PriorityQueue<>(Comparator.comparing((Pair<Character, Integer> p) -> p.charFreq).reversed());
        
        // Another way using Method Ref;
        PriorityQueue<Pair<Character, Integer>> maxHeap = new PriorityQueue<>(Comparator.comparing(Pair::getCharFreq, Comparator.reverseOrder()));

        for(char c : s.toCharArray()){
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }

        for(Map.Entry<Character, Integer> entry : freqMap.entrySet()){
            char strChar = entry.getKey();
            Integer charFreq = entry.getValue(); // auto boxing;

            maxHeap.add(new Pair<>(strChar, charFreq));
        }

        while(maxHeap.size() > 1){
            Pair<Character, Integer> currPair1 = maxHeap.poll();
            Pair<Character, Integer> currPair2 = maxHeap.poll();

            reorganizedSB.append(currPair1.strChar);
            reorganizedSB.append(currPair2.strChar);

            currPair1.charFreq -= 1;
            currPair2.charFreq -= 1;

            if(currPair1.charFreq > 0){
                maxHeap.add(new Pair<>(currPair1.strChar, currPair1.charFreq));
            }

            if(currPair2.charFreq > 0){
                maxHeap.add(new Pair<>(currPair2.strChar, currPair2.charFreq));
            }
        }

        if(!maxHeap.isEmpty()){
            Pair<Character, Integer> lastPair = maxHeap.poll();

            if(lastPair.charFreq > 1 || (reorganizedSB.length() > 0 && lastPair.strChar == reorganizedSB.charAt(reorganizedSB.length() - 1))){
                return "";
            }

            reorganizedSB.append(lastPair.strChar);
        }

        return reorganizedSB.toString();
    }
}