/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const sortedWordsKeyMap = new Map();

    for(let str of strs){
        const hashKey = str.split("").sort().join('');
        
        let hashValue = [];
        const isHashKeyNotPresent = sortedWordsKeyMap.has(hashKey) !== true;
        if(isHashKeyNotPresent){
            sortedWordsKeyMap.set(hashKey, hashValue);
        }

        hashValue = sortedWordsKeyMap.get(hashKey);
        hashValue.push(str);

        sortedWordsKeyMap.set(hashKey, hashValue);
    }

    return [...sortedWordsKeyMap.values()];
};