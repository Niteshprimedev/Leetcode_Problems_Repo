class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_word_end = False
        self.curr_word = ''

class TrieClass:
    def __init__(self):
        self.root = Node()

    def insert_word(self, word):
        current_node = self.root

        for char in word:
            char_idx = ord(char) - ord('a')

            if current_node.children[char_idx] == None:
                current_node.children[char_idx] = Node()
            
            current_node = current_node.children[char_idx]
        
        current_node.is_word_end = True
        current_node.curr_word = word
        return
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m_rows = len(board)
        n_cols = len(board[0])

        all_matched_board_words = set()

        my_trie = TrieClass()

        for word in words:
            my_trie.insert_word(word)
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # # Edge Case:
        # if m_rows == 1 and n_cols == 1:
        #     char = board[0][0]
        #     char_idx = ord(char) - ord('a')

        #     current_node = my_trie.root

        #     if current_node.children[char_idx] != None and current_node.children[char_idx].is_word_end:
        #         all_matched_board_words.add(char)

        def board_search(row_idx, col_idx, current_node):
            # Base Case:
            char = board[row_idx][col_idx]
            char_idx = ord(char) - ord('a')

            new_current_node = current_node.children[char_idx]
            
            if current_node.children[char_idx] == None:
                if current_node.is_word_end:
                    all_matched_board_words.add(current_node.curr_word)
                return
            elif new_current_node and new_current_node.is_word_end:
                all_matched_board_words.add(new_current_node.curr_word)
            
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
        
        return list(all_matched_board_words)

        