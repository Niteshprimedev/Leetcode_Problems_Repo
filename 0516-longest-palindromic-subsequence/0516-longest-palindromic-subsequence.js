/**
 * @param {string} s
 * @return {number}
 */
var longestPalindromeSubseq = function(s) {
    /** 
    // Top Down Solution1 :
    // Logic: Find the Longest Common Subsequence 
    // in the  string s and reverse string revS

    const reverseStrS = s.split('').reverse().join('');
    
    const str1Len = s.length;
    const str2Len = reverseStrS.length;

    const memoDP = new Array(str1Len).fill(-1).map(() => new Array(str2Len).fill(-1));

    function allSubseqsLen(str1Idx, str2Idx){
        // Base Case:
        if(str1Idx < 0 || str2Idx < 0){
            return 0;
        }

        // Memo Case: The result is already computed so return na:
        if(memoDP[str1Idx][str2Idx] !== -1){
            return memoDP[str1Idx][str2Idx];
        }

        // Match Case:
        if(s[str1Idx] === reverseStrS[str2Idx]){
            const matchCaseSubSeqLen = 1 + allSubseqsLen(str1Idx - 1, str2Idx - 1);
            memoDP[str1Idx][str2Idx] = matchCaseSubSeqLen;
            return memoDP[str1Idx][str2Idx];
        }

        const skipStr1SubseqLen = allSubseqsLen(str1Idx - 1, str2Idx);
        const skipStr2SubseqLen = allSubseqsLen(str1Idx, str2Idx -  1);

        memoDP[str1Idx][str2Idx] = Math.max(skipStr1SubseqLen, skipStr2SubseqLen);
        return memoDP[str1Idx][str2Idx];
    }

    // We don't need to check the subsequences to be palindromes cause 
    // They are already palindromes so we just need to find the longest common
    // subsequences;
    return allSubseqsLen(str1Len - 1, str2Len - 1);
    */

    // Top Down Solution 2:
    // With shifting 1 index to the right
    // Logic: Find the Longest Common Subsequence 
    // in the  string s and reverse string revS

    const reverseStrS = s.split('').reverse().join('');
    
    const str1Len = s.length;
    const str2Len = reverseStrS.length;

    const memoDP = new Array(str1Len + 1).fill(-1).map(() => new Array(str2Len + 1).fill(-1));

    function allSubseqsLen(str1Idx, str2Idx){
        // Base Case:
        if(str1Idx === 0 || str2Idx === 0){
            return 0;
        }

        // Memo Case: The result is already computed so return na:
        if(memoDP[str1Idx][str2Idx] !== -1){
            return memoDP[str1Idx][str2Idx];
        }

        // Match Case:
        if(s[str1Idx - 1] === reverseStrS[str2Idx - 1]){
            const matchCaseSubSeqLen = 1 + allSubseqsLen(str1Idx - 1, str2Idx - 1);
            memoDP[str1Idx][str2Idx] = matchCaseSubSeqLen;
            return memoDP[str1Idx][str2Idx];
        }

        const skipStr1SubseqLen = allSubseqsLen(str1Idx - 1, str2Idx);
        const skipStr2SubseqLen = allSubseqsLen(str1Idx, str2Idx -  1);

        memoDP[str1Idx][str2Idx] = Math.max(skipStr1SubseqLen, skipStr2SubseqLen);
        return memoDP[str1Idx][str2Idx];
    }

    // We don't need to check the subsequences to be palindromes cause 
    // They are already palindromes so we just need to find the longest common
    // subsequences;
    return allSubseqsLen(str1Len, str2Len);
};