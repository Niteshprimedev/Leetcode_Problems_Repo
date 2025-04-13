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

            // if(groupLen > 1){
            //     while(groupLen > 0){
            //         const digit = groupLen % 10;
            //         chars[compressedIdx] = digit.toString();
            //         compressedIdx += 1;

            //         groupLen = Math.floor(groupLen / 10);
            //     }
            // }
            
            groupStrtIdx = groupEndIdx;
        }
    }

    return compressedIdx;
    // return chars;
};