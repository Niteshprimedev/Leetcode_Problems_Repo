/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    /**
    // Same Logic on May 29th During Tree Revision:
    // Logic: If both the trees are null then return True
    // And if both exists and their values are equal then True
    // else we return False cause the trees are not identical;
    
    function traverse(currentNode1, currentNode2){
        if(currentNode1 === null && currentNode2 === null){
            return true;
        }

        if(currentNode1 && currentNode2 && currentNode1.val === currentNode2.val){
            const isLeftTree = traverse(currentNode1.left, currentNode2.left);
            const isRightTree = traverse(currentNode1.right, currentNode2.right);

            return isLeftTree && isRightTree;
        }

        return false;
    }
    return traverse(p, q);
    */
    
    // Solution 2: Using Extra Space;
    const rootPNodes = traverse(p, []);
    const rootQNodes = traverse(q, []);

    function traverse(currentNode, arr){
        if(currentNode && currentNode.left === null && currentNode.right === null){
            arr.push(currentNode.val);
            return arr;
        }
        else if(currentNode === null){
            arr.push(null);
            return arr;
        }
        else{
            arr.push(currentNode.val);
        }

        const leftTree = traverse(currentNode.left, arr);
        const rightTree = traverse(currentNode.right, arr);

        return rightTree;
    }

    const loopLen = rootPNodes.length > rootQNodes.length ? rootPNodes.length : rootQNodes.length;
    let isTreeSame = true;

    for(let idxI = 0; idxI < loopLen; idxI++){
        if(rootPNodes[idxI] !== rootQNodes[idxI]){
            isTreeSame = false;
            break;
        }
    }

    // console.log(rootPNodes, rootQNodes);

    return isTreeSame;

    /**
    //  Solution 3: Using Many If Conditions:
    function traverse(currentNode1, currentNode2){
        if(currentNode1 === null && currentNode2 !== null){
            return false;
        }
        else if(currentNode1 !== null && currentNode2 === null){
            return false;
        }
        else if(currentNode1 && currentNode2 && currentNode1.val !== currentNode2.val){
            return false;
        }
        
        if(currentNode1 === null && currentNode2 === null){
            return true
        }

        const leftTree = traverse(currentNode1.left, currentNode2.left);
        const rightTree = traverse(currentNode1.right, currentNode2.right);

        return leftTree && rightTree;
    }
    return traverse(p, q);
    */
};