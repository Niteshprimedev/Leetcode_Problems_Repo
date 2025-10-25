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
    }
}