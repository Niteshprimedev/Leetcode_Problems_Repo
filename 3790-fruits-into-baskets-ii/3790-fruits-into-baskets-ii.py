class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced_fruits_count = 0
        placed = set()

        for fruit in fruits:
            for idx in range(len(baskets)):
                if idx not in placed and fruit <= baskets[idx]:
                    placed.add(idx)
                    break
        
            # print(placed)

        return len(baskets) - len(placed)

