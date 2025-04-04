/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const validBracketsObj = {
        ")": "(",
        "]": "[",
        "}": "{"
    };

    const bracketsStack = [];
    let isValidParentheses = true;

    for(let bracketChar of s){
        const isOpenBracket = "(" === bracketChar || "[" === bracketChar || "{" === bracketChar;
        if(isOpenBracket){
            bracketsStack.push(bracketChar);
        }
        else{
            const stacksOpenBracket = bracketsStack.pop();
            const objsOpenBracket = validBracketsObj[bracketChar];

            const isStacksOpenBracketEmpty = stacksOpenBracket === undefined;
            const isBracketsNotSame = objsOpenBracket !== stacksOpenBracket;
            if(isStacksOpenBracketEmpty || isBracketsNotSame){
                isValidParentheses = false;
                // console.log(bracketChar);
                break;
            }
        }
    }

    if(bracketsStack.length > 0){
        isValidParentheses = false;
    }

    return isValidParentheses;
};