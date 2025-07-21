/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    // Solution using Backtracking and Combinations Logic;

    const allCombsList = []

    function generateCombs(currIdx, currComb){
        // Base Case:
        if(currComb.length === k){
            allCombsList.push([...currComb])
            return;
        }

        if(currComb.length > k || currIdx > n){
            return;
        }

        for(let idxI = currIdx; idxI <= n; idxI++){
            // Pick Case
            currComb.push(idxI);
            generateCombs(idxI + 1, currComb);
            // Not Pick Case & Backtrack
            currComb.pop()
        }
    }

    generateCombs(1, []);

    return allCombsList
};