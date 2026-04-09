class Solution {
    private boolean graphDFSIve(int currVertex, Map<Integer, List<Integer>> adjList, int destination){
        Map<Integer, Boolean> visitedVerticesMap = new HashMap<>();

        Stack<Integer> verticesStack = new Stack<>();

        verticesStack.push(currVertex);
        visitedVerticesMap.put(currVertex, true);

        boolean isPathExist = false;

        while(!verticesStack.isEmpty()){
            currVertex = verticesStack.pop();

            if(currVertex == destination){
                isPathExist = true;
                break;
            }

            List<Integer> currVertexNeighbors = adjList.get(currVertex);
            for(int idxI = 0; idxI < currVertexNeighbors.size(); idxI++){
                int currNeighborVertex = currVertexNeighbors.get(idxI);

                if(!visitedVerticesMap.containsKey(currNeighborVertex)){
                    visitedVerticesMap.put(currNeighborVertex, true);
                    verticesStack.push(currNeighborVertex);
                }
            }
        }

        return isPathExist;
    }

    public boolean validPath(int n, int[][] edges, int source, int destination) {
        Map<Integer, List<Integer>> adjList = new HashMap<>();

        for(int[] currEdge : edges){
            int vertex1 = currEdge[0];
            int vertex2 = currEdge[1];

            if(!adjList.containsKey(vertex1)){
                adjList.put(vertex1, new ArrayList<>());
            }   
            if(!adjList.containsKey(vertex2)){
                adjList.put(vertex2, new ArrayList<>());
            }

            adjList.get(vertex1).add(vertex2);
            adjList.get(vertex2).add(vertex1);
        }
        

        boolean isPathExists = graphDFSIve(source, adjList, destination);
        return isPathExists;
    }
}