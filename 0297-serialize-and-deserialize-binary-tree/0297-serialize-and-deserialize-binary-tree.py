# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
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
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
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
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))