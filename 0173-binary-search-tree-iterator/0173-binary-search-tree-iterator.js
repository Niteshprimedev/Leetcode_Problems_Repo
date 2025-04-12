/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 */
var BSTIterator = function(root) {
    this.root = root;
    let currentNode = this.root;
    this.inorderTraversal = [];

    while(currentNode){
        if(currentNode.left === null){
            this.inorderTraversal.push(currentNode.val);
            currentNode = currentNode.right;
        }
        else{
            let prevNode = currentNode.left;
            while(prevNode.right !== null && prevNode.right !== currentNode){
                prevNode = prevNode.right;
            }

            if(prevNode.right === null){
                prevNode.right = currentNode;
                currentNode = currentNode.left;
            }
            else{
                prevNode.right = null;
                this.inorderTraversal.push(currentNode.val);
                currentNode = currentNode.right;
            }
        }
    }

    function reverseArr(arr){
        let strtIdx = 0;
        let endIdx = arr.length - 1;

        while(strtIdx < endIdx){
            [arr[strtIdx], arr[endIdx]] = [arr[endIdx], arr[strtIdx]];
            strtIdx++;
            endIdx--;
        }

    }

    reverseArr(this.inorderTraversal);
    // console.log(this.inorderTraversal);
    return null;
};

/**
 * @return {number}
 */
BSTIterator.prototype.next = function() {
    console.log(this.inorderTraversal)
    return this.inorderTraversal.pop();
};

/**
 * @return {boolean}
 */
BSTIterator.prototype.hasNext = function() {
    const isArrNotEmpty = this.inorderTraversal.length > 0;
    if(isArrNotEmpty){
        return true;
    }
    
    return false;
};

/** 
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = new BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */