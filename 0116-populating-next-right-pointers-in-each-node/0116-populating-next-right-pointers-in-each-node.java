/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        /*
        if(root == null){
            return null;
        }

        Deque<Node> queue = new ArrayDeque<>();

        queue.addLast(root);

        while(queue.size() > 0){
            Node rightNode = null;
            int levelSize = queue.size();

            for(int idx = 0; idx < levelSize; idx++){
                Node currNode = queue.removeFirst();

                if(currNode.left != null){
                    if(rightNode == null){
                        rightNode = currNode.left;
                    }
                    else{
                        rightNode.next = currNode.left;
                        rightNode = rightNode.next;
                    }
                    queue.addLast(currNode.left);
                }
                if(currNode.right != null){
                    rightNode.next = currNode.right;
                    rightNode = rightNode.next;
                    queue.addLast(currNode.right);
                }
            }
        }

        return root;
        
         */

        // Solution 2: Balanced Tree;
        if(root == null){
            return null;
        }

        Deque<Node> queue = new ArrayDeque<>();

        queue.addLast(root);

        while(queue.size() > 0){
            Node rightNode = null;
            int levelSize = queue.size();

            for(int idx = 0; idx < levelSize; idx++){
                Node currNode = queue.removeFirst();

                if(currNode.right != null){
                    if(rightNode == null){
                        rightNode = currNode.left;
                    }
                    else{
                        rightNode.next = currNode.left;
                        rightNode = rightNode.next;
                    }
                    queue.addLast(currNode.left);

                    rightNode.next = currNode.right;
                    rightNode = rightNode.next;
                    queue.addLast(currNode.right);
                }
            }
        }

        return root;
    }
}