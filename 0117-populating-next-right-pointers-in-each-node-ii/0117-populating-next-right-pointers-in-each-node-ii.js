/**
 * // Definition for a _Node.
 * function _Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {_Node} root
 * @return {_Node}
 */
var connect = function(root) {
    // Logic: If parent node has the right child then
    // the parent's next should point to it;

    let currentNode = root;
    if(currentNode === null){
        return root;
    }

    let currentNodeIdx = 0;
    const queue = [];
    queue.push(currentNode);
    let totalNodes = 0;

    while(currentNodeIdx < queue.length){
        const levelLen = queue.length;
        totalNodes += (levelLen - currentNodeIdx);

        for(let idxI = currentNodeIdx; idxI < levelLen; idxI++){
            currentNode = queue[currentNodeIdx];
            currentNodeIdx += 1;

            let nextNode = null;
            if(currentNodeIdx < totalNodes){
                nextNode = queue[currentNodeIdx];
            }

            currentNode.next = nextNode;
            // console.log(currentNodeIdx, 'idx', totalNodes, queue.length);
            // console.log(currentNode, 'hello', nextNode, 'queue', queue[currentNodeIdx]);
            if(currentNode.left){
                queue.push(currentNode.left);
            }
            if(currentNode.right){
                queue.push(currentNode.right);
            }
        }
    }

    return root;
};