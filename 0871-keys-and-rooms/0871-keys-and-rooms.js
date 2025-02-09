/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function(rooms) {
    // Revision;
    // Pseudocode
    // Solution using Graph AdjacencyList and DFS Traversal
    // Create a roomsAdjacencyList variable and initialize it to the rooms 
    // Create a visitedRoomsHashmap variable and initialize it to an empty hash map
    // Create a totalVisitedRooms variable and initialize it to 0
    // Create a graphDFSIterative function that takes a currRoomKey and marks all the rooms
    // as visited in the hash map if the rooms can be visited 
    // Do the following for the iterative DFS traversal
    // Create a stack variable and initialize it to an empty array
    // Create a currRoom variable and initialize it to currRoomKey param passed in the function
    // Push the currRoom value to the stack to start off the DFS iterative traversal
    // Increment the totalVisitedRooms value by 1 
    // Mark the currRoom or room as visited by setting key:value pair in the hashmap
    // Run a while loop as long as the stack is not empty or until all the rooms are visited/traversed
    // Create a roomsKey variable and initialize it to an array of keys available at currRoom
    // Run a for each loop through the roomsKey and for each roomKey
    // Create a isRoomsKeyNotVisited variable and initialize it to the boolean value true if the 
    // hashmap does not have the roomKey else to the boolean value false
    // Mark the currRoom or room as visited by setting key:value pair in the hashmap
    // Push the currRoom value to the stack to start off the DFS iterative traversal
    // Increment the totalVisitedRooms value by 1 
    // Finally, we will have checked whether it's possible to visit all the rooms with keys
    // or not; so will return false if the hashmap has less number rooms than the available rooms
    // Else will return true cause all the rooms were visited;

    const roomsAdjacencyList = rooms;
    const visitedRoomsHashmap = new Map();
    let totalVisitedRooms = 0;

    function graphDFSIterative(currRoomKey){
        
        const stack = [];
        let currRoom = currRoomKey;
        stack.push(currRoom);

        totalVisitedRooms++;
        visitedRoomsHashmap.set(currRoom, 'visited');

        while(stack.length){
            currRoom = stack.pop();

            const roomsKey = roomsAdjacencyList[currRoom];

            roomsKey.forEach(roomKey => {
                const isRoomsKeyNotVisited = visitedRoomsHashmap.has(roomKey) !== true;
                if(isRoomsKeyNotVisited){
                    visitedRoomsHashmap.set(roomKey, 'visited');

                    stack.push(roomKey);
                    totalVisitedRooms++;
                }
            })
        }
    }
    graphDFSIterative(0);

    // console.log(totalVisitedRooms, visitedRoomsHashmap);

    return totalVisitedRooms === rooms.length;
};