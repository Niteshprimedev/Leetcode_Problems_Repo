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
        # Solution 1: Without Sorting and inserting first
        # then using logic to see if curr_dir is a subfolder?
        # or not by checking if at any point the current_node
        # says the end_folder and the current dir_char is "/"
        # else not a subfolder and add to answer;

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

        '''
        # Solution 2: With Sorting and checking if 
        # the current_node is end_folder and the dir_char is "/"
        # then it is a subfolder else not;

        folder.sort()
        # print(folder)
        
        my_file_sys_trie = TrieClass()
        # print(ord("/"))

        new_file_system = []

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
                
            if not is_subfolder:
                new_file_system.append(folder_dir)
                my_file_sys_trie.insert_dir(folder_dir)

        return new_file_system
        '''

        '''
        # Solution 3: Using Merge Sort;
        def merge(strt_idx, mid, end_idx, folder):
            merged_arr = []

            idx_i = strt_idx
            idx_j = mid + 1

            while idx_i <= mid and idx_j <= end_idx:
                if len(folder[idx_i]) <= len(folder[idx_j]):
                    merged_arr.append(folder[idx_i])
                    idx_i += 1
                else:
                    merged_arr.append(folder[idx_j])
                    idx_j += 1
            
            while idx_i <= mid:
                merged_arr.append(folder[idx_i])
                idx_i += 1
            while idx_j <= end_idx:
                merged_arr.append(folder[idx_j])
                idx_j += 1
            
            for idx in range(len(merged_arr)):
                folder[idx + strt_idx] = merged_arr[idx]
            
            return folder

        def merge_sort(strt_idx, end_idx, folder):
            if strt_idx < end_idx:
                mid = strt_idx + (end_idx - strt_idx) // 2

                merge_sort(strt_idx, mid, folder)
                merge_sort(mid + 1, end_idx, folder)

                merge(strt_idx, mid, end_idx, folder)
        
        merge_sort(0, len(folder) - 1, folder)
        # print(folder)
        
        my_file_sys_trie = TrieClass()
        # print(ord("/"))

        new_file_system = []

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
                
            if not is_subfolder:
                new_file_system.append(folder_dir)
                my_file_sys_trie.insert_dir(folder_dir)

        return new_file_system
        '''