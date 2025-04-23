/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
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
        // console.log(currDP.length, rowIdx, currDP);

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