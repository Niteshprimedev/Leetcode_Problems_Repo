class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:

        '''
        **Flood part explained step by step**

        ```
                if rain in mp:
                    it = st.bisect(mp[rain])
                    if it == len(st):
                        return []   # no dry day available after last fill
                    ans[st[it]] = rain
                    st.discard(st[it])
        ```

        **Notes**
        rain = the lake that is raining today.
        mp = map of lake → last day it rained.
        st = sorted list of indices of dry days (rains[i] == 0).

        We are inside the **else branch**: today it’s raining on lake rain.

        **Step 1**: Check if this lake was already full?
        ```
        if rain in mp:
        ```

        If `rain` is in mp, it already rained on this lake before, and we haven’t dried it since.
        That means: **if we don’t dry it before today**, flood happens.
        So we must find a **dry day to dry** it after the previous rain day and before today.

        **Step 2**: Find the next dry day after last rain
        ```
        it = st.bisect(mp[rain])
        ```

        mp[rain] = last day this lake got rain.
        st.bisect(x) → returns the index in st of the first dry day > x (strictly after x).
        So st[it] = actual day index where we can safely dry this lake.

        ```
        st = [2, 4, 6]  # dry days
        mp[rain] = 1    # lake last rained on day 1
        it = st.bisect(1)  # gives 0 → st[0] = 2
        ```

        `So we can dry the lake on day 2, which is after last rain, before it rains again.`

        **Step 3**: Check if no dry day exists
        ```
        if it == len(st):
            return []   # no dry day available after last fill
        ```

        If it == len(st), it means there is no dry day available after the previous rain.
        That is **exactly a flood scenario** -> cannot prevent flood -> return [].

        **Step 4**: Assign the dry day
        ```
        ans[st[it]] = rain
        st.discard(st[it])
        ```

        st[it] = the dry day index we just found.
        ans[st[it]] = rain → dry this lake on that day.
        st.discard(st[it]) → remove this dry day from available days, because we already used it.
        
        
        '''

        '''

        Intuition in Words

        Whenever a lake rains again, check if it’s already full:

        Yes → must dry it before it rains again.

        Use the earliest dry day available after the last rain.

        If none exists → flood.

        bisect = the magic tool to find the earliest dry day after a given index, in O(log n).

        SortedList keeps dry days sorted, so bisect works efficiently.

        '''

        ans = [1] * len(rains)
        st = SortedList()
        mp = {}
        for i, rain in enumerate(rains):
            if rain == 0:
                st.add(i)
            else:
                ans[i] = -1
                if rain in mp:
                    it = st.bisect(mp[rain])
                    if it == len(st):
                        return []
                    ans[st[it]] = rain
                    st.discard(st[it])
                mp[rain] = i
        return ans