class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        que = deque([(startGene, 0)])
        visited = set([startGene])
        choices = ['A', 'G', 'C', 'T']

        while que:
            gene, step = que.popleft()
            if gene == endGene:
                return step

            genearr = [ch for ch in gene]
            for i in range(len(gene)):
                for choice in choices:
                    genearr[i] = choice
                    new_gene = ''.join(genearr)
                    if new_gene in bank_set and new_gene not in visited:
                        que.append((new_gene, step + 1))
                        visited.add(new_gene)
                genearr[i] = gene[i]

        return -1

