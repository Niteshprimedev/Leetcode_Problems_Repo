class Solution {
    private void graphBFSIve(Integer currRoomKey, List<List<Integer>> roomsAdjList, Map<Integer, Boolean> visitedRoomsMap){
        Deque<Integer> roomsKeysQueue = new ArrayDeque<>();
        roomsKeysQueue.addFirst(currRoomKey);
        visitedRoomsMap.put(currRoomKey, true);

        while(!roomsKeysQueue.isEmpty()){
            currRoomKey = roomsKeysQueue.removeFirst();

            List<Integer> neighborsRoomsKeys = roomsAdjList.get(currRoomKey);

            for(int idxI = 0; idxI < neighborsRoomsKeys.size(); idxI++){
                Integer neighborRoomKey = neighborsRoomsKeys.get(idxI);

                if(!visitedRoomsMap.containsKey(neighborRoomKey)){
                    visitedRoomsMap.put(neighborRoomKey, true);
                    roomsKeysQueue.addFirst(neighborRoomKey);
                }
            }
        }
    }

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        // Meta Prep Time Practice
        // Graph Ive BFS Solution;

        int totalRooms = rooms.size();
        List<List<Integer>> roomsAdjList = rooms;
        Map<Integer, Boolean> visitedRoomsMap = new HashMap<>();

        graphBFSIve(0, roomsAdjList, visitedRoomsMap);

        int totalVisitedRooms = visitedRoomsMap.size();
        return totalRooms == totalVisitedRooms;
    }
}