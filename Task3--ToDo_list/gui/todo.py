import sys

def find_paths(matrix, n, m):
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and matrix[x][y] != 0
    
    moves = {(0, 1): 'R', (1, 0): 'D', (0, -1): 'L', (-1, 0): 'U'}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    paths = []
    
    stack = [((0, 0), '')]
    
    while stack:
        (x, y), path = stack.pop()
        
        if x == n - 1 and (y == n - 1 or y == 0):
            paths.append(path)
            continue
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                new_path = path + moves[(dx, dy)]
                new_oxygen = m - matrix[nx][ny]
                stack.append(((nx, ny), new_path))
    
    return paths

def find_feasible_paths(matrix, n, m):
    available_paths = find_paths(matrix, n, m)
    feasible_paths = []
    
    for path in available_paths:
        oxygen = m
        for move in path:
            x, y = move_to_coordinate(move)
            oxygen -= matrix[x][y]
            if matrix[x][y] == 9:
                oxygen = m
            if oxygen < 0:
                break
        else:
            feasible_paths.append((path, oxygen))
    
    return feasible_paths

def move_to_coordinate(move):
    moves = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
    return moves[move]

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())

    feasible_paths = find_feasible_paths(matrix, n, m)

    if feasible_paths:
        print("The available paths are")
        for path in feasible_paths:
            print(path[0])
        print("\nThe feasible paths with remaining oxygen levels are")
        for path, oxygen in feasible_paths:
            print(f"{path} {oxygen}")
    else:
        print("No feasible path available to reach the destination")

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)  # Set recursion limit
    main()
