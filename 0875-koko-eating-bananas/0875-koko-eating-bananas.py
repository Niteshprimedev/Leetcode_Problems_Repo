class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        # Brute Force Solution:

        count = 1

        while True:
            remaining_piles = 0
            hours_left = h
            koko_eat_all_bananas = False

            for pile_idx in range(len(piles)):
                pile = piles[pile_idx]
                pile += remaining_piles

                if pile <= count:
                    remaining_piles = 0
                else:
                    remaining_piles += pile - count
                
                hours_left -= 1
            
                while hours_left > 0 and remaining_piles > 0:
                    hours_left -= 1
                    remaining_piles -= count

                    if remaining_piles < 0:
                        remaining_piles = 0
                
                if remaining_piles == 0 and pile_idx == len(piles) - 1:
                    koko_eat_all_bananas = True
                
                if hours_left == 0:
                    break

            if koko_eat_all_bananas:
                break

            count += 1
        
        return count
        '''

        # Binary Search:
        # Observation: the total hours to finish all the piles are
        # always gonna be greater than or equal to the total piles count
        # so I can finish at least 1 pile in 1 hour if I start off with max pile

        def check_koko_eating_piles(eating_pile):
            hours_count = 0

            for pile_idx in range(len(piles)):
                curr_pile = piles[pile_idx]

                hours_count += (curr_pile // eating_pile)

                if (curr_pile % eating_pile) != 0:
                    hours_count += 1
                
                if hours_count > h:
                    break
            
            # print(hours_count, 'pile', eating_pile)
            
            if hours_count <= h:
                return True
            
            return False

        left_pile = 1
        right_pile = max(piles)
        min_piles_count = 1

        while left_pile <= right_pile:
            middle_pile = left_pile + (right_pile - left_pile) // 2

            is_koko_eating_bananas = check_koko_eating_piles(middle_pile)
            # print(left_pile, middle_pile, right_pile)

            if is_koko_eating_bananas == True:
                min_piles_count = middle_pile
                right_pile = middle_pile - 1
            else:
                left_pile = middle_pile + 1
        
        return min_piles_count                

        '''
        # Binary Search: Optimized or Modified if conditions
        # Observation: the total hours to finish all the piles are
        # always gonna be greater than or equal to the total piles count
        # so I can finish at least 1 pile in 1 hour if I start off with max pile

        def check_koko_eating_piles(eating_pile):
            hours_count = 0

            for pile_idx in range(len(piles)):
                curr_pile = piles[pile_idx]

                hours_count += (curr_pile // eating_pile)

                if (curr_pile % eating_pile) != 0:
                    hours_count += 1
                
                if hours_count > h:
                    break
            
            # print(hours_count, 'pile', eating_pile)
            # koko needs more hours than the given hours so not possible
            if hours_count > h:
                return False

            # the hours were enough for the koko, let's see if koko can
            # finish eating all piles in lesser hours or not
            return True

        left_pile = 1
        right_pile = max(piles)
        min_piles_count = 1

        while left_pile <= right_pile:
            middle_pile = left_pile + (right_pile - left_pile) // 2

            is_koko_eating_bananas = check_koko_eating_piles(middle_pile)
            # print(left_pile, middle_pile, right_pile)

            if is_koko_eating_bananas == True:
                min_piles_count = middle_pile
                right_pile = middle_pile - 1
            else:
                left_pile = middle_pile + 1
        
        return min_piles_count     
        '''           