/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
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
};