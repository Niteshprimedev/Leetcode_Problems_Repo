class Solution:

    def isPowerTwo(self, currNum):
        if((currNum & (currNum - 1)) == 0):
            return True
        
        return False

    def reorderedPowerOf2(self, n: int) -> bool:
        digitsStr = str(n)
        isPower = [False]
        str_len = len(digitsStr)

        # idx = 1
        # while(idx < 30):
        #     valN = 2 ** idx
        #     idx += 1
        #     print(valN)

        # 536870912

        def allPerms(curr_idx, currPerm):
            # print(curr_idx, currPerm, currPerm[str_len - 1])
            # Base Case:
            if currPerm[0] == '0':
                return
            if curr_idx == (str_len - 1):
                reorderedDigit = int(''.join(currPerm))
                if(self.isPowerTwo(reorderedDigit)):
                    isPower[0] = True
                return # back track for other permutations:

            # Recursive Case:
            for swap_idx in range(curr_idx, str_len):
                if isPower[0]:
                    return
                [currPerm[curr_idx], currPerm[swap_idx]] = [currPerm[swap_idx], currPerm[curr_idx]]

                # if currPerm[0] != '0' and currPerm[str_len - 1] not in ('13579'):
                    # allPerms(curr_idx + 1, currPerm)
                allPerms(curr_idx + 1, currPerm)

                # Backtracking step to revert swap changes:
                [currPerm[curr_idx], currPerm[swap_idx]] = [currPerm[swap_idx], currPerm[curr_idx]]

        allPerms(0, list(digitsStr))

        return isPower[0]