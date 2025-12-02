class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        y_cords_map = defaultdict(int)

        for _,y in points:
            y_cords_map[y] += 1

        horizontal_segments = []

        for y, count in y_cords_map.items():
            if count >= 2:
                seg = (count * (count - 1)) // 2 #calc horizontal segs when count >= 2

                horizontal_segments.append(seg)

        # print(horizontal_segments)
        total_trapezoids = 0
        prefix_sum = 0

        for seg in horizontal_segments:
            total_trapezoids += seg * prefix_sum
            prefix_sum += seg
            total_trapezoids %= MOD

        return total_trapezoids

        