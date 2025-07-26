/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    /**
    // Solution 1: Using Map & Built in Sorting Algo
    const sortedWordsKeyMap = new Map();

    for(let str of strs){
        const hashKey = str.split("").sort().join('');
        let hashValue = [];

        const isHashkeyNotPresent = sortedWordsKeyMap.has(hashKey) !== true;
        if(isHashkeyNotPresent){
            sortedWordsKeyMap.set(hashKey, hashValue);
        }

        hashValue = sortedWordsKeyMap.get(hashKey);
        hashValue.push(str);

        sortedWordsKeyMap.set(hashKey, hashValue);
    }

    return [...sortedWordsKeyMap.values()];
    */

    // Solution 2: Using Map & MergeSort Algo

    function merge(strtIdx, midIdx, endIdx, strArr){
        const mergedArr = [];

        let idxI = strtIdx;
        let idxJ = midIdx + 1;

        while (idxI <= midIdx && idxJ <= endIdx){
            if(strArr[idxI].charCodeAt(0) <= strArr[idxJ].charCodeAt(0)){
                mergedArr.push(strArr[idxI]);
                idxI += 1;
            }
            else{
                mergedArr.push(strArr[idxJ]);
                idxJ += 1;
            }
        }

        while(idxI <= midIdx){
            mergedArr.push(strArr[idxI]);
            idxI += 1;
        }

        while(idxJ <= midIdx){
            mergedArr.push(strArr[idxJ]);
            idxJ += 1;
        }

        for(let idx = 0; idx < mergedArr.length; idx++){
            strArr[idx + strtIdx] = mergedArr[idx];
        }

        return strArr;
    }

    function mergeSort(strtIdx, endIdx, strArr){
        if(strtIdx < endIdx){
            const midIdx = strtIdx + Math.floor((endIdx - strtIdx)/2)

            mergeSort(strtIdx, midIdx, strArr);
            mergeSort(midIdx + 1, endIdx, strArr);

            merge(strtIdx, midIdx, endIdx, strArr);
        }

        return strArr;
    }
    
    const sortedWordsKeyMap = new Map();

    for(let str of strs){
        const hashKey = mergeSort(0, str.length - 1, str.split("")).join('');
        let hashValue = [];

        const isHashkeyNotPresent = sortedWordsKeyMap.has(hashKey) !== true;
        if(isHashkeyNotPresent){
            sortedWordsKeyMap.set(hashKey, hashValue);
        }

        hashValue = sortedWordsKeyMap.get(hashKey);
        hashValue.push(str);

        sortedWordsKeyMap.set(hashKey, hashValue);
    }

    return [...sortedWordsKeyMap.values()];
};