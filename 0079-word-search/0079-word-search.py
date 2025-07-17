class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Solution 1: Using visited array and creating word
        m_rows = len(board)
        n_cols = len(board[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited_arr = [[-1 for _ in range(n_cols)] for _ in range(m_rows)]
        is_word_found = [False]

        def board_search(row_idx, col_idx, curr_word, visited_arr):
            # Base Case:
            if curr_word == word:
                is_word_found[0] = True
                return
            
            original_word = word[:len(curr_word)]

            # print(original_word)
            if curr_word != original_word:
                return

            visited_arr[row_idx][col_idx] = 1

            for direction in directions:
                new_row_idx = row_idx + direction[0]
                new_col_idx = col_idx + direction[1]

                if new_row_idx < 0 or new_row_idx >= m_rows or new_col_idx < 0 or new_col_idx >= n_cols:
                    continue
                elif visited_arr[new_row_idx][new_col_idx] == 1:
                    continue
                else:
                    board_search(new_row_idx, new_col_idx, curr_word + board[new_row_idx][new_col_idx], visited_arr)

            visited_arr[row_idx][col_idx] = -1

        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if board[row_idx][col_idx] == word[0]:
                    board_search(row_idx, col_idx, word[0], visited_arr)
                
                if is_word_found[0]:
                    break

            if is_word_found[0]:
                break

        return is_word_found[0]

        '''
        # Solution2: The Better & Optimized Solution using Backtracking;
        m_rows = len(board)
        n_cols = len(board[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        is_word_found = [False]

        def board_search(row_idx, col_idx, curr_word_idx):
            # Base Case:
            if curr_word_idx == len(word):
                is_word_found[0] = True
                return
            
            curr_char = board[row_idx][col_idx]
            board[row_idx][col_idx] = -1

            for direction in directions:
                new_row_idx = row_idx + direction[0]
                new_col_idx = col_idx + direction[1]

                if new_row_idx < 0 or new_row_idx >= m_rows or new_col_idx < 0 or new_col_idx >= n_cols:
                    continue
                elif board[new_row_idx][new_col_idx] == -1:
                    continue
                elif board[new_row_idx][new_col_idx] == word[curr_word_idx]:
                    board_search(new_row_idx, new_col_idx, curr_word_idx + 1)

            board[row_idx][col_idx] = curr_char

        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                if board[row_idx][col_idx] == word[0]:
                    board_search(row_idx, col_idx, 1)
                
                if is_word_found[0]:
                    break

            if is_word_found[0]:
                break

        return is_word_found[0]
        '''

'''
# TRIE DS SOLUTION:
class Node:
    def __init__(self):
        self.children = [None] * 256
        self.is_word_end = False
        self.curr_word = ''

class TrieClass:
    def __init__(self):
        self.root = Node()

    def insert_word(self, word):
        current_node = self.root

        for char in word:
            char_idx = ord(char)

            if current_node.children[char_idx] == None:
                current_node.children[char_idx] = Node()
            
            current_node = current_node.children[char_idx]
        
        current_node.is_word_end = True
        current_node.curr_word = word
        return
    
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m_rows = len(board)
        n_cols = len(board[0])

        is_word_found = [False]

        my_trie = TrieClass()

        my_trie.insert_word(word)
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def board_search(row_idx, col_idx, current_node):
            # Base Case:
            char = board[row_idx][col_idx]
            char_idx = ord(char)

            new_current_node = current_node.children[char_idx]
            
            if current_node.children[char_idx] == None:
                if current_node.is_word_end:
                    is_word_found[0] = True
                return
            elif new_current_node and new_current_node.is_word_end:
                is_word_found[0] = True
            
            board[row_idx][col_idx] = -1

            for direction in directions:
                new_row_idx = row_idx + direction[0]
                new_col_idx = col_idx + direction[1]

                if new_row_idx >= 0 and new_row_idx < m_rows and new_col_idx >= 0 and new_col_idx < n_cols and board[new_row_idx][new_col_idx] != -1:
                    board_search(new_row_idx, new_col_idx, new_current_node)
            
            # backtrack to explore other paths;
            board[row_idx][col_idx] = char

        for row_idx in range(m_rows):
            for col_idx in range(n_cols):
                current_node = my_trie.root
                board_search(row_idx, col_idx, current_node)
        
        return is_word_found[0]
'''

        