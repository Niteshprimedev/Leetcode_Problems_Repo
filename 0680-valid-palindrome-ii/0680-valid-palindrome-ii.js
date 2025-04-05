/**
 * @param {string} s
 * @return {boolean}
 */
var validPalindrome = function(s) {
    const strLen = s.length;

    let strtIdx = 0;
    let endIdx = strLen - 1;

    const loopLen = Math.floor(strtIdx + (endIdx - strtIdx) / 2);
    let charsDeleteCount = 0;

    while(strtIdx <= loopLen){
        const strtIdxChar = s[strtIdx];
        const endIdxChar = s[endIdx];

        if(strtIdxChar !== endIdxChar){
            // const nextIdxChar = s[strtIdx + 1];
            const prevIdxChar = s[endIdx - 1];

            if(strtIdxChar === prevIdxChar){
                charsDeleteCount++;
                endIdx--;
            }
            else{
                charsDeleteCount = 2;
                break;
            }
        }
        strtIdx++;
        endIdx--;
    }

    if(charsDeleteCount < 2) return true;

    strtIdx = 0;
    endIdx = strLen - 1;
    charsDeleteCount = 0;

    while(strtIdx <= loopLen){
        const strtIdxChar = s[strtIdx];
        const endIdxChar = s[endIdx];

        if(strtIdxChar !== endIdxChar){
            const nextIdxChar = s[strtIdx + 1];

            if(nextIdxChar === endIdxChar){
                charsDeleteCount++;
                strtIdx++;
            }
            else{
                charsDeleteCount = 2;
                break;
            }
        }
        // console.log(strtIdx, endIdx, s[strtIdx], s[endIdx], charsDeleteCount);
        strtIdx++;
        endIdx--;
    }

    if(charsDeleteCount > 1){
        return false
    }

    return true;
};