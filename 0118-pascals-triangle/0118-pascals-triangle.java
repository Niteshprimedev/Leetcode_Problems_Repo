class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> pascalTriangle = new ArrayList<>();

        List<Integer> prevLevel = new ArrayList<>();
        prevLevel.add(1);
        
        for(int rowIdx = 0; rowIdx < numRows; rowIdx++){
            List<Integer> currLevel = new ArrayList<>();

            for(int idx = 0; idx <= rowIdx; idx++){
                int prevVal = idx > 0 ? prevLevel.get(idx - 1) : 0;
                int currVal = idx < prevLevel.size() ? prevLevel.get(idx) : 0;

                currLevel.add(prevVal + currVal);
            }

            prevLevel = currLevel;
            pascalTriangle.add(currLevel);
        }

        return pascalTriangle;
    }
}