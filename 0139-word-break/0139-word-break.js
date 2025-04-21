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
    // Solution 1 - Top Down Approach Solution:
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

    /**
    // Solution 2 - Top Down Approach Solution:
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
    */

    /**
    // Solution - 3 Top Down Approach Solution:
    // With moving idx 1 to the right;
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
        if(currIdx === 0){
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
            breakWordAndNewSeq = allSeqsWords(currIdx - 1, s[currIdx - 1]);
        }

        const continuousStrSeq = allSeqsWords(currIdx - 1, s[currIdx - 1] + currStr);

        const isBreakingOrContinueGivesSeq = breakWordAndNewSeq || continuousStrSeq;
        memoMap.set(hashKey, isBreakingOrContinueGivesSeq);

        return isBreakingOrContinueGivesSeq;
    }
    return allSeqsWords(strLen, '');
    */

    // Solution - 4 Top Down Approach Solution:
    // Without using the currStr & only Indices, Also moving idx 1 to the right;
    const strLen = s.length;
    const wordsDictMap = new Map();

    for(let word of wordDict){
        wordsDictMap.set(word, true);
    }

    // console.log(wordsDictMap);

    const memoDP = new Array(strLen + 1).fill(-1).map(() => new Array(strLen).fill(-1));

    function allSeqsWords(currIdx, endPosIdx){
        // Base Case:
        const currStr = s.slice(currIdx, endPosIdx + 1);
        if(currIdx === 0){
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

        // const hashKey = `${currIdx}-${endPosIdx}`;
        if(memoDP[currIdx][endPosIdx] !== -1){
            return memoDP[currIdx][endPosIdx];
        }

        let breakWordAndNewSeq = false;
        const isWordPresent = wordsDictMap.has(currStr);
        if(isWordPresent){
            breakWordAndNewSeq = allSeqsWords(currIdx - 1, currIdx - 1);
        }

        const continuousStrSeq = allSeqsWords(currIdx - 1, endPosIdx);

        const isBreakingOrContinueGivesSeq = breakWordAndNewSeq || continuousStrSeq;
        memoDP[currIdx][endPosIdx] = isBreakingOrContinueGivesSeq;

        return isBreakingOrContinueGivesSeq;
    }
    return allSeqsWords(strLen, strLen - 1);

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

    // For Loops:
    let currStr = '';
    for(let currIdx = 0; currIdx <= strLen; currIdx++){
        for(let char of s){
            // Base Case:
            const hashKey = `${currIdx}-${currStr}`;
            if(currIdx === 0){
                const isWordPresent = wordsDictMap.has(currStr);
                if(isWordPresent){
                    memoMap.set(hashKey, true);
                    currStr = '';
                }
                else{
                    memoMap.set(hashKey, false);
                }
            }
            else{

                let breakWordAndNewSeq = false;
                const isWordPresent = wordsDictMap.has(currStr);
                if(isWordPresent){
                    const hashKey1 = `${currIdx - 1}-${s[currIdx - 1]}`;
                    breakWordAndNewSeq = memoMap.get(hashKey1) || false;
                    currStr = '';
                }

                const hashKey2 = `${currIdx - 1}-${s[currIdx - 1] + currStr}`;
                const continuousStrSeq = memoMap.get(hashKey2) || false;

                const isBreakingOrContinueGivesSeq = breakWordAndNewSeq || continuousStrSeq;
                memoMap.set(hashKey, isBreakingOrContinueGivesSeq);
            }
            currStr += char;
        }
    }
    const hashKey = `${strLen}-''`;
    return memoMap.get(hashKey) || false;
    */
    /** 
    const strLen = s.length;
    const wordsDictMap = new Map();
    for (let word of wordDict) {
        wordsDictMap.set(word, true);
    }

    const memoMap = new Map();

    // Start with empty string at position 0
    memoMap.set(`0-`, true);

    for (let i = 0; i < strLen; i++) {
        for (let j = i + 1; j <= strLen; j++) {
            const currStr = s.slice(i, j); // substring from i to j-1
            const hashKeyBefore = `${i}-`;
            const hashKeyNow = `${j}-`;

            if (wordsDictMap.has(currStr) && memoMap.get(hashKeyBefore)) {
                memoMap.set(hashKeyNow, true);
            }
        }
    }

    return memoMap.get(`${strLen}-`) || false;
    */
};