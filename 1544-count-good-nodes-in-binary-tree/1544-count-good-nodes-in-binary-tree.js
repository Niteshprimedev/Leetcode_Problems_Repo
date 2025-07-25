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
 * @return {number}
 */
var goodNodes = function(root) {

    // Solution: Using DFS - Depth First Search & Array Filter Approach to filter out the nodes/ array items which are in increasing order;
    // Pseudocode
    // Create a totalNodesPathsArr variable and initialize it to an empty array 
    // Create a nodesCurrPathArr variable and initialize it to an empty array
    // Create a dfsTraverse(currentNode) function that takes a node as an input and makes depth first search
    // Push the currentNode value into the nodesCurrPathArr
    // Push the nodesCurrPathArr array as an element into the totalNodesPathsArr variable
    // Move and traverse to the left node in the tree if there's a left node;
    // Move and traverse to the riht node in the tree if there's a right node
    // When you left and right node traversal then pushing the node to the nodesCurrPathArr & pushing nodesCurrPathArr
    // into the totalNodesPathsArr along with left and right traversal for that node is done;
    // Pop the last node element from the nodesCurrPathArr once the nodes left & right traversal is done
    // Run a forEach loop through the totalNodesPathsArr to run another for loop through the each element 
    // Run a for loop through each element from index i = 0 to index i = elements.length - 1 value
    // Break the for loop for the element if any element's value at index i = 0 to elements.length - 2 is greater than the 
    // last elements value in the current elements array
    // Else update the totalGoodNodesCount value by 1 if the last element value is greater than or equal to all the values 
    // Finally, we will have the total number of good nodes count in the totalGoodNodesCount variable for the given
    // binary tree so will return it

    let totalGoodNodesCount = 0;
    const totalNodesPathsArr = [];
    const nodesCurrPathArr = [];
    let currentNode = root;

    // Recursive DFS Function
    function dfsTraverseRec(currentNode){
        nodesCurrPathArr.push(currentNode.val);
        let nodes = [...nodesCurrPathArr];
        totalNodesPathsArr.push(nodes);
        
        // console.log("Recursive call", currentNode.val, nodesCurrPathArr, totalNodesPathsArr);

        // Traverse to the left node if left node;
        if(currentNode.left) dfsTraverseRec(currentNode.left);

        // Traverse to the right node if right node;
        if(currentNode.right) dfsTraverseRec(currentNode.right);

        // Pop the last node as we have traversed it's left & right node;
        nodesCurrPathArr.pop();
    }

    // kick off the recursive dfs traverse() function & pass the root
    dfsTraverseRec(currentNode);

    // console.log(totalNodesPathsArr);

    // Finding the good nodes in binary tree;
    totalNodesPathsArr.forEach(nodeElementArr => {
        let isGoodNode = true;
        for(let i = 0; i < nodeElementArr.length - 1; i++){

            let lastElementVal = nodeElementArr[nodeElementArr.length - 1];
            let remainingElementVal = nodeElementArr[i];

            if(remainingElementVal > lastElementVal){
                isGoodNode = false;
                break;
            }
        }
        if(isGoodNode){
            totalGoodNodesCount++;
        }
    });

    return totalGoodNodesCount;

    // We can't do this one with BFS Traversal;
    // // Pseudocode
    // // Solution using BFS - Breadth First Search Iterative
    // // Observation: Each row can be described by the depth of its nodes in DFS;
    // // Create a totalGoodNodesArr variable and initialize it to an empty array;
    // // Create a queue variable and initialize it to an empty array
    // // Create a currentDepth variable and initialize it to nothing
    // // Push the root & currentDepth to queue array to start off the dfs tree traversal as [root, 0]
    // // Run a while loop as long as the queue is not empty or in other words until the tree is traversed
    // // Destructing the values in a currentNode and currentDepth from the queue shift() method
    // // Check if we are visiting the node first time, true then push the node's value to totalGoodNodesArr
    // // By comparing the currentDepth value and the arrays length
    // // Else check if the currentNode's value is greater than the value stored in the totalGoodNodesArr array
    // // If there's a left node then push the left node and currentDepth + 1 value to queue
    // // If there's a right node then push the right node and currentDepth + 1 value to queue
    // // Once the while loop is done;
    // // Finally, we will have the largest values of each tree row in the totalGoodNodesArr, so will return it 

    // if(root === null) return 0;

    // const totalGoodNodesArr = [root.val];
    // const queue = [];
    // let currentNode = root;
    // let currentDepth;

    // queue.push([currentNode, 0]);

    // while(queue.length){
    //     [currentNode, currentDepth] = queue.pop();
    //     let tempNode = root;

    //     let goodNodeSum = Number.NEGATIVE_INFINITY;

    //     for(let i = 0; i < currentDepth; i++){
    //         let xNodeValue = currentNode.val;
    //         let prevNodeValue = tempNode.val;
    //         if(xNodeValue >= prevNodeValue){
                
    //         }
    //         tempNode = tempNode
    //     }

    //     totalGoodNodesArr.push(goodNodeSum);

    //     currentNode++;
    //     if(currentNode.left){
    //         queue.push([currentNode.left, currentNode]);
    //     }
    //     if(currentNode.right){
    //         queue.push([currentNode.right, currentNode]);
    //     }



    // }

    // return totalGoodNodesArr.length;
};