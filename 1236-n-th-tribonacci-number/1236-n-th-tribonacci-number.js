/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
    // Base Cases;
    if(n === 0) return 0;
    if(n === 1 || n === 2) return 1;

    const memoDP = new Array(n + 1).fill(0);

    memoDP[0] = 0;
    memoDP[1] = 1;
    memoDP[2] = 1;

    // Bottom Up Approach;
    let seqIdx = 0;
    for(let idxI = 3; idxI <=n; idxI++){
        memoDP[idxI] = memoDP[seqIdx] + memoDP[seqIdx + 1] + memoDP[seqIdx + 2];
        seqIdx++;
    }

    // console.log(memoDP);
    return memoDP[n];
};