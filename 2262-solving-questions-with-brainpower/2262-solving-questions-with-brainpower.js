/**
 * @param {number[][]} questions
 * @return {number}
 */
var mostPoints = function(questions) {
    let maxQuestionPoints = 0;
    const memo = new Array(questions.length).fill(-1);

    function solveOrSkip(idx, questions, memo){
        // Base case:
        if(idx >= questions.length) return 0;

        if(memo[idx] > -1) return memo[idx];

        const solveItPoints = questions[idx][0] + solveOrSkip(idx + questions[idx][1] + 1, questions, memo);
        const leaveItPoints = solveOrSkip(idx + 1, questions, memo);

        memo[idx] = Math.max(solveItPoints, leaveItPoints);
        return memo[idx];
    }
    return solveOrSkip(0, questions, memo);

    /** 
    // Algorithm for 2 steps;
    let maxQuestionPoints = 0;

    for(let idxI = 0; idxI < 1; idxI++){
        let choiceOnePoints = 0;
        let choiceTwoPoints = 0;
        let choiceThreePoints = 0;

        for(let idxJ = idxI + 3; idxJ < questions.length; idxJ += 3){
            choiceOnePoints += questions[idxJ][0];
        }
        for(let idxK = idxI + 4; idxK < questions.length; idxK += 4){
            choiceTwoPoints += questions[idxK][0];
        }
        for(let idxL = idxI + 5; idxL < questions.length; idxL += 5){
            choiceThreePoints += questions[idxL][0];
        }

        let newMaxQuestionPoints = questions[idxI][0] + choiceOnePoints;
        maxQuestionPoints = Math.max(maxQuestionPoints, newMaxQuestionPoints);
        
        newMaxQuestionPoints = questions[idxI][0] + choiceTwoPoints;
        maxQuestionPoints = Math.max(maxQuestionPoints, newMaxQuestionPoints);

        newMaxQuestionPoints = questions[idxI][0] + choiceThreePoints;
        maxQuestionPoints = Math.max(maxQuestionPoints, newMaxQuestionPoints);

        if(idxI + 1 < questions.length){
            newMaxQuestionPoints = questions[idxI + 1][0] + choiceTwoPoints;
            maxQuestionPoints = Math.max(maxQuestionPoints, newMaxQuestionPoints);
        }
        if(idxI + 2 < questions.length){
            newMaxQuestionPoints = questions[idxI + 2][0] + choiceThreePoints;
            maxQuestionPoints = Math.max(maxQuestionPoints, newMaxQuestionPoints);
        }
    }

    return maxQuestionPoints;
    */
};