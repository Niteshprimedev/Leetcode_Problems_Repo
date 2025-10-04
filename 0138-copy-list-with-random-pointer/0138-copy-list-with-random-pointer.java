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
        HashMap<Node, Node> nodesKeyCopiedNodesMap = new HashMap<>();

        Node currNode = head;

        while(currNode != null){
            Node copiedNode = new Node(currNode.val);
            nodesKeyCopiedNodesMap.put(currNode, copiedNode);

            currNode = currNode.next;
        }

        currNode = head;
        Node clonedHead = new Node(-1);
        Node clonedNodeP = clonedHead;

        while(currNode != null){
            Node copiedNode = nodesKeyCopiedNodesMap.get(currNode);
            Node copiedNodeNextNode = nodesKeyCopiedNodesMap.get(currNode.next);
            Node copiedNodeRandomNode = nodesKeyCopiedNodesMap.get(currNode.random);

            copiedNode.next = copiedNodeNextNode;
            copiedNode.random = copiedNodeRandomNode;

            clonedNodeP.next = copiedNode;
            clonedNodeP = copiedNode;
            currNode = currNode.next;
        }

        clonedHead = clonedHead.next;
        return clonedHead;
    }
}