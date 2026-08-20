class Solution {
    public int[] resultArray(int[] nums) {
        List<Integer> arr1 = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();

        int idx = 0;

        for(int num : nums){
            if(idx >= 2){
                if(arr1.get(arr1.size() - 1) > arr2.get(arr2.size() - 1)){
                    arr1.add(num);
                }
                else{
                    arr2.add(num);
                }
            }
            if(idx == 0){
                arr1.add(num);
            }
            else if(idx == 1){
                arr2.add(num);
            }

            idx += 1;
        }

        // System.out.println(arr2.size() + " " + arr1.size());

        int n = nums.length;
        int[] result = new int[n];

        for(int i = 0; i < n; i++){
            if(i < arr1.size()){
                result[i] = arr1.get(i);
            }
            else{
                result[i] = arr2.get(i - arr1.size());
            }
        }

        return result;
    }
}