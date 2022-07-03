from datetime import datetime
import collections


class Solution():
    def criticalConnections(self, n, connections):
        def make_graph(connections):
            graph = collections.defaultdict(list)
            for conn in connections:
                graph[conn[0]].append(conn[1])
                graph[conn[1]].append(conn[0])
            return graph

        graph = make_graph(connections)
        connections = set(map(tuple, (map(sorted, connections))))
        colours = [0] * n
        edges = []
        #colour of node is `0 if node not passed
        #                   1 if node passed once and there are paths out of it
        #                   2 if node passed and there are no path out of it or all paths got to nodes of 2-colour
        cycle_detected = None

        def delete_connections_of_cycle(node):
            """
            deletes connections from cycle detected using edges
            :return:
            """
            connections.discard(tuple(edges[-1]))
            for edge in reversed(edges[:-1]):
                if node not in set(edge):
                    connections.discard(tuple(edge))
                else:
                    connections.discard(tuple(edge))
                    break


        def dfs(node, previous_node=None):

            colours[node] = 1
            stack = []

            for neighbor in graph[node]:
                if colours[neighbor] == 2 or neighbor == previous_node:
                    continue  # neighbour already visited and has no exits undeployed
                if colours[neighbor] == 1:
                    edges.append(sorted([node,neighbor]))
                    #colours[node] = 0
                    delete_connections_of_cycle(neighbor)
                    #connections.discard(tuple(sorted((node, neighbor))))
                    edges.pop(-1)
                    #return neighbor
                if colours[neighbor] == 0:
                    previous_node = node
                    edges.append(sorted([node,neighbor]))


                    cycle_detected = dfs(neighbor, previous_node)


                    colours[neighbor] = 2
                    edges.pop(-1)

            """
            if cycle_detected is not None:
                if cycle_detected != node:
                    colours[node] = 0
                    #connections.discard(tuple(sorted((node, neighbor))))
                    return cycle_detected
                else:
                    colours[node] = 1
                    #connections.discard(tuple(sorted((node, neighbor))))
                    continue
            """
            colours[node] == 2
            cycle_detected = None
            return cycle_detected
        dfs(0)
        return list(connections)

if __name__ == "__main__":
    sol = Solution()

    with open("1192.txt", "r") as f:
        n = int(f.readline())
        arr = []

        arr = f.readline()[2:-2].split("],[")
        arr1 = list(map( lambda x: [int(x.split(",")[0]), int(x.split(",")[1])] , arr))





    

    start_time = datetime.now()
    #print(sol.criticalConnections(3, [[0,1],[1,2]]))
    #print(sol.criticalConnections(4, [[0,1],[1,2],[2,0],[3,1]]))
    #print(sol.criticalConnections(4, [[0,3],[3,2],[2,0],[3,1]]))
    #print(sol.criticalConnections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[3,5]]))
    #print(sol.criticalConnections(7, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[3,5],[5,6]]))
    #print(sol.criticalConnections(6, [[0,1],[1,2],[1,4],[5,4],[2,3],[3,4]]))
    print(sol.criticalConnections(n, arr1))
    #print(sol.criticalConnections([1, 3, 1, 4, 1, 5, 10]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))