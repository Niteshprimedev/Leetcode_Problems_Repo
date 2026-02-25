class Solution {
    private int totalBits(int num){
        int count = 0;

        while(num > 0){ 
            count += 1;
            num = num & (num - 1);
        }

        return count;
    }

    public int[] sortByBits(int[] arr) {
        return Arrays.stream(arr)
            .boxed()
            .sorted(Comparator.comparing((Integer num) -> totalBits(num)).thenComparing(Comparator.comparing(num -> num)))
            .mapToInt(Integer::intValue).toArray();

    }
}