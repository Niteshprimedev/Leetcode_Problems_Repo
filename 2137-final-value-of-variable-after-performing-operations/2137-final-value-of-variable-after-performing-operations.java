class Solution {
    public int finalValueAfterOperations(String[] operations) {
        /*
        Optional<Integer> xValue = Arrays.stream(operations).map(currOp -> {
            if(currOp.charAt(0) == '+'){
                return 1;
            }
            else if(currOp.charAt(0) == '-'){
                return -1;
            }
            else if(currOp.charAt(2) == '+'){
                return 1;
            }
            else{
                return -1;
            }
        }).reduce((op1Val, op2Val) -> op1Val + op2Val);

        return xValue.get();
        */

        /*
        // Using Method Refs:
        Optional<Integer> xValue = Arrays.stream(operations).map(currOp -> {
            if(currOp.charAt(0) == '+'){
                return 1;
            }
            else if(currOp.charAt(0) == '-'){
                return -1;
            }
            else if(currOp.charAt(2) == '+'){
                return 1;
            }
            else{
                return -1;
            }
        }).reduce(Integer::sum);

        return xValue.get();
        */
        
        // Using reduce Identity 0 => then no Optional<Integer> only int
        int xValue = Arrays.stream(operations).map(currOp -> {
            if(currOp.charAt(0) == '+'){
                return 1;
            }
            else if(currOp.charAt(0) == '-'){
                return -1;
            }
            else if(currOp.charAt(2) == '+'){
                return 1;
            }
            else{
                return -1;
            }
        }).reduce(0, Integer::sum);

        return xValue;

        /*
        // Performance Better Solution:
        int xValue = Arrays.stream(operations).mapToInt(currOp -> currOp.charAt(0) == '+' || currOp.charAt(2) == '+' ? 1 : -1).sum(); // Stream<String> to IntStream => then sum() method on primitives

        return xValue;
        */
    }
}