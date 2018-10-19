from __future__ import print_function

class AStarGraph(object):
    
    # Takes a barrier that represents obstacles to find a path around
    def __init__(self, barriers):
        self.barriers = []
        self.barriers.append(barriers)

    def heuristic(self, start, end):
        # Heuristic to decide to go to the square next to it or diagonal
        D = 1
        D2 = 1
        dx = abs(start[0] - end[0])
        dy = abs(start[1] - end[1])
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

    def getneighbors(self, pos):
        n = []
        # Define legal movement
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            x2 = pos[0] + dx
            y2 = pos[1] + dy
            if x2 < 0 or x2 > 7 or y2 < 0 or y2 > 7:
                continue
            n.append((x2, y2))
        return n

    def getcost(self, a, b):
        for barrier in self.barriers:
            if b in barrier:
                return 100  # Extremely high cost to enter barrier squares
        return 1  # Normal movement cost


def AStarSearch(start, end, grid):
    G = {}  # Actual movement cost to each position from the start position
    F = {}  # Estimated movement cost of start to end going via this position

    G[start] = 0
    F[start] = grid.heuristic(start, end)

    closednodes = set()
    opennodes = set([start])
    cameFrom = {}

    while len(opennodes) > 0:
        # Get the node in the open list with the lowest F score
        current = None
        currentFscore = None
        for pos in opennodes:
            if current is None or F[pos] < currentFscore:
                currentFscore = F[pos]
                current = pos

        # Check if we have reached the end
        if current == end:
            # Retrace our route backward
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            path.reverse()
            # return path, F[end]  # Done!
            return path

        # Mark the current node as closed
        opennodes.remove(current)
        closednodes.add(current)

        # Update scores for vertices near the current position
        for neighbour in grid.getneighbors(current):
            if neighbour in closednodes:
                continue  # We have already processed this node exhaustively
            candidateG = G[current] + grid.getcost(current, neighbour)

            if neighbour not in opennodes:
                opennodes.add(neighbour)  # Discovered a new node
            elif candidateG >= G[neighbour]:
                continue  # This G score is worse than previously found

            # Adopt this G score
            cameFrom[neighbour] = current
            G[neighbour] = candidateG
            H = grid.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H

    raise RuntimeError("A* failed to find a solution")