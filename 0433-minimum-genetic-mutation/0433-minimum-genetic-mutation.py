class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Logic: No Clue -> Just perform BFS
        gene_banks_map = set(bank)

        def graph_bfs(curr_gene):
            genes_queue = []

            genes_queue.append((curr_gene, 0))
            visited_set = set()

            min_mutations = -1
            while len(genes_queue):
                curr_gene, curr_mutation = genes_queue.pop(0)

                if curr_gene == endGene:
                    min_mutations = curr_mutation
                    break

                if curr_gene not in visited_set:
                    visited_set.add(curr_gene)

                    for char_idx in range(len(curr_gene)):
                        for nucleotide in 'ACGT':
                            if curr_gene[char_idx] != nucleotide:
                                next_gene = curr_gene[:char_idx] + nucleotide + curr_gene[char_idx + 1:]
                                if next_gene in gene_banks_map and next_gene not in visited_set:
                                    genes_queue.append((next_gene, curr_mutation + 1))
            
            return min_mutations

        min_mutations = graph_bfs(startGene)

        return min_mutations