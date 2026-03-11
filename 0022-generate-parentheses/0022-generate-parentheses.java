class Solution {
    private static boolean isOpeningParenthe(char parentheChar){
        if(parentheChar == '('){
            return true;
        }
        
        return false;
    }

    private static boolean isValidParentheses(char[] parentheArr){
        Stack <Character> stack = new Stack<>();

        for(char parenthe : parentheArr){
            int lastIdx = stack.size() - 1;

            if(stack.isEmpty() || isOpeningParenthe(parenthe)){
                stack.push(parenthe);
            }
            else if(parenthe == ')' && stack.get(lastIdx) == '('){
                stack.pop();
            }
            else{
                return false;
            }
        }

        if(stack.isEmpty()){
            return true;
        }

        return false;
    }

    private static List<String> generateParentheCombos(int currIdx, int totalSize, char[] currCombo, List<String> allParentheCombos){
        // Base Case:
        if(currIdx == totalSize - 1){
            if(isValidParentheses(currCombo)){
                allParentheCombos.add(String.valueOf(currCombo));
            }

            return allParentheCombos;
        }

        // Recursive Case:
        for(char currParenthe : new char[]{'(', ')'}){
            currCombo[currIdx] = currParenthe;

            generateParentheCombos(currIdx + 1, totalSize, currCombo, allParentheCombos);

            // backtrack and revert changes for next parenthesis generation;
            currCombo[currIdx] = '\0';
        }

        return allParentheCombos;
    }

    public List<String> generateParenthesis(int n) {
        int totalSize = n * 2;
        char[] currCombo = new char[totalSize];
        Arrays.fill(currCombo, '\0');

        currCombo[0] = '(';
        currCombo[totalSize - 1] = ')';

        ArrayList<String> allParentheCombos = new ArrayList<>();

        generateParentheCombos(1, totalSize, currCombo, allParentheCombos);
        return allParentheCombos;
    }
}