class EdgePair{
    int d;
    int w;

    EdgePair(int d, int w){
        this.d = d;
        this.w = w;
    }
}

class FlightCity{
    int stopsCount;
    int currCity;
    int currCost;

    public FlightCity(int stopsCount, int currCity, int currCost){
        this.stopsCount = stopsCount;
        this.currCity = currCity;
        this.currCost = currCost;
    }

}

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        /*
        int cheapestFlightCost = Integer.MAX_VALUE;

        // Directed graph;
        HashMap<Integer, List<EdgePair>> graph = new HashMap<>();

        for(int[] flight : flights){
            int s = flight[0];
            int d = flight[1];
            int w = flight[2];

            if(!graph.containsKey(s)){
                graph.put(s, new ArrayList<>());
            }

            graph.get(s).add(new EdgePair(d, w));
        }

        int[] cheapestPrices = new int[n];

        Arrays.fill(cheapestPrices, Integer.MAX_VALUE);
        PriorityQueue<FlightCity> minHeap = new PriorityQueue<>(Comparator.comparingInt(obj -> obj.stopsCount));
        
        minHeap.add(new FlightCity(0, src, 0));
        cheapestPrices[src] = 0;

        while(!minHeap.isEmpty()){
            FlightCity currFlight = minHeap.poll();

            int stopsCount = currFlight.stopsCount;
            int currFlightCity = currFlight.currCity;
            int currCost = currFlight.currCost;

            if(currFlightCity == dst){
                cheapestFlightCost = Math.min(cheapestFlightCost, currCost);
            }

            if(stopsCount > k){
                continue;
            }

            List<EdgePair> neighbors = new ArrayList<>();

            if(graph.containsKey(currFlightCity)){
                neighbors = graph.get(currFlightCity);
            }

            for(EdgePair neighbor : neighbors){
                int neighborCity = neighbor.d;
                int neighborCost = neighbor.w;

                if(currCost + neighborCost < cheapestPrices[neighborCity] && stopsCount <= k){
                    cheapestPrices[neighborCity] = currCost + neighborCost;
                    minHeap.add(new FlightCity(stopsCount + 1, neighborCity, cheapestPrices[neighborCity]));
                }
            }
        }

        return cheapestFlightCost == Integer.MAX_VALUE ? -1 : cheapestFlightCost;
        */

        // Build adjacency list
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for(int[] flight : flights){
            int s = flight[0];
            int d = flight[1];
            int w = flight[2];

            graph.putIfAbsent(s, new ArrayList<>());
            graph.get(s).add(new int[]{d, w});
        }

        // Queue: {city, totalCost, stops}
        Deque<int[]> queue = new ArrayDeque<>();
        queue.offerLast(new int[] {src, 0, 0});

        // Track minimum cost to reach each city within <= k stops
        int[] cheapestPrices = new int[n];
        Arrays.fill(cheapestPrices, Integer.MAX_VALUE);
        cheapestPrices[src] = 0;

        int cheapestFlightCost = Integer.MAX_VALUE;

        while (!queue.isEmpty()) {
            int[] curr = queue.pollFirst();
            int currCity = curr[0];
            int currCost = curr[1];
            int stopsCount = curr[2];

            if (currCity == dst) {
                cheapestFlightCost = Math.min(cheapestFlightCost, currCost);
            }

            // Stop if stops exceed limit
            if (stopsCount > k) continue; // +1 because src counts as 0 stop

            if (!graph.containsKey(currCity)) continue;

            for (int[] neighbor : graph.get(currCity)) {
                int neighborCity = neighbor[0];
                int neighborCost = neighbor[1];

                int nextCost = currCost + neighborCost;

                // Only explore if cost is cheaper
                if (nextCost < cheapestPrices[neighborCity] && stopsCount <= k) {
                    cheapestPrices[neighborCity] = nextCost;
                    queue.offerLast(new int[]{neighborCity, nextCost, stopsCount + 1});
                }
            }
        }

        return cheapestFlightCost == Integer.MAX_VALUE ? -1 : cheapestFlightCost;
    }
}