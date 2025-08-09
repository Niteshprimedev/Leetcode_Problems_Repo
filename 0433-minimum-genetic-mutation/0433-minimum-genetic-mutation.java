class Pair<G,M>{
    G currGene;
    M currMutations;

    Pair(G currGene, M currMutations){
        this.currGene = currGene;
        this.currMutations = currMutations;
    }
}

class Solution {
    public int minMutation(String startGene, String endGene, String[] bank) {
        HashSet<String> genesBankSet = new HashSet<>();

        for(String currGene : bank){
            genesBankSet.add(currGene);
        }

        HashSet<String> visitedSet = new HashSet<>();
        Deque<Pair<String, Integer>> genesQueue = new ArrayDeque<>();

        genesQueue.addLast(new Pair<>(startGene, 0));
        int totalMutations = -1;
        visitedSet.add(startGene);

        while(genesQueue.size() > 0){
            Pair<String, Integer> firstEl = genesQueue.removeFirst();

            String currGene = firstEl.currGene;
            int currMutations = firstEl.currMutations;

            if(currGene.equals(endGene)){
                totalMutations = currMutations;
                break;
            }

            for(int idxI = 0; idxI < currGene.length(); idxI++){
                for(char currChar : new char[] {'A','C','G','T'}){

                    String newGene = currGene.substring(0, idxI) + currChar + currGene.substring(idxI + 1);
                    if(!visitedSet.contains(newGene) && genesBankSet.contains(newGene)){
                        visitedSet.add(newGene);
                        genesQueue.addLast(new Pair<>(newGene, currMutations + 1));
                    }
                }
            }
        }

        return totalMutations;
    }
}