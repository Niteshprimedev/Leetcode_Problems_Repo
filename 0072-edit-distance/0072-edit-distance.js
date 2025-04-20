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

    /**
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
    */
    
    // Space Optimized Bottom Up Approach:
    // With the right shift of indices by 1;
    const str1Len = word1.length;
    const str2Len = word2.length;

    // const memoDP = new Array(str1Len + 1).fill(-1).map(() => new Array(str2Len + 1).fill(-1));
    // Initialize the first row: "" to word2 (insert all chars)
    let prevDP = new Array(str2Len + 1).fill(0);

    // Base Case:
    // for(let str1Idx = 0; str1Idx <= str1Len; str1Idx++){
    //     prevDP[str1Idx] = str1Idx;
    // }

     // Loop over each character in word1 (rows)
    for(let str2Idx = 0; str2Idx <= str2Len; str2Idx++){
        prevDP[str2Idx] = str2Idx; // Only Column data to be updated for base case
    }

    // For Loops:
    for(let str1Idx = 1; str1Idx <= str1Len; str1Idx++){
        const currDP = new Array(str2Len + 1).fill(0);

        // First col: from word1[0..i-1] to "" => i deletions
        currDP[0] = str1Idx; // \U0001f448 Base case for column-0 (delete all chars from word1[0..str1Idx-1])
        for(let str2Idx = 1; str2Idx <= str2Len; str2Idx++){

            if(word1[str1Idx - 1] === word2[str2Idx - 1]){
                const matchCaseOps = prevDP[str2Idx - 1];

                // Characters match, no operation needed
                currDP[str2Idx] = matchCaseOps;
            }
            else{
                // We can do Insert (←), Delete (↑), or Replace (↖)
                // Insert a char Operation:
                const insertCaseOps = 1 + currDP[str2Idx - 1]; // insert ch2 into word1

                // Delete a char Operation:
                const deleteCaseOps = 1 + prevDP[str2Idx]; // delete ch1 from word1

                // Repalce a char Operation:
                const replaceCaseOps = 1 + prevDP[str2Idx - 1]; // replace ch1 with ch2

                let allOpsMinOps = Math.min(insertCaseOps, deleteCaseOps);
                allOpsMinOps = Math.min(allOpsMinOps, replaceCaseOps);

                // Characters don't match, calculate min num of operations needed
                currDP[str2Idx] = allOpsMinOps;
            }
        }

        // After this row is done, update prevDP to currDP
        prevDP = currDP;
    }

    // Final answer is the last cell (full word1 → full word2)
    // console.log(prevDP);
    return prevDP[str2Len];
};