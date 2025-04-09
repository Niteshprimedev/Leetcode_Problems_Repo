/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.toLowerCase();
    const regExp = /[a-z0-9]/;

    let newPalindromicStr = '';
    for(let char of s){
        const isAlphabet = regExp.test(char);
        if(isAlphabet){
            newPalindromicStr += char;
        }
    }

    // console.log(newPalindromicStr);

    let strtIdx = 0;
    let endIdx = newPalindromicStr.length - 1;

    while(strtIdx < endIdx){
        const strtChar = newPalindromicStr[strtIdx];
        const endChar = newPalindromicStr[endIdx];

        if(strtChar !== endChar){
            return false;
        }

        strtIdx++;
        endIdx--;
    }

    return true;
};