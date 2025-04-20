class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # How many rabbits have the same color as you?
        
        rabbits_colors_freq_map = dict()
        min_num_of_rabbits = 0

        for rabbit in answers:
            if rabbit in rabbits_colors_freq_map:
                rabbits_colors_freq_map[rabbit] += 1
            else:
                rabbits_colors_freq_map[rabbit] = 1
        
        # print(rabbits_colors_freq_map)

        for rabbit in answers:
            if len(rabbits_colors_freq_map) == 0:
                break
            elif rabbit in rabbits_colors_freq_map:
                rabbits_colors_freq_map[rabbit] -= 1

                hash_value = rabbits_colors_freq_map[rabbit]
                min_num_of_rabbits += 1
                min_num_of_rabbits += rabbit

                hash_value -= rabbit
                if hash_value <= 0:
                    del rabbits_colors_freq_map[rabbit]
                else:
                    rabbits_colors_freq_map[rabbit] = hash_value

        return min_num_of_rabbits