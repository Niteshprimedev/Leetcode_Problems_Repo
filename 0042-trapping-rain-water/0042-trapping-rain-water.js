/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    /**
    const heightLen = height.length;

    // maxLeftBoundary[0] = height[0];
    // maxRightBoundary[heightLen - 1] = height[heightLen - 1];

    const maxLeftBoundary = new Array(heightLen).fill(0);
    const maxRightBoundary = new Array(heightLen).fill(0);

    let maxLeft = height[0];
    let maxRight = height[heightLen - 1];

    for(let idxI = 0; idxI < height.length; idxI++){
        const strtIdxEl = height[idxI];
        const endIdxEl = height[heightLen - 1 - idxI];

        if(strtIdxEl > maxLeft){
            maxLeft = strtIdxEl;
        }
        if(endIdxEl > maxRight){
            maxRight = endIdxEl;
        }

        maxLeftBoundary[idxI] = maxLeft;
        maxRightBoundary[heightLen - 1 - idxI] = maxRight;
    }

    // console.log(maxLeftBoundary, maxRightBoundary);

    const wallsBoundary = new Array(heightLen);

    for(let idxI = 0; idxI < heightLen; idxI++){
        const currBoundary = Math.min(maxLeftBoundary[idxI], maxRightBoundary[idxI]);

        wallsBoundary[idxI] = currBoundary;
    }

    // console.log(wallsBoundary);

    let totalTrappedRainWaterUnits = 0;

    let idxI = 0;
    for(let boundary of wallsBoundary){
        const waterTrappedUnit = boundary - height[idxI];

        idxI++;
        totalTrappedRainWaterUnits += waterTrappedUnit;
    }

    return totalTrappedRainWaterUnits;
    */

    // Solution 2: Using only suffix Max 
    const heightLen = height.length;

    const maxLeftBoundary = 0;
    const maxRightBoundary = new Array(heightLen).fill(0);

    let maxRight = height[heightLen - 1];

    for(let idxI = heightLen - 1; idxI >= 0; idxI--){
        const newMaxRight = height[idxI];

        if(newMaxRight > maxRight){
            maxRight = newMaxRight;
        }

        maxRightBoundary[idxI] = maxRight;
    }

    // console.log(maxRightBoundary);

    let totalTrappedRainWaterUnits = 0;
    let maxLeftHeight = height[0];

    for(let heightIdx = 0; heightIdx < heightLen; heightIdx++){
        const currentHeight = height[heightIdx];

        maxLeftHeight = Math.max(maxLeftHeight, currentHeight);
        const maxRightHeight = maxRightBoundary[heightIdx];

        const boundary = Math.min(maxLeftHeight, maxRightHeight);

        const waterTrappedUnit = boundary - currentHeight;

        totalTrappedRainWaterUnits += waterTrappedUnit;
    }

    return totalTrappedRainWaterUnits;
    
    /** 
    // Logic: First, we calculate the maxLeft Boundary 
    // traversing from the left, and the maxRight Boundary
    // traversing from the right
    // And at each leftIdx or rightIdx in the height array
    // we are calculating the trapped water units
    // based on the maxLeft or maxRight Boundaries
    // substracting the current leftIdx or rightIdx height
    // 
    // Initialize the trapped rain water to 0
    let totalTrappedRainWaterUnits = 0;
    const heightLen = height.length;

    // Initialize two pointer variables leftIdx and rightIdx
    let leftIdx = 0;
    let rightIdx = heightLen - 1;

    // Initialize two boundaries -> maxLeft, maxRight
    let maxLeftBoundary = -Infinity;
    let maxRightBoundary = -Infinity;

    // Run the loop while the leftIdx < rightIdx: 
    while(leftIdx < rightIdx){
        maxLeftBoundary = Math.max(maxLeftBoundary, height[leftIdx]);
        maxRightBoundary = Math.max(maxRightBoundary, height[rightIdx]);

        // Calculate the the trapped water units based on the leftMax
        // & left height;
        if(maxLeftBoundary < maxRightBoundary){
            totalTrappedRainWaterUnits += maxLeftBoundary - height[leftIdx];
            leftIdx++;
        }
        // Calculate the trapped water units based on the rightMax
        // & right height;
        else {
            totalTrappedRainWaterUnits += maxRightBoundary - height[rightIdx];
            rightIdx--;
        }
    }

    return totalTrappedRainWaterUnits;
    */
};