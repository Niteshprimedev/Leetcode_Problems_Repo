# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''

        serialized = []
        def traverse(curr_node):
            if not curr_node:
                serialized.append('*')
                return
            
            serialized.append(str(curr_node.val))

            traverse(curr_node.left)
            traverse(curr_node.right)
        
        traverse(root)
        # print(serialized)
        return ','.join(serialized)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        # print(data)

        deserialized_root = None
        if not data:
            return deserialized_root

        tree = data.split(',')
        # print(tree)
        deserialized_root = TreeNode(int(tree[0]))

        def traverse(curr_node, idx):
            idx[0] += 1

            if(idx[0] >= len(tree)):
                return
    
            if tree[idx[0]] != '*':
                curr_node.left = TreeNode(int(tree[idx[0]]))
                traverse(curr_node.left, idx)
            
            idx[0] += 1
            if tree[idx[0]] != '*':
                curr_node.right = TreeNode(int(tree[idx[0]]))
                traverse(curr_node.right, idx)

        traverse(deserialized_root, [0])

        return deserialized_root
    '''

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''

        serialized = []
        def traverse(curr_node):
            if not curr_node:
                serialized.append('null')
                return
            
            serialized.append(str(curr_node.val))

            traverse(curr_node.left)
            traverse(curr_node.right)
        
        traverse(root)

        return ' '.join(serialized)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        deserialized_root = None
        if not data:
            return deserialized_root

        tree = data.split(' ')

        deserialized_root = TreeNode(int(tree[0]))

        def traverse(curr_node, idx):
            idx[0] += 1

            if(idx[0] >= len(tree)):
                return
    
            if tree[idx[0]] != 'null':
                curr_node.left = TreeNode(int(tree[idx[0]]))
                traverse(curr_node.left, idx)
            
            idx[0] += 1
            if tree[idx[0]] != 'null':
                curr_node.right = TreeNode(int(tree[idx[0]]))
                traverse(curr_node.right, idx)

        traverse(deserialized_root, [0])

        return deserialized_root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans