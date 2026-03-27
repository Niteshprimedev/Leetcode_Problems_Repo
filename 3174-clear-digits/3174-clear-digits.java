class Solution {
    private boolean isDigit(char curr){
        String numbers = "0123456789";
        return numbers.indexOf(curr) >= 0;
    }

    public String clearDigits(String s) {
        Stack<Character> charsStack = new Stack<>();

        for(char curr : s.toCharArray()){
            if(isDigit(curr) && !charsStack.isEmpty()){
                charsStack.pop();
            }
            else if(!isDigit(curr) || (isDigit(curr) && charsStack.isEmpty())){
                charsStack.push(curr);
            }
        }

        StringBuilder clearDigitsStr = new StringBuilder();
        
        for(int i = 0; i < charsStack.size(); i++){
            clearDigitsStr.append(charsStack.get(i));
        }

        return clearDigitsStr.toString();
    }
}