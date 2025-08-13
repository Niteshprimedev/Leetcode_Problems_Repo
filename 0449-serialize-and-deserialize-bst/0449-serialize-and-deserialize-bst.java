/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    private void preDfsTraverse(TreeNode currNode, List<String> serializedTree){
        // Base Case:
        if(currNode == null){
            serializedTree.add("null");
            return;
        }

        serializedTree.add(String.valueOf(currNode.val));

        preDfsTraverse(currNode.left, serializedTree);
        preDfsTraverse(currNode.right, serializedTree);
    }

    private TreeNode constructBST(TreeNode currNode, String[] tree, int[] currIdx){
        currIdx[0] += 1;
        // Base Case:
        if(currIdx[0] >= tree.length){
            return currNode;
        }

        String numStr = tree[currIdx[0]];
        if(!numStr.equals("null")){
            currNode.left = new TreeNode(Integer.valueOf(numStr));
            constructBST(currNode.left, tree, currIdx);
        }

        currIdx[0] += 1;
        numStr = tree[currIdx[0]];
        if(!numStr.equals("null")){
            currNode.right = new TreeNode(Integer.valueOf(numStr));
            constructBST(currNode.right, tree, currIdx);
        }

        return currNode;
    }

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if(root == null){
            return "";
        }

        List<String> serializedTree = new ArrayList<>();

        preDfsTraverse(root, serializedTree);

        return String.join(" ", serializedTree);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        TreeNode deserializedRoot = null;
        if(data.length() == 0){
            return deserializedRoot;
        }

        String[] tree = data.split(" ");
        String numStr = tree[0];
        deserializedRoot = new TreeNode(Integer.valueOf(numStr));

        return constructBST(deserializedRoot, tree, new int[]{0});
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// String tree = ser.serialize(root);
// TreeNode ans = deser.deserialize(tree);
// return ans;