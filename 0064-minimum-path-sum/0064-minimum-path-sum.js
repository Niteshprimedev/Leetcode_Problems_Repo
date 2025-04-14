/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    
    // Bottom Up Approach:
    // To convert TOP DOWN TO BOTTOM UP:
    // You need to follow below steps:
    // 1) Declare Base Case First as it is and probably intialize DP at that indices
    // 2) Express all states in for loops
    // 3) Copy the recurrence and write it in terms of DP;

    // SPACE OPTIMIZATION; when you don't need to carry entire DP array but
    // just the prevRow of the memoDP; so carry that only to optimize space;

    const mRows = grid.length;
    const nCols = grid[0].length;

    // Initialize DP table
    let prevDP = new Array(nCols).fill(Infinity);

    for(let rowIdx = 0; rowIdx < mRows; rowIdx++){

        // The memo Base Case for Tabulation;
        const currDP = new Array(nCols).fill(0);

        for(let colIdx = 0; colIdx < nCols; colIdx++){
            if(rowIdx === 0 && colIdx === 0){
                currDP[colIdx] = grid[0][0];
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
                    topPathSum = grid[rowIdx][colIdx] + prevDP[colIdx];
                }
                // Calculate the leftPathsum by getting the left col value and the current
                // cell value
                if(colIdx > 0){
                    leftPathSum = grid[rowIdx][colIdx] + currDP[colIdx - 1];
                }

                // Minimum of the two paths: How do we get to the minimum path sum 
                // for the current cell: by checking the min of topPath and leftPath
                currDP[colIdx] = Math.min(topPathSum, leftPathSum);
            }
        }

        prevDP = currDP;
    }

    // console.log(prevDP);
    return prevDP[nCols - 1];
};