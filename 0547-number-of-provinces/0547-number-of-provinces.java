class Solution {
    private void graphDFSIve(int currVertex, Map<Integer, List<Integer>> adjList, Map<Integer, Boolean> visitedVerticesMap){
        Stack<Integer> verticesStack = new Stack<>();
        verticesStack.push(currVertex);
        visitedVerticesMap.put(currVertex, true);

        while(!verticesStack.isEmpty()){
            currVertex = verticesStack.pop();

            List<Integer> currVertexNeighbors = adjList.get(currVertex);

            for(int idxI = 0; idxI < currVertexNeighbors.size(); idxI++){
                int neighborVertex = currVertexNeighbors.get(idxI);

                if(!visitedVerticesMap.containsKey(neighborVertex)){
                    visitedVerticesMap.put(neighborVertex, true);
                    verticesStack.push(neighborVertex);
                }
            }
        }
    }

    public int findCircleNum(int[][] isConnected) {
        int mRows = isConnected.length;
        int nCols = isConnected[0].length;

        Map<Integer, List<Integer>> adjList = new HashMap<>();

        for(int i = 0; i < mRows; i++){
            for(int j = 0; j < nCols; j++){
                int currCellVal = isConnected[i][j];

                if(i == j || currCellVal == 0){
                    continue;
                }

                int cityVertex1 = i;
                int cityVertex2 = j;

                if(!adjList.containsKey(cityVertex1)){
                    adjList.put(cityVertex1, new ArrayList<>());
                }

                adjList.get(cityVertex1).add(cityVertex2);
            }
        }

        Map<Integer, Boolean> visitedVerticesMap = new HashMap<>();
        int totalNumOfProvinces = 0;
        
        for(int currCityVertex = 0; currCityVertex < mRows; currCityVertex++){
            if(!adjList.containsKey(currCityVertex) && !visitedVerticesMap.containsKey(currCityVertex)){
                totalNumOfProvinces += 1;
            }
            else if(!visitedVerticesMap.containsKey(currCityVertex)){
                totalNumOfProvinces += 1;
                graphDFSIve(currCityVertex, adjList, visitedVerticesMap);
            }
        }
        
        return totalNumOfProvinces;
    }
}