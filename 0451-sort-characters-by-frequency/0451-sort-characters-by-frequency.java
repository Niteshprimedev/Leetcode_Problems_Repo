class Solution {
    public String frequencySort(String s) {
        /*
        // creating pairs
        // 

        // List<List<Integer>> pairs = new ArrayList<>();
        // 24
        // [[][][][][][]['a', 'A'],[][]]
        // {'a': 10, 'A': 10}
        // 10: ['a', 'A']
        // 

        StringBuilder sb = new StringBuilder();

        int n = s.length();
        HashMap<Character, Integer> map = new HashMap<>();

        for(char curr_char : s.toCharArray()){
            map.put(curr_char, map.getOrDefault(curr_char, 0) + 1);
        }

        List<Character>[] freq_arr = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            freq_arr[i] = new ArrayList<>();
        }

        for(Map.Entry<Character, Integer> entry : map.entrySet()){
            char hashKey = entry.getKey();
            int freq = entry.getValue();

            freq_arr[freq].add(hashKey);
        }

        for(int idx = n; idx >= 0; idx--){
            if(freq_arr[idx].size() > 0){
                for(int j = 0; j < freq_arr[idx].size(); j++){
                    char curr_char = freq_arr[idx].get(j);
                    int curr_freq = idx;

                    while(curr_freq > 0){
                        sb.append(curr_char);
                        curr_freq -= 1;
                    }
                }
            }
        }

        return sb.toString();
        */

        // Meta Prep Time Practice:
        StringBuilder sb = new StringBuilder();

        int n = s.length();
        HashMap<Character, Integer> map = new HashMap<>();

        for(char curr_char : s.toCharArray()){
            map.put(curr_char, map.getOrDefault(curr_char, 0) + 1);
        }

        List<Character>[] freq_arr = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            freq_arr[i] = new ArrayList<>();
        }

        for(Map.Entry<Character, Integer> entry : map.entrySet()){
            char hashKey = entry.getKey();
            int freq = entry.getValue();

            freq_arr[freq].add(hashKey);
        }

        for(int idx = n; idx >= 0; idx--){
            if(freq_arr[idx].size() > 0){
                for(int j = 0; j < freq_arr[idx].size(); j++){
                    char curr_char = freq_arr[idx].get(j);
                    int curr_freq = idx;

                    while(curr_freq > 0){
                        sb.append(curr_char);
                        curr_freq -= 1;
                    }
                }
            }
        }

        return sb.toString();
    }
}