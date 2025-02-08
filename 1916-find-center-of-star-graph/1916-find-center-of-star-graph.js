/**
 * @param {number[][]} edges
 * @return {number}
 */
var findCenter = function(edges) {
    // Solution using Topological Sort 
    // Create a inDegreeArr variable and initialize it to an empty array of (edges.length + 1) value
    // Run a loop through the edges and for each edge do the following;
    // Create vertex1 & vertex2 variables and initialize them to an edge at index 0 & index 1
    // Update the inDegreeArr element value for the particular edge with the
    // value 0 if it's empty item else update it by incrementing the previous value by 1
    // Find the largest value in the inDegreeArr cause that will have max num of edges & store it in 
    // the variable largestNumOfEdges using Math.max(...inDegreeArr) expression
    // Create a starGraphCenterVertexNode variable and initalize it to the index value of
    // the largestNumOfEdges & adding it to 1 to get the vertex/node
    // Finally, we will have found our center of star graph in the starGraphCenterVertexNode variable
    // so will return it;


    const inDegreeArr = new Array(edges.length + 1);

    edges.forEach(edge => {
        const vertex1 = edge[0];
        const vertex2 = edge[1];

        inDegreeArr[vertex1 - 1] = (inDegreeArr[vertex1 - 1] || 0) + 1;
        inDegreeArr[vertex2 - 1] = (inDegreeArr[vertex2 - 1] || 0) + 1;
    });

    // console.log(inDegreeArr, inDegreeArr.length);

    // Find the largest value;
    const largestNmOfEdges = Math.max(...inDegreeArr);
    const starGraphCenterVertexNode = inDegreeArr.indexOf(largestNmOfEdges) + 1;

    return starGraphCenterVertexNode;
};