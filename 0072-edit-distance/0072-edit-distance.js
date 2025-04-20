/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    /** 
    // Top Down Approach:
    // With -1 to n - 1 iteration;
    const str1Len = word1.length;
    const str2Len = word2.length;

    const memoDP = new Array(str1Len).fill(-1).map(() => new Array(str2Len).fill(-1));

    function allStrOps(str1Idx, str2Idx){   
        // Base Case:
        if(str2Idx < 0){
            return str1Idx + 1;
        }
        
        if(str1Idx < 0 && str2Idx >= 0){
            return str2Idx + 1;
        }


        if(memoDP[str1Idx][str2Idx] !== -1){
            return memoDP[str1Idx][str2Idx];
        }

        if(word1[str1Idx] === word2[str2Idx]){
            const matchCaseOps = 0 + allStrOps(str1Idx - 1, str2Idx - 1);
            memoDP[str1Idx][str2Idx] = matchCaseOps;
            return matchCaseOps;
        }

        // Insert a char Operation:
        const insertOpsCase = 1 + allStrOps(str1Idx, str2Idx - 1);

        // Delete a char Operation:
        const deleteOpsCase = 1 + allStrOps(str1Idx - 1, str2Idx);

        // Repalce a char Operation:
        const replaceOpsCase = 1 + allStrOps(str1Idx - 1, str2Idx - 1);

        let allOpsMinOps = Math.min(insertOpsCase, deleteOpsCase);
        allOpsMinOps = Math.min(allOpsMinOps, replaceOpsCase);

        // console.log(memoDP);
        memoDP[str1Idx][str2Idx] = allOpsMinOps;
        return allOpsMinOps;
    }
    return allStrOps(str1Len - 1, str2Len - 1);
    */

    /**
    // Top Down Approach:
    // With the right shift of indices by 1;
    const str1Len = word1.length;
    const str2Len = word2.length;

    const memoDP = new Array(str1Len + 1).fill(-1).map(() => new Array(str2Len + 1).fill(-1));

    function allStrOps(str1Idx, str2Idx){   
        // Base Case:
        if(str2Idx === 0){
            return str1Idx; // Idx are now 1 based;
        }
        
        if(str1Idx === 0 && str2Idx >= 0){
            return str2Idx; // Idx are now 1 based;
        }


        if(memoDP[str1Idx][str2Idx] !== -1){
            return memoDP[str1Idx][str2Idx];
        }

        // Now the last indicess are available at str1Idx - 1
        // str2Idx - 1
        if(word1[str1Idx - 1] === word2[str2Idx - 1]){
            const matchCaseOps = 0 + allStrOps(str1Idx - 1, str2Idx - 1);
            memoDP[str1Idx][str2Idx] = matchCaseOps;
            return matchCaseOps;
        }

        // Insert a char Operation:
        const insertOpsCase = 1 + allStrOps(str1Idx, str2Idx - 1);

        // Delete a char Operation:
        const deleteOpsCase = 1 + allStrOps(str1Idx - 1, str2Idx);

        // Repalce a char Operation:
        const replaceOpsCase = 1 + allStrOps(str1Idx - 1, str2Idx - 1);

        let allOpsMinOps = Math.min(insertOpsCase, deleteOpsCase);
        allOpsMinOps = Math.min(allOpsMinOps, replaceOpsCase);

        // console.log(memoDP);
        memoDP[str1Idx][str2Idx] = allOpsMinOps;
        return allOpsMinOps;
    }
    return allStrOps(str1Len, str2Len);
    */

    // Bottom Up Approach:
    // With the right shift of indices by 1;
    const str1Len = word1.length;
    const str2Len = word2.length;

    const memoDP = new Array(str1Len + 1).fill(-1).map(() => new Array(str2Len + 1).fill(-1));

    // Base Case:
    for(let str1Idx = 0; str1Idx <= str1Len; str1Idx++){
        memoDP[str1Idx][0] = str1Idx;
    }

    for(let str2Idx = 0; str2Idx <= str2Len; str2Idx++){
        memoDP[0][str2Idx] = str2Idx;
    }

    // For Loops:
    for(let str1Idx = 1; str1Idx <= str1Len; str1Idx++){
        for(let str2Idx = 1; str2Idx <= str2Len; str2Idx++){
            
            if(word1[str1Idx - 1] === word2[str2Idx - 1]){
                const matchCaseOps = memoDP[str1Idx - 1][str2Idx - 1];
                memoDP[str1Idx][str2Idx] = matchCaseOps;
            }
            else{
                // Insert a char Operation:
                const insertCaseOps = 1 + memoDP[str1Idx][str2Idx - 1];

                // Delete a char Operation:
                const deleteCaseOps = 1 + memoDP[str1Idx - 1][str2Idx];

                // Repalce a char Operation:
                const replaceCaseOps = 1 + memoDP[str1Idx - 1][str2Idx - 1];

                let allOpsMinOps = Math.min(insertCaseOps, deleteCaseOps);
                allOpsMinOps = Math.min(allOpsMinOps, replaceCaseOps);

                memoDP[str1Idx][str2Idx] = allOpsMinOps;
            }
        }
    }

    // console.log(memoDP);
    return memoDP[str1Len][str2Len];
};