/**
 * @param {number[][]} isConnected
 * @return {number}
 */

 class ProvincesBiDirGraph{
    constructor(){
        this.adjacencyList = {};
    }

    // Add Vertices to the graph
    addVertex(vertex){
        const isVertexNotAdded = this.adjacencyList[vertex] === undefined;
        if(isVertexNotAdded){
            this.adjacencyList[vertex] = [];
            return true;
        }
        return false;
    }

    // Add Edges to the Graph
    addEdge(cityVertex1, cityVertex2){
        // this.adjacencyList[cityVertex1] = cityVertex2;
        // return;

        this.addVertex(cityVertex1);
        this.addVertex(cityVertex2);

        const isCityVertex1 = this.adjacencyList[cityVertex1] !== undefined;
        const isCityVertex2 = this.adjacencyList[cityVertex2] !== undefined;

        if(isCityVertex1 && isCityVertex2){
            this.adjacencyList[cityVertex1].push(cityVertex2);
            return true;
        }
        return false;
    }
 }

 // Solution using AdjacencyList;
var findCircleNum = function(isConnected) {
    // [Logic: Build an adjacencyList of a bi-directional graph where each cityVertex is connected with another cityVertex those are considered as our city edges/connections & cityVertex are considered as vertices. 
    // Do a component wise DFS/BFS traversal as long as the component is not been visited, and number of times the DFS/BFS traversal
    // will be called for the individual vertices, the number of provinces will increment.
    // Pseudocode &
    // Solution using Graph DS + Graph DFS method
    // Create a provincesBDGraph (Bi-Dir) variable and initialize it to a new graph
    // Create a totalNumOfProvinces variable and initialize it to 0
    // Create a rowCitiesVertices variable and initialize it to total num of rows in isConnected
    // Create a colCitiesVertices variable and initialize it to total num of cols in isConnected

    // Run a for loop through the isConnected num of rows i.e rowCitiesVertices from index
    // rowCityVertex = 0 to rowCityVertex < rowCitiesVertices value
    // Run a for loop through the isConnected num of cols i.e colCitiesVertices from index
    // colCityVertex = 0 to colCityVertex < colCitiesVertices value
    // Create a isProvincesConnected variable and initialize it to the value in the isConnected matrix
    // at index rowCityVertex & colCityVertex
    // Do the following if the rowCityVertex index value is not equal to the colCityVertex index value
    // && isProvincesConnected is equals to 1;
    // Create a cityVertex1 variable and initialize it to rowCityVertex;
    // Create a cityVertex2 variable and initialize it to colCityVertex;
    // Update the graph edge by passing the cityVertex1 & cityVertex2 into the provincesBDGraph.addEdge();
    // Create a adjacencyList variable and initialize it to the graph's adjacencyList 
    // Create a visitedCityVerticesHashmap variable and initialize it to an empty hash map;
    // Run a for loop through the isConnected num of rows i.e rowCitiesVertices from index
    // rowCityVertex = 0 to rowCityVertex < rowCitiesVertices value
    // Create a isCityVertexNotPresent variable and initialize it to boolean value true if the 
    // rowCityVertex has not been present in the adjacencyList else to the boolean value false
    // Create a isCityVertexNotVisited variable and initialize it to the boolean value true if the 
    // rowCityVertex has not been visited else to the boolean value false
    // Group of Directly connected provinces;
    // Increment the totalNumOfProvinces value by 1 if the isCityVertexNotPresent is true
    // Group of Directly & Indirectly connected provinces;
    // Increment the totalNumOfProvinces value by 1 if the isCityVertexNotVisited is true
    // && Call the graphDFSIve(rowCityVertex) that takes rowCityVertex and visits all the connected cities
    // Create a graphDFSIve(rowCityVertex) function that traverses through all the connected cities
    // And it is helpful to traverse through the separately connected cities as well
    // Create a stack variable and initialize it to an empty array;
    // Create a currCityVertex variable and initialize it to the passed cityVertex
    // Run a while loop as long as the stack is not empty or in other words until all the connected vertices
    // are not visited/traversed
    // Update the currCityVertex value with the popped value from the stack;
    // Update the visitedCityVerticesHashmap with the currCityVertex as key and 'visited' as the value
    // Create a adjCityVertices variable and initialize it to all the adjacent cities for currCityVertex
    // in the adjacencyList
    // Run a forEach loop through the adjCityVertices and for each adjCityVertex 
    // Create a isAdjCityVertexNotVisited variable and initialize it to the boolean value true if the 
    // adjCityVertex has not been visited in the visitedCityVerticesHashmap else to the boolean value false
    // Push the adjCityVertex to the stack to visit other adjacent connected cities
    // Finally, we will have the number of provinces output value in the totalNumOfProvinces variable
    // so will return it;

    const provincesBDGraph = new ProvincesBiDirGraph();
    let totalNumOfProvinces = 0;

    const rowCitiesVertices = isConnected.length;
    const colCitiesVertices = isConnected[0].length;
    // const connectedCitiesGroupsArr = [];
    // const visitedCitiesConnections = new Map();

    for(let rowCityVertex = 0; rowCityVertex < rowCitiesVertices; rowCityVertex++){
        for(let colCityVertex = 0; colCityVertex < colCitiesVertices; colCityVertex++){
            const isProvincesConnected = isConnected[rowCityVertex][colCityVertex];

            if(rowCityVertex !== colCityVertex && isProvincesConnected === 1){
                let cityVertex1 = rowCityVertex;
                let cityVertex2 = colCityVertex;
                provincesBDGraph.addEdge(cityVertex1, cityVertex2);
            }
        }
    }

    const adjacencyList = provincesBDGraph.adjacencyList;
    const visitedCityVerticesHashmap = new Map();

    for(let rowCityVertex = 0; rowCityVertex < rowCitiesVertices; rowCityVertex++){
        const isCityVertexNotVisited = visitedCityVerticesHashmap.has(rowCityVertex) !== true;

        if(isCityVertexNotVisited){
            // Group of directly & indirectly connected provinces
            totalNumOfProvinces++;
            recGraphDFSIve(rowCityVertex);
        }
    }

    function recGraphDFSIve(cityVertex){

        const adjCityVertices = adjacencyList[cityVertex];

        // Base Case;
        if(adjCityVertices === undefined) return;

        visitedCityVerticesHashmap.set(cityVertex, 'visited');

        adjCityVertices.forEach(adjCityVertex => {
            const isAdjCityVertexNotVisited = visitedCityVerticesHashmap.has(adjCityVertex) !== true;

            if(isAdjCityVertexNotVisited){
                recGraphDFSIve(adjCityVertex);
            }
        });
    }

    // console.log('SOLVED USING DFS & ADJACENCYLIST');
    // console.log(adjacencyList);
    // console.log(visitedCityVerticesHashmap);
    // console.log(totalNumOfProvinces);

    return totalNumOfProvinces;
}
 