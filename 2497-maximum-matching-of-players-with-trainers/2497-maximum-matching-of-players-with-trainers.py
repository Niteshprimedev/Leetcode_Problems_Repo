class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        np = len(players)
        nt = len(trainers)

        max_matching_counts = 0

        players.sort()
        trainers.sort()

        player_idx = 0
        trainer_idx = 0

        while trainer_idx < nt:
            if player_idx < np and players[player_idx] <= trainers[trainer_idx]:
                player_idx += 1
                max_matching_counts += 1
                
            trainer_idx += 1
        
        return max_matching_counts

