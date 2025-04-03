/**
 * @param {string[]} votes
 * @return {string}
 */
var rankTeams = function(votes) {
    // Logic: Create a hashmap with the teams name as keys
    // and their votes as an array of ranking values
    // 'ABC' => {A: [1, 0, 0], B: [0,1,0], C:[0,0,1]}
    // To create a hashmap like this, first we create a 
    // hashvalue of length vote filled with 0s initially
    // And then updating the value at that particular index
    // Finally, we wanted to sort the teams based on their 
    // rankings
    // so to do that, we check which of the teams ranking array
    // has a different value at any index and is greater so we return that
    // else we return the lexicographically sorted letter;
    // Finally, we get the teams sorted based on their rankings so we join them;
    const rankingTeamsKeyVotesArrValHashmap = new Map();

    // const teamsVotingFrequencyHashmap = new Map();

    for(let vote of votes){
        // Build a Ranking System hashmap for all teams;
        for(let teamIdx = 0; teamIdx < vote.length; teamIdx++){
            const teamHashKey = vote[teamIdx];
            let teamHashValue = new Array(vote.length).fill(0);
            const teamVoteIdx = teamIdx;

            const isTeamNotAdded = rankingTeamsKeyVotesArrValHashmap.has(teamHashKey) !== true;
            if(isTeamNotAdded){
                rankingTeamsKeyVotesArrValHashmap.set(teamHashKey, teamHashValue);
            }

            // Update the hashvalue with the frequency by 1 for the current team
            // at teamVoteIdx;
            teamHashValue = rankingTeamsKeyVotesArrValHashmap.get(teamHashKey);
            teamHashValue[teamVoteIdx] += 1;
            rankingTeamsKeyVotesArrValHashmap.set(teamHashKey, teamHashValue);
        }

    }
    // Get all the teams to sort them based on thier rankings;
    const teamRankByVotes = [...rankingTeamsKeyVotesArrValHashmap.keys()];

    // Sort the teams by voting ranks;
    teamRankByVotes.sort((keyA, keyB) => {
        const hashValueA = rankingTeamsKeyVotesArrValHashmap.get(keyA);
        const hashValueB = rankingTeamsKeyVotesArrValHashmap.get(keyB);

        let isValueAWinner = false;
        let isValueBWinner = false;

        for(let idxI = 0; idxI < hashValueA.length; idxI++){
            const valueA = hashValueA[idxI];
            const valueB = hashValueB[idxI];

            // TeamA is the winner cause it got more votes
            if(valueA > valueB){
                isValueAWinner = true;
                break;
            }
            // TeamB is the winner cause it got more votes
            else if(valueB > valueA){
                isValueBWinner = true;
                break;
            }
        }

        // Keep the teamA first cause it is the winner;
        if(isValueAWinner){
            return -1;
        }
        // Keep the teamB first cause it is the winner;
        else if(isValueBWinner){
            return 1;
        }
        // Both teamA & teamB got equal votes so none is winner
        // Keep the teamA if it is lexicographically ranked first
        // else keep the teamB if it is lexicographically ranked
        // else return both them;
        else{
            if(keyA < keyB) return -1;
            if(keyA > keyB) return 1;
            return 0;
        }
    });

    // Return the teams string ranked based on the votes;
    return teamRankByVotes.join('');
};