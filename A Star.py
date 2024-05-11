import heapq

class AStar:
    def __init__(self, graph):
        self.graph = graph

    def heuristic(self, node, start, end):
        raise NotImplementedError

    def search(self, start, end):
        queue = []
        heapq.heappush(queue, (0, start))

        costs = {}
        costs[start] = 0

        path = {}
        path[start] = None

        while queue:
            (cost, node) = heapq.heappop(queue)

            if node == end:
                break

            for next_node in self.graph.neighbors(node):
                new_cost = costs[node] + self.graph.cost(node, next_node)

                if next_node not in costs or new_cost < costs[next_node]:
                    costs[next_node] = new_cost
                    priority = new_cost + self.heuristic(next_node, start, end)
                    heapq.heappush(queue, (priority, next_node))
                    path[next_node] = node

        return path, costs
