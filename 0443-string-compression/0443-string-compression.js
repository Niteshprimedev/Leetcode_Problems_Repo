/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    let groupStrtIdx = 0;
    let groupEndIdx = 1;
    let compressedIdx = 0;

    for(groupEndIdx; groupEndIdx <= chars.length; groupEndIdx++){
        const strtChar = chars[groupStrtIdx];
        const endChar = chars[groupEndIdx];

        if(groupEndIdx === chars.length || endChar !== strtChar){
            let groupLen = groupEndIdx - groupStrtIdx;

            chars[compressedIdx] = chars[groupStrtIdx];
            compressedIdx += 1;
            
            if(groupLen > 1){
                const lenStr = groupLen.toString();
                for(let lenNum of lenStr){
                    chars[compressedIdx] = lenNum;
                    compressedIdx += 1;
                }
            }
            // Follow up: if we don't have toString function or ability then?
            /**
            if(groupLen > 1){
                let digitsLen = groupLen;
                let totalDigits = 0;

                while(digitsLen > 0){
                    digitsLen = Math.floor(digitsLen / 10);
                    totalDigits += 1;
                }

                let idxI = 0;

                while(groupLen > 0){
                    const digit = groupLen % 10;

                    if(totalDigits > 1){
                        chars[compressedIdx + totalDigits - 1] = digit.toString();
                        idxI += 1;
                    }
                    else{
                        chars[compressedIdx] = digit.toString();
                        compressedIdx += 1;
                    }

                    totalDigits -= 1;
                    groupLen = Math.floor(groupLen / 10);
                }
                compressedIdx += idxI;
            }

            */
            
            groupStrtIdx = groupEndIdx;
        }
    }

    return compressedIdx;
    // return chars;
};