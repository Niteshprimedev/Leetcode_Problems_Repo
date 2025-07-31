/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Node currNode = head;
		
		HashMap<Node, Node> nodesKeyCopiedNodesMap = new HashMap<>();
		
		while(currNode != null){
			int nodeVal = currNode.val;
			Node newNode = new Node(nodeVal);
			
			nodesKeyCopiedNodesMap.put(currNode, newNode);
			currNode = currNode.next;
		}
		
		currNode = head;
		while(currNode != null){
			Node copiedNode = nodesKeyCopiedNodesMap.get(currNode);
			Node copiedNextNode = nodesKeyCopiedNodesMap.get(currNode.next);
			Node copiedRandomNode = nodesKeyCopiedNodesMap.get(currNode.random);
			
			copiedNode.next = copiedNextNode;
			copiedNode.random = copiedRandomNode;
			currNode = currNode.next;
		}
		
		return nodesKeyCopiedNodesMap.get(head);
    }
}