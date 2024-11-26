class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        if len(edges)==0 and n==1:
            return 0
        if len(edges)==0 and n>1:
            return -1

        edges_present = []
        for edge in edges:
            edges_present.append(edge[0])
            edges_present.append(edge[1])
        
        edges_set=set(edges_present)
        if len(edges_set) != n:
            return -1

        Dominating_end = []
        Loosing_end = []

        for edge in edges:
            if edge[0] in Loosing_end:
                Loosing_end.append(edge[1])
            else:
                if edge[0] not in Dominating_end:
                    Dominating_end.append(edge[0])
                Loosing_end.append(edge[1])
            
        Dominating_end= list(set(Dominating_end) - set(Loosing_end))

        return Dominating_end[0] if len(Dominating_end)==1 else -1


        