/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    // SAME Logic as finding the maximum rectangle area in a histogram
    // Just need to make sure that the height and the width are same;

    // Logic: Not using the leftSmallerElIdx Arr and rightSmallerElIdx Arr
    // cause the stack is helping us to get the leftSmaller element and the
    // rightSmaller element for the popped stack element;
    // The element that is popped will have its left Smaller element either as the 
    // next lastIdx element in the stack or if stack is empty then 0;
    // The element that is popped will have its right Smaller element either as 
    // the current smaller element that is about to push in the stack or
    // the heightsLen - 1

    // Intuition:
    // We use a monotonic increasing stack to track indices of bars. 
    // When we encounter a shorter bar, we pop taller bars and calculate area 
    // using the popped height and distance to nearest smaller bars on both sides.

    function largestSqArea(sqHeights){
        let maxSqArea = 0;
        const heightsLen = sqHeights.length;

        const prevSmallerElStack = []; // Stores indices of bars in increasing order of height
        for(let heightIdx = 0; heightIdx < heightsLen; heightIdx++){
            const currHeight = sqHeights[heightIdx];

            let lastIdx = prevSmallerElStack.length - 1;
            // Pop all taller or equal bars, calculate area with each
            while(prevSmallerElStack.length > 0 && sqHeights[prevSmallerElStack[lastIdx]] >= currHeight){

                const prevElIdx = prevSmallerElStack.pop();
                lastIdx = prevSmallerElStack.length - 1;

                const newMaxSqArea = findNewMaxSqArea(prevElIdx, heightIdx, lastIdx);
                
                maxSqArea = Math.max(maxSqArea, newMaxSqArea);
            }
            // Push current bar index
            prevSmallerElStack.push(heightIdx);
        }

        // Calculate Area for remaining bars
        while(prevSmallerElStack.length > 0){

            const prevElIdx = prevSmallerElStack.pop();
            let lastIdx = prevSmallerElStack.length - 1;
            
            // Right boundary is end of array, if heights are traversed first;
            const newMaxSqArea = findNewMaxSqArea(prevElIdx, heightsLen, lastIdx);
            
            maxSqArea = Math.max(maxSqArea, newMaxSqArea);
        }

        // Helper function to calculate rectangle area
        function findNewMaxSqArea(prevElIdx, heightIdx, lastIdx){
            let leftSmallerElIdx = 0;
            let rightSmallerElIdx = heightsLen - 1;

            const prevElHeight = sqHeights[prevElIdx];
            
            // If stack is empty, left boundary is -1
            leftSmallerElIdx = lastIdx < 0 ? -1 : prevSmallerElStack[lastIdx];
            rightSmallerElIdx = heightIdx;
            
            const currWidth = rightSmallerElIdx - leftSmallerElIdx - 1; // Distance between smaller bars
            const sqAreaVal = Math.min(prevElHeight, currWidth);
            const newMaxSqArea = sqAreaVal ** 2;

            // Debugger Beauty goes here:
            // console.log(`Height: ${currHeight}, Width: ${currWidth}, Area: ${newMaxSqArea}`);
            return newMaxSqArea;
        }

        return maxSqArea;

        /** 

        // Striver Version:
        for(let heightIdx = 0; heightIdx <= heightsLen; heightIdx++){
            while(prevSmallerElStack.length > 0 && (heightIdx === heightsLen || sqHeights[prevSmallerElStack.length - 1] >= sqHeights[heightIdx])){
                const prevElHeight = sqHeights[prevSmallerElStack.length - 1];
                prevSmallerElStack.pop();

                let currWidth;
                if(prevSmallerElStack.length === 0){
                    currWidth = heightIdx;
                }
                else{
                    currWidth = heightIdx - prevSmallerElStack[prevSmallerElStack.length - 1] - 1;
                }

                const sqAreaVal = Math.min(prevElHeight, currWidth);
                const newMaxSqArea = sqAreaVal ** 2;

                maxSqArea = Math.max(maxSqArea, newMaxSqArea);
            }

            prevSmallerElStack.push(heightIdx);
        }

        return maxSqArea;
        */
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