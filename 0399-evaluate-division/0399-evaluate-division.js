/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function(equations, values, queries) {
    // Brute Force Solution:
    const adjacencyList = {};

    for(let idxI = 0; idxI < equations.length; idxI++){
        const equationVertex1 = equations[idxI][0];
        const equationVertex2 = equations[idxI][1];

        const isVertex1NotVisited = adjacencyList[equationVertex1] === undefined;
        if(isVertex1NotVisited){
            adjacencyList[equationVertex1] = [];
        }
        const isVertex2NotVisited = adjacencyList[equationVertex2] === undefined;
        if(isVertex2NotVisited){
            adjacencyList[equationVertex2] = [];
        }

        adjacencyList[equationVertex1].push([equationVertex2, values[idxI]]);
        adjacencyList[equationVertex2].push([equationVertex1, 1/values[idxI]]);
    }    

    console.log(adjacencyList);

    const queriesResult = queries.map(query => {
        const source = query[0];
        const destination = query[1];

        const isSourceNotPresent = adjacencyList[source] === undefined;
        const isDestinationNotPresent = adjacencyList[destination] === undefined;

        if(isSourceNotPresent || isDestinationNotPresent){
            return -1;
        }
        else if(source === destination){
            return 1;
        }

        const visitedVerticesHashmap = new Map();
        return graphDFS(source, destination, visitedVerticesHashmap, 1);
    });

    function graphDFS(source, destination, visitedVerticesHashmap, answer){

        visitedVerticesHashmap.set(source, 'visited');

        const queue = [];
        queue.push([source, answer]);

        while(queue.length){
            const weightedVertex = queue.shift();

            source = weightedVertex[0];
            answer = weightedVertex[1];

            if(source === destination){
                return answer;
            }

            const adjVertices = adjacencyList[source];
            adjVertices.forEach(adjVertex => {
                const isAdjVertexNotVisited = visitedVerticesHashmap.has(adjVertex[0]) !== true;
                if(isAdjVertexNotVisited){
                    visitedVerticesHashmap.set(adjVertex[0], 'visited');
                    queue.push([adjVertex[0], answer * adjVertex[1]]);
                }
            });
        }

        return -1;
    }

    /** 
    function recGraphDFS(source, destination, visitedVerticesHashmap, answer){
        if(source === destination){
            return answer;
        }
        const adjVertices = adjacencyList[source];

        visitedVerticesHashmap.set(source, 'visited');

        // adjVertices.forEach(adjVertex => {
        //     const isVertexNotVisited = visitedVerticesHashmap.has(adjVertex[0]) !== true;
        //     if(isVertexNotVisited){
        //         answer = answer * adjVertex[1];
        //         console.log(answer, adjVertex[0]);
        //         answer = recGraphDFS(adjVertex[0], destination, visitedVerticesHashmap, answer);
        //     }
        // });

        for(let adjVertex of adjVertices){
            const isVertexNotVisited = visitedVerticesHashmap.has(adjVertex[0]) !== true;
            if(isVertexNotVisited){
                if(adjVertex[0] === destination){
                    answer = answer * adjVertex[1];
                    break;
                }
                answer = answer * adjVertex[1];
                answer = recGraphDFS(adjVertex[0], destination, visitedVerticesHashmap, answer);
            }
        }

        return answer;
    }

    */

    return queriesResult;
};