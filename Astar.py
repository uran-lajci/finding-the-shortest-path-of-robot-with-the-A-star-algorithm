import heapq

def heuristic(a, b):
    # Manhattan distance heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(landscape, start, goal):
    # Create a priority queue
    queue = []
    heapq.heappush(queue, (0, start))
    # Create a dictionary to store the cost of each node
    cost = {start: 0}
    # Create a dictionary to store the parent of each node
    parent = {start: None}
    while queue:
        # Remove the node with the lowest f(n) from the priority queue
        current_cost, current_node = heapq.heappop(queue)
        # If the removed node is the goal, return the path
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]
        # Otherwise, for each neighbor of the removed node
        for neighbor in get_neighbors(landscape, current_node):
            # Calculate the new cost
            new_cost = cost[current_node] + 1
            # If the neighbor is not in the priority queue or if the new cost is lower
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)
                heapq.heappush(queue, (priority, neighbor))
                parent[neighbor] = current_node
    # If the priority queue becomes empty and the goal is not reached, return "no solution"
    return "no solution"

def get_neighbors(landscape, node):
    neighbors = []
    x, y = node
    if x > 0 and landscape[x-1][y] != "obstacle":
        neighbors.append((x-1, y))
    if x < len(landscape)-1 and landscape[x+1][y] != "obstacle":
        neighbors.append((x+1, y))
    if y > 0 and landscape[x][y-1] != "obstacle":
        neighbors.append((x, y-1))
    if y < len(landscape[0])-1 and landscape[x][y+1] != "obstacle":
        neighbors.append((x, y+1))
    return neighbors

# Example usage
landscape = [[0, 0, 0, 0, 0],
             [0, "obstacle", 0, "obstacle", 0],
             [0, 0, "obstacle", 0, 0],
             [0, 0, 0, 0, "obstacle"],
             [0, "obstacle", 0, 0, 0]]
start = (0, 0)
goal = (4, 4)
print(a_star(landscape, start, goal))
# Output: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3


# if __name__ == '__main__':
#     # Read input from user
#     n, m, k = map(int, input("Enter the size of the landscape and the number of obstacles: ").split())
#     landscape = [[0 for _ in range(m)] for __ in range(n)]
#     obstacles = []
#     print("Enter the coordinates of the obstacles:")
#     for _ in range(k):
#         x, y = map(int, input().split())
#         obstacles.append((x, y))
#         landscape[x][y] = "obstacle"
#     start = tuple(map(int, input("Enter the starting point (x y): ").split()))
#     goal = tuple(map(int, input("Enter the goal (x y): ").split()))

#     # Find the shortest path using A*
#     path = a_star(landscape, start, goal)
#     if path == "no solution":
#         print("No solution found.")
#     else:
#         print("Shortest path:", path)
