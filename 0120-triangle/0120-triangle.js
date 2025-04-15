/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    /** 
    // TOP Down Approach:
    let rowsLen = triangle.length;
    const memoDP = new Array(rowsLen).fill(0).map((currEl, idx) => new Array(idx + 1).fill(0));

    function allPathsSumDFS(currIdx, currRowLen){
        // Base Case:
        if(currRowLen >= rowsLen || currIdx >= triangle[currRowLen].length){
            return 0;
        }

        if(memoDP[currRowLen][currIdx] !== 0){
            return memoDP[currRowLen][currIdx];
        }

        // Choose the currentIdx 
        const choseCurrIdx = triangle[currRowLen][currIdx] + allPathsSumDFS(currIdx, currRowLen + 1);

        // Choose the nextIdx
        const choseNextIdx = triangle[currRowLen][currIdx] + allPathsSumDFS(currIdx + 1, currRowLen + 1);

        memoDP[currRowLen][currIdx] = Math.min(choseCurrIdx, choseNextIdx);
        return memoDP[currRowLen][currIdx];
    }

    allPathsSumDFS(0, 0);

    // console.log(memoDP);

    return memoDP[0][0];
    */
    
    /**
    // Bottom Up Approach;
    // If we are goingg from 0 to n in Top Down, then
    // we need to go from n to 0 in Bottom up!

    let rowsLen = triangle.length;
    const memoDP = new Array(rowsLen).fill(0).map((currEl, idx) => new Array(idx + 1).fill(0));
    
    // console.log(memoDP);
    // Base Case:
    // memoDP[0][0] = triangle[0][0];
    for(let colIdx = 0; colIdx < rowsLen; colIdx++){
        memoDP[rowsLen - 1][colIdx] = triangle[rowsLen - 1][colIdx];
    }

    for(let rowIdx = rowsLen - 2; rowIdx >= 0; rowIdx--){
        for(colIdx = rowIdx; colIdx >= 0; colIdx--){
            // Choose the currentIdx 
            const choseCurrIdx = triangle[rowIdx][colIdx] + memoDP[rowIdx + 1][colIdx];

            // Choose the nextIdx
            const choseNextIdx = triangle[rowIdx][colIdx] + memoDP[rowIdx + 1][colIdx + 1];

            memoDP[rowIdx][colIdx] = Math.min(choseCurrIdx, choseNextIdx);
        }
    }   

    // console.log(memoDP);

    return memoDP[0][0];
    */

    // Space Optimized Bottom Up Approach;
    // If we are goingg from 0 to n in Top Down, then
    // we need to go from n to 0 in Bottom up!

    let rowsLen = triangle.length;
    let prevDP = new Array(rowsLen).fill(0);
    
    // console.log(prevDP);
    // Base Case:
    // prevDP[0] = triangle[0][0];
    for(let colIdx = 0; colIdx < rowsLen; colIdx++){
        prevDP[colIdx] = triangle[rowsLen - 1][colIdx];
    }

    for(let rowIdx = rowsLen - 2; rowIdx >= 0; rowIdx--){
        const currDP = new Array(rowIdx + 1).fill(0);
        console.log(currDP.length, rowIdx, currDP);

        for(colIdx = rowIdx; colIdx >= 0; colIdx--){
            // Choose the currentIdx 
            const choseCurrIdx = triangle[rowIdx][colIdx] + prevDP[colIdx];

            // Choose the nextIdx
            const choseNextIdx = triangle[rowIdx][colIdx] + prevDP[colIdx + 1];

            currDP[colIdx] = Math.min(choseCurrIdx, choseNextIdx);
        }

        prevDP = currDP;
    }   

    // console.log(memoDP);

    return prevDP[0];
};