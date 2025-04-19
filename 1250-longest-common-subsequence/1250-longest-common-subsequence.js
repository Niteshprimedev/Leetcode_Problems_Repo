/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    // Bottom Up Approach:
    const str1Len = text1.length;
    const str2Len = text2.length;

    const memoDP = new Array(str1Len + 1).fill(-1).map(() => new Array(str2Len + 1).fill(0));

    // Base Case:
    // Ignored cause not had any valid base cases:
    for(let idxI = 0; idxI <= str1Len; idxI++){
        memoDP[idxI][0] = 0;
    }

    for(let idxJ = 0; idxJ <= str2Len; idxJ++){
        memoDP[0][idxJ] = 0;
    }

    // console.log(memoDP);

    for(let str1Idx = 1; str1Idx <=str1Len; str1Idx++){
        for(let str2Idx = 1; str2Idx <= str2Len; str2Idx++){
            if(text1[str1Idx - 1] === text2[str2Idx - 1]){
                const matchCase = 1 + memoDP[str1Idx - 1][str2Idx - 1];

                memoDP[str1Idx][str2Idx] = matchCase;
            }
            else{
                const str1NotMatchCase = memoDP[str1Idx - 1][str2Idx];
                const str2NotMatchCase = memoDP[str1Idx][str2Idx - 1];

                // console.log(str1Idx, str2Idx);
                const notMatchCase = Math.max(str1NotMatchCase, str2NotMatchCase);
                memoDP[str1Idx][str2Idx] = notMatchCase;
            }
        }
    }

    // console.log(memoDP);
    return memoDP[str1Len][str2Len];
};

/**
Not A Valid Thought Process -> What did I just do here?
/**
    while(str1Idx < str1Len || str2Idx < str2Len){
        if(text1[str1Idx] === text2[str2Idx]){
            let matchCase = 0;
            if(str1Idx > 0 && str2Idx > 0){
                matchCase = 1 + memoDP[str1Idx - 1][str2Idx - 1];
            }

            memoDP[str1Idx][str2Idx] = matchCase;
        }
        else{
            let str1NotMatchCase = 0;
            let str2NotMatchCase = 0;

            if(str1Idx > 0){
                str1NotMatchCase = memoDP[str1Idx - 1][str2Idx];
            }
            if(str2Idx > 0){
                str2NotMatchCase = memoDP[str1Idx][str2Idx - 1];
            }

            console.log(str1Idx, str2Idx);
            const notMatchCase = Math.max(str1NotMatchCase, str2NotMatchCase);
            memoDP[str1Idx][str2Idx] = notMatchCase;
        }

        if(str1Idx < str1Len){
            str1Idx += 1;
        }
        if(str2Idx < str2Len){
            str2Idx += 1;
        }
    }
*/