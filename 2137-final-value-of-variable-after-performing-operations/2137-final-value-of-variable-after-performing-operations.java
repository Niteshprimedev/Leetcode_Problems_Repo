class Solution {
    public int finalValueAfterOperations(String[] operations) {
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
    }
}