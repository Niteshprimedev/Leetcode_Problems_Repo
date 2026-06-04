class Solution {
    private String sortedStr(String inputStr){
        if(inputStr == null || inputStr.length() == 0) return "";
        return inputStr.chars()
                        .mapToObj(c -> (char) c)
                        .sorted()
                        .collect(
                            StringBuilder::new,
                            StringBuilder::appendCodePoint,
                            StringBuilder::append
                        )
                        .toString();
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        /*
        Sol1: Stream API Solution
        return Arrays.stream(strs)
            .collect(Collectors.groupingBy(str -> sortedStr(str)))
            .entrySet()
            .stream()
            .peek(entry -> System.out.println("Sorted key: " + entry.getKey()))
            .map(Map.Entry::getValue)
            .toList();
            */

        // Sol2: Using map and sorting;

        Map<String, List<String>> groupsMap = new HashMap<>();
        List<List<String>> anagramsGroup = new ArrayList<>();

        for(String currStr : strs){
            char[] charsArr = currStr.toCharArray();
            Arrays.sort(charsArr);

            String sortedStr = new String(charsArr);
            List<String> hashValue = new ArrayList<>();

            if(!groupsMap.containsKey(sortedStr)){
                groupsMap.put(sortedStr, hashValue);
            }

            hashValue = groupsMap.get(sortedStr);
            hashValue.add(currStr);

            groupsMap.put(sortedStr, hashValue);
        }

        // for(Map.Entry<String, List<String>> entry : groupsMap.entrySet()){
        //     anagramsGroup.add(entry.getValue());
        // }

        // return anagramsGroup;

        // Or;
        return groupsMap.values().stream().toList();
    }
}