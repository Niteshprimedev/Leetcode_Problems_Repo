class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Logic: Greedy idea is to remove more of substrings 
        # ba if y points is greater than x points, else
        # try to remove more of substrings ab if x points > y points
        # And keep the a chars in the stack if x points > y points
        # Else keep the b chars in the stack if x points > y points
        # Then find the matching char b when x > y and char a when
        # y > x so this way we greedily make ba or ab substrings

        max_ops_score = [0]
        substrings_chars_stack = []

        is_ab_op_choice = False

        if x > y:
            is_ab_op_choice = True
        
        def count_non_greedy_score(max_ops_score, substrings_chars_stack):
            idx_i = 0
            while idx_i < len(substrings_chars_stack):
                strt_char = substrings_chars_stack[idx_i]
                end_char = substrings_chars_stack.pop()

                op_substring = strt_char + end_char

                # y > x but we don't have ba choices anymore
                if op_substring == 'ab':
                    max_ops_score[0] += x
                # x > y but we don't have ab choices anymore
                elif op_substring == 'ba':
                    max_ops_score[0] += y
                # the substring is either 'aa' or 'bb' but neither
                # 'ab' nor 'ba' so we can't remove anymore substrings
                else:
                    # print(substrings_chars_stack, idx_i)
                    substrings_chars_stack = []
                    break
                
                idx_i += 1

        for char in s:
            if char not in ('ab'):
                # not just empty stack cause we have non-greedy substrings
                # so count non-greedy score for 'ab' if y > x and 'ba'
                # if x > y
                # print(char, substrings_chars_stack)
                count_non_greedy_score(max_ops_score, substrings_chars_stack)
                substrings_chars_stack = []
            elif is_ab_op_choice:
                # for removing 'ab' cause x > y we need
                # to preserve char a's till the end;
                if char == 'a':
                    substrings_chars_stack.append('a')
                # if curr_char is 'b' and we already have 'a'
                # in our stack then remove 'ab' and gain x
                elif char == 'b' and substrings_chars_stack and substrings_chars_stack[-1] == 'a':
                    substrings_chars_stack.pop()
                    max_ops_score[0] += x
                elif char == 'b':
                    # if curr_char is 'b' then we need to 
                    # preserve it as well cause we might 
                    # not have any choices to remove 'ab' but just 'ba'
                    # so keep it in our stack
                    substrings_chars_stack.append('b')
            else:
                # for removing 'ba' cause y > x we need
                # to preserve char b's till the end;
                if char == 'b':
                    substrings_chars_stack.append('b')
                # if curr_char is 'a' and we already have 'b'
                # in our stack then remove 'ba' and gain y
                elif char == 'a' and substrings_chars_stack and substrings_chars_stack[-1] == 'b':
                    substrings_chars_stack.pop()
                    max_ops_score[0] += y
                elif char == 'a':
                    # if curr_char is 'a' then we need to 
                    # preserve it as well cause we might 
                    # not have any choices to remove 'ba' but just 'ab'
                    # so keep it in our stack
                    substrings_chars_stack.append('a')
        
        # finally, we need to remove substrings
        # like 'ba' if y < x cause we couldn't get max_score
        # but we can get the min(x, y) score by performing
        # our non-dominant (non-greedy) operation;
        count_non_greedy_score(max_ops_score, substrings_chars_stack)

        return max_ops_score[0]