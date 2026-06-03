class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        min_land_time = [float('inf'), float('inf')]
        min_water_time = [float('inf'), float('inf')]

        earliest_time = float('inf')
        
        l = len(landStartTime)
        w = len(waterStartTime)

        for idx in range(w):
            start_time = waterStartTime[idx] + waterDuration[idx]

            if(start_time < min_water_time[1]):
                min_water_time = [waterStartTime[idx], start_time]

        for idx in range(l):
            end_time = min_water_time[1]
            end_time = max(landStartTime[idx], end_time) + landDuration[idx]

            earliest_time = min(earliest_time, end_time)
            

        for idx in range(l):
            start_time = landStartTime[idx] + landDuration[idx]

            if(start_time < min_land_time[1]):
                min_land_time = [landStartTime[idx], start_time]

        for idx in range(w):
            end_time = min_land_time[1]
            end_time = max(waterStartTime[idx], end_time) + waterDuration[idx]

            earliest_time = min(earliest_time, end_time)
        
        # print(min_land_time, min_water_time)

        return earliest_time
        
        