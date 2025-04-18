/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    /**
    Did not actually work: Wrong Thought Process::: D
    // Area: Height * Width
    let maxRectArea = 0;
    let minHeight = Infinity;
    let maxWidth = 0;

    for(height of heights){ 
        if(height === 0){
            maxWidth = 0;
        }
        else{
            maxWidth += 1;
        }
        minHeight = Math.min(minHeight, height);
        const newMaxRectArea = minHeight * maxWidth;

        maxRectArea = Math.max(maxRectArea, newMaxRectArea);
    }

    return maxRectArea;
    */

    /** 
    // Brute Force Solution:
    let maxRectArea = -Infinity;

    for(let heightIdx = 0; heightIdx < heights.length; heightIdx++){
        const currHeight = heights[heightIdx];
        let maxWidth = 1;

        for(let idxJ = heightIdx - 1; idxJ >= 0; idxJ--){
            const prevHeight = heights[idxJ];
            if(prevHeight >= currHeight){
                maxWidth += 1;
            }
            else{
                break;
            }
        }

        for(let idxJ = heightIdx + 1; idxJ < heights.length; idxJ++){
            const nextHeight = heights[idxJ];
            if(nextHeight >= currHeight){
                maxWidth += 1;
            }
            else{
                break;
            }
        }
        
        let newMaxRectArea = currHeight * maxWidth;
        maxRectArea = Math.max(maxRectArea, newMaxRectArea);
    }

    return maxRectArea;
    */

    // Better Solution:
    // How many elements are bigger than and equal to the current Height
    // both on the left side  and the right side;
    // Using the Next Greater Element Logic & Stack:
    // Previous Smaller Element && Next Smaller Element;
    // Doing it in O(N) Auxiliary space only and not with prefixLeft & suffixRight;

    // Intuition:
    // We use a monotonic increasing stack to track indices of bars. 
    // When we encounter a shorter bar, we pop taller bars and calculate area 
    // using the popped height and distance to nearest smaller bars on both sides.

    let maxRectArea = 0;
    const previousSmallerElsStack = []; // Stores indices of bars in increasing order of height
    const heightsLen = heights.length;

    for(let heightIdx = 0; heightIdx < heightsLen; heightIdx++){
        if(previousSmallerElsStack.length > 0){
            let lastStackIdx = previousSmallerElsStack.length - 1;

            // Pop all taller or equal bars, calculate area with each
            while(previousSmallerElsStack.length > 0 && heights[previousSmallerElsStack[lastStackIdx]] >= heights[heightIdx]){
                const prevElIdx = previousSmallerElsStack.pop();
                lastStackIdx = previousSmallerElsStack.length - 1;

                const newMaxRectArea = calcRectArea(prevElIdx, heightIdx, lastStackIdx);
                maxRectArea = Math.max(maxRectArea, newMaxRectArea);
            }
        }

        // Push current bar index
        previousSmallerElsStack.push(heightIdx);
    }

    // Calculate Area for remaining bars
    while(previousSmallerElsStack.length > 0){
        const prevElIdx = previousSmallerElsStack.pop();
        let lastStackIdx = previousSmallerElsStack.length - 1;

        // Right boundary is end of array, if heights are traversed first;
        const newMaxRectArea = calcRectArea(prevElIdx, heightsLen, lastStackIdx);

        maxRectArea = Math.max(maxRectArea, newMaxRectArea);
    }

    // Helper function to calculate rectangle area
    function calcRectArea(prevElIdx, heightIdx, lastStackIdx){
        // If stack is empty, left boundary is -1
        const leftSmallerElIdx = lastStackIdx < 0 ? -1 : previousSmallerElsStack[lastStackIdx];
        const rightSmallerElIdx = heightIdx;

        const currHeight = heights[prevElIdx];
        const currWidth = rightSmallerElIdx - leftSmallerElIdx - 1; // Distance between smaller bars

        const newMaxRectArea = currHeight * currWidth;

        // Debugger Beauty goes here:
        // console.log(`Height: ${currHeight}, Width: ${currWidth}, Area: ${newMaxRectArea}`);
        return newMaxRectArea;
    }

    // console.log(maxRectArea);
    return maxRectArea;
};