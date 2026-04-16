/**
 * @param {number[]} nums
 * @param {number[]} queries
 * @return {number[]}
 */
var solveQueries = function(nums, queries) {
    const numsElsIdxPrevNextHashmap = new Map();
    const numsElsIdxKeyAndNestedIdxVal = new Map();

    let currIdx = 0;
    for(let num of nums){
        const hashKey = num;
        let hashValue = [];

        const isNumHashKeyAdded = numsElsIdxPrevNextHashmap.has(hashKey) !== true;
        if(isNumHashKeyAdded){
            numsElsIdxPrevNextHashmap.set(hashKey, hashValue);
        }

        hashValue = numsElsIdxPrevNextHashmap.get(hashKey);

        updateElsNestedIdxHashmap(hashKey, currIdx, hashValue.length);
        
        hashValue.push(currIdx);
        numsElsIdxPrevNextHashmap.set(hashKey, hashValue);

        currIdx++;
    }    

    // console.log(numsElsIdxPrevNextHashmap);
    // console.log(numsElsIdxKeyAndNestedIdxVal);

    const queriesClosestEls = queries.map(query => {
        let minDistance = -1;
        const numHashKey = nums[query]; 

        const numsIndicesHashValue = numsElsIdxPrevNextHashmap.get(numHashKey);

        const indicesArrLen = numsIndicesHashValue.length; 
        if(indicesArrLen < 2){
            return minDistance;
        }

        const numHashValue = numsElsIdxKeyAndNestedIdxVal.get(numHashKey)[query];
        // numsElsQueryFreqHashmap.set(numHashKey, numHashValue);

        let prevIdx = numHashValue - 1;
        if(prevIdx < 0){
            prevIdx = numsIndicesHashValue.length - 1;
            prevIdx = numsIndicesHashValue[prevIdx];
            prevIdx = Math.abs(nums.length - prevIdx + query);
        }
        else{
            prevIdx = numHashValue - 1;
            prevIdx = numsIndicesHashValue[prevIdx];
            prevIdx = Math.abs(query - prevIdx);
        }
        let nextIdx = numHashValue + 1;
        
        if(nextIdx >= numsIndicesHashValue.length){
            nextIdx = nextIdx % (numsIndicesHashValue.length);
            nextIdx = numsIndicesHashValue[nextIdx];
            nextIdx = Math.abs(nums.length - query + nextIdx);
        }
        else{
            nextIdx = numsIndicesHashValue[nextIdx];
            nextIdx = Math.abs(query - nextIdx);
        }

        // prevIdx = 
        // prevIdx = Math.abs(query - prevIdx);
        // nextIdx = Math.abs(query - nextIdx);
        
        minDistance = Math.min(prevIdx, nextIdx);

        // console.log(query, 'pre', prevIdx, 'next', nextIdx);
        return minDistance;
    });

    function updateElsNestedIdxHashmap(hashKey, idxKey, idxValue){
        let hashValue = {};

        const isNestedIdxNotAdded = numsElsIdxKeyAndNestedIdxVal.has(hashKey) !== true;
        if(isNestedIdxNotAdded){
            numsElsIdxKeyAndNestedIdxVal.set(hashKey, hashValue);
        }
        hashValue = numsElsIdxKeyAndNestedIdxVal.get(hashKey);
        hashValue[idxKey] = idxValue;
        
        numsElsIdxKeyAndNestedIdxVal.set(hashKey, hashValue);
    }

    return queriesClosestEls;
    // return queries;
};