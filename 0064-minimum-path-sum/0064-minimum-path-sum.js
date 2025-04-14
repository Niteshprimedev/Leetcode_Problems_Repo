/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
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
};