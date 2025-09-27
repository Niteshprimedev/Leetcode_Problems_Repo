class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int n = s.length();
        HashMap<String, Integer> map = new HashMap<>();
        List<String> repeatedDNASeqs = new ArrayList<>();

        int strt = 0;
        int end = 9;

        while(end < n){
            String currDNASeq = s.substring(strt, end + 1);

            if(map.containsKey(currDNASeq) && map.get(currDNASeq) == 1){
                repeatedDNASeqs.add(currDNASeq);
            }

            map.put(currDNASeq, map.getOrDefault(currDNASeq, 0) + 1);
            int windowSize = end - strt + 1;
            if(windowSize == 10){
                strt += 1;
            }
            end += 1;
        }

        return repeatedDNASeqs;
    }
}