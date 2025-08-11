/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> zigzagLevelList = new ArrayList<>();
		
		if(root == null){
			return zigzagLevelList;
		}
		
		Deque<TreeNode> queue = new ArrayDeque<>();
		
		queue.addLast(root);
		boolean isReverse = false;
		
		while(queue.size() > 0){
            // System.out.println(queue.size());
            int levelSize = queue.size();
			Stack<TreeNode> currLevelStack = new Stack<>();
            List<Integer> currLevelNodes = new ArrayList<>();
			
			for(int idx = 0; idx < levelSize; idx++){
				TreeNode currNode = queue.removeFirst();
				
				currLevelNodes.add(currNode.val);
				
				if(isReverse){
					if(currNode.right != null){
						currLevelStack.push(currNode.right);
					}
					if(currNode.left != null){
						currLevelStack.push(currNode.left);
					}
				}
				else{
					if(currNode.left != null){
						currLevelStack.push(currNode.left);
					}
					if(currNode.right != null){
						currLevelStack.push(currNode.right);
					}
				}
			}
			
            zigzagLevelList.add(currLevelNodes);

			while(currLevelStack.size() > 0){
				queue.addLast(currLevelStack.pop());
			}
			
			isReverse = !isReverse;
		}
			
		return zigzagLevelList;
    }
}