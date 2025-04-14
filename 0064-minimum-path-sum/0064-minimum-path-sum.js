/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    /** 
    // Logic: Recurrence Relation:
    // Step1: Express the problem in terms of indices
    // Step2: Do all the stuff on that index;
    // Step3: Return the min of topPathSum and leftPathSum;

    const mRows = grid.length - 1;
    const nCols = grid[0].length - 1;
    let minPathSum = Infinity;

    const memoDP = new Array(mRows + 1).fill(0).map(() => new Array(nCols + 1).fill(-1));

    function allPathsSum(mRows, nCols){


        // Base Case:
        if(mRows === 0 && nCols === 0){

            return grid[mRows][nCols];
        }

        // If we go beyond the left & top boundary:
        // Then it's an invalid path;
        if(mRows < 0 || nCols < 0){
            return Infinity;
        }

        if(memoDP[mRows][nCols] !== -1){
            return memoDP[mRows][nCols];
        }

        const topPathSum =  grid[mRows][nCols] + allPathsSum(mRows, nCols - 1);
        const leftPathSum = grid[mRows][nCols] + allPathsSum(mRows - 1, nCols);

        memoDP[mRows][nCols] = Math.min(topPathSum, leftPathSum);

        return memoDP[mRows][nCols];
    }
    minPathSum = allPathsSum(mRows, nCols);

    // console.log(memoDP, memoDP[0][0])

    return minPathSum;
    */

    // Bottom Up Approach:
    // To convert TOP DOWN TO BOTTOM UP:
    // You need to follow below steps:
    // 1) Declare Base Case First as it is and probably intialize DP at that indices
    // 2) Express all states in for loops
    // 3) Copy the recurrence and write it in terms of DP;

    const mRows = grid.length;
    const nCols = grid[0].length;

    // Initialize DP table
    const memoDP = new Array(mRows).fill(0).map(() => new Array(nCols).fill(-1));

    // The memo Base Case for Tabulation;
    memoDP[0][0] = grid[0][0];

    for(let rowIdx = 0; rowIdx < mRows; rowIdx++){
        for(let colIdx = 0; colIdx < nCols; colIdx++){
            if(rowIdx === 0 && colIdx === 0){
                memoDP[rowIdx][colIdx] = grid[0][0];
            }
            else{

                // Default paths are Infinity
                // Meaning, if don't have a left path or a top path then the 
                // default path value will be infinity for them;
                // Top Path: The top 
                let topPathSum = Infinity;
                // Left Path:
                let leftPathSum = Infinity;

                // Calculate the topPathsum by getting the top row value and the current
                // cell value
                if(rowIdx > 0){
                    topPathSum = grid[rowIdx][colIdx] + memoDP[rowIdx - 1][colIdx];
                }
                // Calculate the leftPathsum by getting the left col value and the current
                // cell value
                if(colIdx > 0){
                    leftPathSum = grid[rowIdx][colIdx] + memoDP[rowIdx][colIdx - 1];
                }

                // Minimum of the two paths: How do we get to the minimum path sum 
                // for the current cell: by checking the min of topPath and leftPath
                memoDP[rowIdx][colIdx] = Math.min(topPathSum, leftPathSum);
            }

        }
    }

    // console.log(memoDP);
    return memoDP[mRows - 1][nCols - 1];
};