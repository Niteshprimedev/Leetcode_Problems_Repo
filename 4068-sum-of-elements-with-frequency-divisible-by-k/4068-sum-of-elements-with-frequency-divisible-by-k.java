import java.util.Map;
// import java.
class Solution {
    public int sumDivisibleByK(int[] nums, int k) {
        /*
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int num : nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        int totalSum = 0;

        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            if(entry.getValue() % k == 0){
                totalSum += (entry.getKey() * entry.getValue());
            }
        }

        return totalSum;
        */

        /*
        // Using Stream API;
        Map<Integer, Long> map = Arrays.stream(nums).boxed().collect(Collectors.groupingBy(num -> num, Collectors.counting()));

        int totalSum = 0;

        for(Map.Entry<Integer, Long> entry : map.entrySet()){
            if(entry.getValue() % k == 0){
                totalSum += (entry.getKey() * entry.getValue());
            }
        }

        return totalSum;
        */

        int totalSum = Arrays.stream(nums)
        .boxed()
        .collect(Collectors.groupingBy(n -> n, Collectors.summingInt(x -> 1))) // frequency map
        .entrySet()
        .stream()
        .filter(entry -> entry.getValue() % k == 0) // keep entries divisible by k
        .mapToInt(entry -> entry.getKey() * entry.getValue()) // key * frequency
        .sum();

        return totalSum;
    }
}