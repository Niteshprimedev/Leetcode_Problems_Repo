/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function(s, wordDict) {
    // Solving using Hashmap & Traverse:

    // Not matched and hit the base case then 
    // it means the string can't be segmented into a space separated
    // sequence

    /**
    // Top Down Approach Solution:
    const strLen = s.length;
    const wordsDictMap = new Map();

    for(let word of wordDict){
        wordsDictMap.set(word, true);
    }

    // console.log(wordsDictMap);

    // const memoDP = new Array(strLen).fill(-1).map(() => new Array());
    const memoMap = new Map();

    function allSeqsWords(currIdx, currStr){
        // Base Case:
        if(currIdx === strLen){
            // currStr += s[0];
            // console.log(currStr);
            const isWordPresent = wordsDictMap.has(currStr);
            if(isWordPresent){
                return true;
            }
            else{
                return false;
            }
        }

        const hashKey = `${currIdx}-${currStr}`;
        if(memoMap.has(hashKey)){
            return memoMap.get(hashKey);
        }

        let breakWordAndNewSeq = false;
        const isWordPresent = wordsDictMap.has(currStr);
        if(isWordPresent){
            breakWordAndNewSeq = allSeqsWords(currIdx + 1, s[currIdx]);
        }

        const continuousStrSeq = allSeqsWords(currIdx + 1, currStr + s[currIdx]);

        const isBreakingOrContinueGivesSeq = breakWordAndNewSeq || continuousStrSeq;
        memoMap.set(hashKey, isBreakingOrContinueGivesSeq);

        return isBreakingOrContinueGivesSeq;
    }
    return allSeqsWords(0, '');

    */

    // Top Down Approach Solution:
    // Without moving idx 1 to the right;
    const strLen = s.length;
    const wordsDictMap = new Map();

    for(let word of wordDict){
        wordsDictMap.set(word, true);
    }

    // console.log(wordsDictMap);

    // const memoDP = new Array(strLen).fill(-1).map(() => new Array());
    const memoMap = new Map();

    function allSeqsWords(currIdx, currStr){
        // Base Case:
        if(currIdx < 0){
            // currStr += s[0];
            // console.log(currStr);
            const isWordPresent = wordsDictMap.has(currStr);
            if(isWordPresent){
                return true;
            }
            else{
                return false;
            }
        }

        const hashKey = `${currIdx}-${currStr}`;
        if(memoMap.has(hashKey)){
            return memoMap.get(hashKey);
        }

        let breakWordAndNewSeq = false;
        const isWordPresent = wordsDictMap.has(currStr);
        if(isWordPresent){
            breakWordAndNewSeq = allSeqsWords(currIdx - 1, s[currIdx]);
        }

        const continuousStrSeq = allSeqsWords(currIdx - 1, s[currIdx] + currStr);

        const isBreakingOrContinueGivesSeq = breakWordAndNewSeq || continuousStrSeq;
        memoMap.set(hashKey, isBreakingOrContinueGivesSeq);

        return isBreakingOrContinueGivesSeq;
    }
    return allSeqsWords(strLen - 1, '');
    
    /**
    // Bottom Up Approach Solution:
    const strLen = s.length;
    const wordsDictMap = new Map();

    for(let word of wordDict){
        wordsDictMap.set(word, true);
    }

    // console.log(wordsDictMap);

    // const memoDP = new Array(strLen).fill(-1).map(() => new Array());
    const memoMap = new Map();

    // Base Case:


    function allSeqsWords(currIdx, currStr){
        // Base Case:
        if(currIdx === strLen){
            // currStr += s[0];
            // console.log(currStr);
            const isWordPresent = wordsDictMap.has(currStr);
            if(isWordPresent){
                return true;
            }
            else{
                return false;
            }
        }

        const hashKey = `${currIdx}-${currStr}`;
        if(memoMap.has(hashKey)){
            return memoMap.get(hashKey);
        }

        let breakWordAndNewSeq = false;
        const isWordPresent = wordsDictMap.has(currStr);
        if(isWordPresent){
            breakWordAndNewSeq = allSeqsWords(currIdx + 1, s[currIdx]);
        }

        const continuousStrSeq = allSeqsWords(currIdx + 1, currStr + s[currIdx]);

        const isBreakingOrContinueGivesSeq = breakWordAndNewSeq || continuousStrSeq;
        memoMap.set(hashKey, isBreakingOrContinueGivesSeq);

        return isBreakingOrContinueGivesSeq;
    }
    return allSeqsWords(0, '');
    */
};