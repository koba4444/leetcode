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
        edges = [] # edges on the path

        # colour of node is `0 if node not passed
        #                   1 if node passed once and there are paths out of it
        #                   2 if node passed and there are no path out of it or all paths got to nodes of 2-colour


        def traversal(n):
            path_walked = [None] * n
            node = 0
            neighbor = 0
            path_walked[0] = node
            previous = None
            travers_ind = [len(graph[i]) for i in range(n) if i in graph.keys() or 0]
            depth = 0
            curr_ind = [0] * n
            edges_to_delete = set()
            while True: #
                colours[node] = 1
                go_up = False


                for ind in range(curr_ind[depth], travers_ind[path_walked[depth]]):

                    neighbor = graph[node][ind]
                    if colours[neighbor] == 2 or neighbor == previous:
                        continue  # neighbour already visited and has no exits undeployed. Go one step back.
                    if colours[neighbor] == 1:
                        edges.append(sorted([node, neighbor]))
                        #print(edges)
                        ind_from = path_walked.index(neighbor)

                        #print(edges[ind_from:])
                        #print(edges_to_delete)
                        edges_to_delete |= set(map(tuple,edges[ind_from:]))

                        #delete_connections_of_cycle(neighbor) # the cycle was found


                        edges.pop(-1)
                        continue # go to next neighbor

                    if colours[neighbor] == 0: # go step ahead
                        edges.append(sorted([node, neighbor]))
                        curr_ind[depth] = ind + 1
                        colours[neighbor] = 1
                        previous = node
                        depth += 1
                        path_walked[depth] = neighbor
                        node = neighbor
                        go_up = True
                        break

                if not go_up:
                    colours[node] = 2  # no way out. Make step back
                    if edges: edges.pop(-1)
                    path_walked[depth] = None
                    curr_ind[depth] = 0
                    depth -= 1
                    if depth >= 0: node = path_walked[depth]
                if depth == -1: break
            return edges_to_delete


        connections -= traversal(n)
        return list(connections)


if __name__ == "__main__":
    sol = Solution()

    with open("1192.txt", "r") as f:
        n = int(f.readline())
        arr = []

        arr = f.readline()[2:-2].split("],[")
        arr1 = list(map(lambda x: [int(x.split(",")[0]), int(x.split(",")[1])], arr))

    start_time = datetime.now()
    """
    print(sol.criticalConnections(3, [[0,1],[1,2]]))
    print(sol.criticalConnections(4, [[0,1],[1,2],[2,0],[3,1]]))
    print(sol.criticalConnections(4, [[0,3],[3,2],[2,0],[3,1]]))
    print(sol.criticalConnections(6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[3,5]]))
    print(sol.criticalConnections(7, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[3,5],[5,6]]))
    print(sol.criticalConnections(6, [[0,1],[1,2],[1,4],[5,4],[2,3],[3,4]]))
    """
    print(sol.criticalConnections(n, arr1))

    print(sol.criticalConnections(10, [[1,0],[2,0],[3,0],[4,1],[5,3],[6,1],[7,2],[8,1],[9,6],[9,3],[3,2],[4,2],[7,4],[6,2],[8,3],[4,0],[8,6],[6,5],[6,3],[7,5],[8,0],[8,5],[5,4],[2,1],[9,5],[9,7],[9,4],[4,3]]))
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))