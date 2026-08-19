class DFS:
    def explore(self, graph, node, visited, result):

        visited.add(node)
        result.append(node)

        for adjele in graph[node]:
            if adjele not in visited:
                self.explore(graph, adjele, visited, result)

        return result
