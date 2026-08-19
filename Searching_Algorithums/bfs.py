from collections import defaultdict, deque


class Node:
    def __init__(self , node , side):
        self.node = node
        self.side = side
        
class BFS: 
    def shortestPath(self, edges, src, destination):
        # adjacency list
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist = defaultdict(lambda: float('inf'))

        parent = {}
        dist[src] = 0
        parent[src] = None

        q = deque()
        q.append(src)

        while q:
            node = q.popleft()
            if node == destination:
                break

            for neighbor in adj[node]:
                if dist[node] + 1 < dist[neighbor]:
                    dist[neighbor] = dist[node] + 1
                    parent[neighbor] = node
                    q.append(neighbor)

        if dist[destination] == float('inf'):
            return [], -1

        path = []
        current = destination
        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()
        return path, dist[destination]

    def undirectional_bfs(self , edge , src , destination):
        adj = defaultdict(list)
        for u , v in edge:
            adj[u].append(v)
            adj[v].append(u)

        q = deque()
        visited_src = {src}
        visited_dest = {destination}

        parent_src = {src: None}
        parent_destination = {destination: None}

        q.append(Node(src, 0))
        q.append(Node(destination, 1))

        while q:
            current_node = q.popleft()
            node = current_node.node
            side = current_node.side

            if side == 0:
                for adjele in adj[node]:
                    if adjele not in visited_src:
                        visited_src.add(adjele)
                        parent_src[adjele] = node

                        if adjele in visited_dest:
                            return self.createPath(adjele, parent_src, parent_destination)

                        q.append(Node(adjele, 0))

            if side == 1:
                for adjele in adj[node]:
                    if adjele not in visited_dest:
                        visited_dest.add(adjele)
                        parent_destination[adjele] = node

                        if adjele in visited_src:
                            return self.createPath(adjele, parent_src, parent_destination)

                        q.append(Node(adjele, 1))

        return [], -1

    def createPath(self, meeting, parent_src, parent_destination):
        path_src = []
        current = meeting
        while current is not None:
            path_src.append(current)
            current = parent_src.get(current)
        path_src.reverse()


        path_dest = []
        current = parent_destination.get(meeting)
        while current is not None:
            path_dest.append(current)
            current = parent_destination.get(current)

        full_path = path_src + path_dest
        return full_path, len(full_path) - 1
