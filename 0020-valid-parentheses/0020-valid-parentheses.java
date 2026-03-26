class Solution {

    private static boolean isOpenParenthe(char parentheChar){
        if(parentheChar == '(' || parentheChar == '[' || parentheChar == '{'){
            return true;
        }

        return false;
    }

    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for(char parenthe : s.toCharArray()){
            int lastIdx = stack.size() - 1;
            if(stack.isEmpty() || isOpenParenthe(parenthe)){
                stack.push(parenthe);
            }
            else if(parenthe == ')' && stack.get(lastIdx) == '('){
                stack.pop();
            }
            else if(parenthe == ']' && stack.get(lastIdx) == '['){
                stack.pop();
            }
            else if(parenthe == '}' && stack.get(lastIdx) == '{'){
                stack.pop();
            }
            else{
                return false;
            }
        }

        // System.out.println(stack);
        if(stack.isEmpty()){
            return true;
        }

        return false;
    }
}