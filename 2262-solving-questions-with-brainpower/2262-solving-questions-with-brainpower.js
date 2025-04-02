/**
 * @param {number[][]} questions
 * @return {number}
 */
var mostPoints = function(questions) {
    // Bottom Up Approach:
    const N = questions.length;

    let maxQuestionPoints = 0;
    const memoDP = new Array(N).fill(0);

    for(let idxI = N - 1; idxI >= 0; idxI--){
        const [points, brainpower] = questions[idxI];

        let nextIdx = (idxI + brainpower + 1) >= N ? 0 : (idxI + brainpower + 1);
        const solveItPoints = points + memoDP[nextIdx];
        nextIdx = (idxI + 1) >= N ? 0 : idxI + 1;
        const skipItPoints = memoDP[nextIdx];

        memoDP[idxI] = Math.max(solveItPoints, skipItPoints);
    }
    // console.log(memoDP);
    return memoDP[0];

    /** 
    // Top Down Approach:
    let maxQuestionPoints = 0;
    const memoDP[0] = new Array(N).fill(-1);

    function solveOrSkip(idx, questions, memoDP){
        if(idx >= questions.length) return 0;

        if(memoDP[idx] > -1) return memoDP[idx];

        const solveItPoints = questions[idx][0] + solveOrSkip(idx + questions[idx][1] + 1, questions, memoDP);
        const leaveItPoints = solveOrSkip(idx + 1, questions, memoDP);

        memoDP[idx] = Math.max(solveItPoints, leaveItPoints);
        return memoDP[idx];
    }
    return solveOrSkip(0, questions, memoDP);
    */
};