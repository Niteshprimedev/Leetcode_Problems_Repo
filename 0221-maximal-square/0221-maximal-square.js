/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    // SAME Logic as finding the maximum rectangle area in a histogram
    // Just need to make sure that the height and the width are same;

    function largestSqArea(sqHeights){
        let maxSqArea = 0;
        const heightsLen = sqHeights.length;

        const prefixLeft = [];

        let prevSmallerElStack = []

        for(let idxI = 0; idxI < heightsLen; idxI++){
            const currHeight = sqHeights[idxI];

            while(sqHeights[prevSmallerElStack[prevSmallerElStack.length - 1]] >= currHeight && prevSmallerElStack.length > 0){
                prevSmallerElStack.pop();
            }

            prefixLeft[idxI] = prevSmallerElStack.length === 0 ? 0 : prevSmallerElStack[prevSmallerElStack.length - 1] + 1;

            prevSmallerElStack.push(idxI);
        }

        // console.log(prefixLeft)

        prevSmallerElStack = [];

        for(let idxI = heightsLen - 1; idxI >= 0; idxI--){
            const currHeight = sqHeights[idxI];

            const leftSmallerElIdx = prefixLeft[idxI];
            let rightSmallerElIdx;

            while(sqHeights[prevSmallerElStack[prevSmallerElStack.length - 1]] >= currHeight && prevSmallerElStack.length > 0){
                prevSmallerElStack.pop();
            }

            rightSmallerElIdx = prevSmallerElStack.length === 0 ? heightsLen - 1 : prevSmallerElStack[prevSmallerElStack.length - 1] - 1;

            const currWidth = Math.abs(leftSmallerElIdx - rightSmallerElIdx) + 1;

            const sqAreaVal = Math.min(currHeight, currWidth);
            const newMaxSqArea = sqAreaVal ** 2;

            maxSqArea = Math.max(maxSqArea, newMaxSqArea);
            prevSmallerElStack.push(idxI);
        }

        return maxSqArea;
    }

    // const matricesMaxSqAreaT = largestSqArea([2,1,5,6,2,3]);
    // console.log(matricesMaxSqAreaT);
    let matricesMaxSqArea = 0;

    const mRows = matrix.length;
    const nCols = matrix[0].length;
    const sqHeights = new Array(nCols).fill(0);

    for(let rowIdx = 0; rowIdx < mRows; rowIdx++){
        for(let colIdx = 0; colIdx < nCols; colIdx++){
            const currCellVal = matrix[rowIdx][colIdx];

            if(Number(currCellVal) === 0){
                sqHeights[colIdx] = 0;
            }
            else{
                sqHeights[colIdx] += 1;
            }
        }

        const newMatricesMaxSqArea = largestSqArea(sqHeights);
        matricesMaxSqArea = Math.max(matricesMaxSqArea, newMatricesMaxSqArea);
    }

    return matricesMaxSqArea;
};