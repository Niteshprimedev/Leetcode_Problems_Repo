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

            if(prevSmallerElStack.length > 0){
                let prevIdx = prevSmallerElStack.pop();
                while(sqHeights[prevIdx] >= currHeight && prevSmallerElStack.length > 0){
                    prevIdx = prevSmallerElStack.pop();
                }

                if(sqHeights[prevIdx] < currHeight){
                    prefixLeft.push(prevIdx + 1);
                    prevSmallerElStack.push(prevIdx);
                }
                else{
                    prefixLeft.push(0);
                }
            }
            else{
                prefixLeft.push(0);
            }

            prevSmallerElStack.push(idxI);
        }

        prevSmallerElStack = [];

        for(let idxI = heightsLen - 1; idxI >= 0; idxI--){
            const currHeight = sqHeights[idxI];

            const leftSmallerElIdx = prefixLeft[idxI];
            let rightSmallerElIdx;

            if(prevSmallerElStack.length > 0){
                let prevIdx = prevSmallerElStack.pop();
                while(sqHeights[prevIdx] >= currHeight && prevSmallerElStack.length > 0){
                    prevIdx = prevSmallerElStack.pop();
                }

                if(sqHeights[prevIdx] < currHeight){
                    rightSmallerElIdx = prevIdx - 1;
                    prevSmallerElStack.push(prevIdx);
                }
                else{
                    rightSmallerElIdx = heightsLen - 1;
                }
            }
            else{
                rightSmallerElIdx = heightsLen - 1;
            }

            const currWidth = Math.abs(leftSmallerElIdx - rightSmallerElIdx) + 1;

            const sqAreaVal = Math.min(currHeight, currWidth);
            const newMaxSqArea = sqAreaVal ** 2;

            maxSqArea = Math.max(maxSqArea, newMaxSqArea);
            prevSmallerElStack.push(idxI);
        }

        return maxSqArea;
    }

    // const matricesMaxSqArea = largestSqArea([2,1,5,6,2,3]);
    // console.log(matricesMaxSqArea);
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