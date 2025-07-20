'''
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_dir_end = False
        self.curr_word = ''
'''

'''
from collections import defaultdict
from typing import List

class Node:
    def __init__(self):
        self.children = {}
        self.is_dir_end = False
        self.curr_path = []
    
class TrieClass:
    def __init__(self):
        self.root = Node()

    def insert_dir(self, curr_dir):
        current_node = self.root

        for sub_folder in curr_dir:
            if sub_folder not in current_node.children:
                current_node.children[sub_folder] = Node()
            
            current_node.curr_path = curr_dir
            current_node = current_node.children[sub_folder]

        # if len(current_node.children) == 0:
        #     current_node.is_dir_end = True
        #     current_node.curr_path = curr_dir
        #     return True
        
        # return False
        # ✅ Only set curr_path at leaf
        current_node.is_dir_end = True
        current_node.curr_path = curr_dir
        return True
    
    def search_dir(self, curr_dir):
        current_node = self.root

        matched_prefix = []
        for sub_folder in curr_dir:

            if sub_folder not in current_node.children:
                break
            
            matched_prefix.append(sub_folder)
            current_node = current_node.children[sub_folder]

        if not matched_prefix:
            return (0, [])        
        return (len(matched_prefix), matched_prefix)

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        paths.sort(key=lambda x:len(x))
        rem_unique_folders = set()

        # print(paths)
        last_dir_char_map = defaultdict(list)
        my_trie = TrieClass()

        # Build Trie Tree
        for idx in range(len(paths) - 1, -1, -1):
            curr_dir = paths[idx]
            
            is_end_dir = my_trie.insert_dir(curr_dir)
            if is_end_dir:
                last_dir_name = curr_dir[-1]
                last_dir_char_map[last_dir_name].append(curr_dir)
        
        # print(last_dir_char_map)

        def form_folder_path(dir_str, rem_unique_folders):
            prefix_arr = []

            for dir_char in dir_str:
                prefix_arr = prefix_arr.copy()
                prefix_arr.append(dir_char)
                rem_unique_folders.add(tuple(prefix_arr))

        # Process groups
        for hash_key, hash_value in last_dir_char_map.items():
            # Unique Directory so keep all of them;
            if len(hash_value) == 1:
                form_folder_path(hash_value[0], rem_unique_folders)
            else:
                # check duplicates with reversed trie
                new_my_trie = TrieClass()
                match_prefix_map = defaultdict(int)

                for curr_dir in hash_value:
                    rev_dir = curr_dir[::-1] #reverse
                    match_chars_count, match_dir_path = new_my_trie.search_dir(rev_dir)
                    new_my_trie.insert_dir(rev_dir)

                    if match_chars_count == 0:
                        continue
                    match_prefix_map[tuple(rev_dir)] = match_chars_count
                    match_prefix_map[tuple(match_dir_path)] = match_chars_count
                
                # print(match_prefix_map)
                for dir_path, match_subfolders_count in match_prefix_map.items():
                    if len(dir_path) ==  match_subfolders_count:
                        # entire path matched => duplicate
                        continue
                    
                    dir_path = dir_path[match_subfolders_count:]
                    dir_path = dir_path[::-1] # reverse back
                    print(dir_path)
                    form_folder_path(dir_path, rem_unique_folders)

        return [list(dir_path) for dir_path in rem_unique_folders]
'''

from collections import defaultdict, Counter
from typing import List

class Node:
    def __init__(self):
        self.children = {}
        self.serial = ""  # to store serialization
        self.valid = True  # will mark false if duplicate

class TrieClass:
    def __init__(self):
        self.root = Node()

    def insert_dir(self, curr_dir):
        node = self.root
        for folder in curr_dir:
            if folder not in node.children:
                node.children[folder] = Node()
            node = node.children[folder]

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # 1. Build trie
        my_trie = TrieClass()
        for path in paths:
            my_trie.insert_dir(path)

        # 2. Serialize subtrees and count frequency
        freq = Counter()

        def serialize(node: Node) -> str:
            if not node.children:
                node.serial = ""
                return node.serial
            parts = []
            for folder, child in sorted(node.children.items()):
                parts.append(folder + "(" + serialize(child) + ")")
            node.serial = "".join(parts)
            freq[node.serial] += 1
            return node.serial

        serialize(my_trie.root)

        # 3. Mark duplicates
        def mark(node: Node):
            if freq[node.serial] > 1 and node.serial != "":
                node.valid = False
            for child in node.children.values():
                mark(child)

        mark(my_trie.root)

        # 4. Collect results
        ans = []

        def dfs(node: Node, path: List[str]):
            for folder, child in node.children.items():
                if child.valid:
                    ans.append(path + [folder])
                    dfs(child, path + [folder])

        dfs(my_trie.root, [])
        return ans