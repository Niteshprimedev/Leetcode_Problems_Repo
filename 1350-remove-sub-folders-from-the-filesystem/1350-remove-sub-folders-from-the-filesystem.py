class Node:
    def __init__(self):
        self.children = [None] * 27
        self.is_folder_end = False

class TrieClass:
    def __init__(self):
        self.root = Node()

    def get_dir_char_idx(self, dir_char):
        if dir_char == "/":
            return 26
        else:
            return ord(dir_char) - ord('a')
        
    def insert_dir(self, curr_dir):
        current_node = self.root

        for dir_char in curr_dir:
            dir_char_idx = self.get_dir_char_idx(dir_char)

            if current_node.children[dir_char_idx] == None:
                current_node.children[dir_char_idx] = Node()
            
            current_node = current_node.children[dir_char_idx]
        
        current_node.is_folder_end = True
        return True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        my_file_sys_trie = TrieClass()
        # print(ord("/"))

        new_file_system = []

        for folder_dir in folder:
            my_file_sys_trie.insert_dir(folder_dir)
        
        for folder_dir in folder:
            is_subfolder = False

            # search matching folder with this folder_dir;
            dir_idx = 0
            dir_char = folder_dir[dir_idx]
            dir_char_idx = my_file_sys_trie.get_dir_char_idx(dir_char)

            current_node = my_file_sys_trie.root

            while current_node.children[dir_char_idx] != None and (dir_idx + 1) < len(folder_dir):
                current_node = current_node.children[dir_char_idx]
                
                dir_idx += 1
                dir_char = folder_dir[dir_idx]
                dir_char_idx = my_file_sys_trie.get_dir_char_idx(dir_char)
            
                if current_node != None and current_node.is_folder_end:
                    if dir_idx < len(folder_dir) and (folder_dir[dir_idx] == "/"):
                        is_subfolder = True
                        break
                
            if not is_subfolder:
                new_file_system.append(folder_dir)

        return new_file_system