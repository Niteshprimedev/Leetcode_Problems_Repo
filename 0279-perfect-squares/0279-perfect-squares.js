/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    // Bottom Up Approach:
    const isPerfectSquare = Number.isInteger(Math.sqrt(n));
    if(isPerfectSquare){
        return 1;
    }

    const perfectSquares = [];

    let sqIdx = 1;
    let squareVal = 1;

    while(squareVal < n){
        squareVal = sqIdx ** 2;
        if(squareVal < n){
            perfectSquares.push(squareVal);
        }

        sqIdx += 1;
    }

    const memoDP = new Array(n + 1).fill(Infinity);
    memoDP[0] = 0 // It takes zero numbers to sum to 0 → that's our base!

    for(let idxI = 1; idxI <= n; idxI++){
        for(let square of perfectSquares){
            if(idxI - square >= 0){
                memoDP[idxI] = Math.min(memoDP[idxI], 1 + memoDP[idxI - square]);
            }
        }
    }

    // console.log(memoDP, perfectSquares);
    return memoDP[n];
    
    /** 
    // Top Down Approach:
    const isPerfectSquare = Number.isInteger(Math.sqrt(n));
    if(isPerfectSquare){
        return 1;
    }

    const perfectSquares = [];

    let sqIdx = 1;
    let squareVal = 1;

    while(squareVal < n){
        squareVal = sqIdx ** 2;
        if(squareVal < n){
            perfectSquares.push(squareVal);
        }

        sqIdx += 1;
    }

    const squaresSize = perfectSquares.length;
    const memoDP = new Map();

    // console.log(memoDP, perfectSquares);
    
    function allNumSquaresSum(currSqSum){
        if(currSqSum === n){
            return 0;
        }

        if(currSqSum > n){
            return Infinity;
        }

        if(memoDP.has(currSqSum)){
            return memoDP.get(currSqSum);
        }

        
        let minPerfectSqSumCount = Infinity;

        /** 
        // Not picking current element square sum;
        const notPickingElsCount = allNumSquaresSum(currIdx + 1, currSqSum);

        // Picking current element square sum;
        const pickingElsCount = 1 + allNumSquaresSum(currIdx, currSqSum + square);

        for(let idxI = 0; idxI < perfectSquares.length; idxI++){
            const square = perfectSquares[idxI];
            const newCount = 1 + allNumSquaresSum(currSqSum + square);
            minPerfectSqSumCount = Math.min(minPerfectSqSumCount, newCount);
        }

        memoDP.set(currSqSum, minPerfectSqSumCount);
        return memoDP.get(currSqSum);
    }
    const minPerfectSqSumCount = allNumSquaresSum(0);

    // console.log(memoDP);
    return minPerfectSqSumCount;
    */
};