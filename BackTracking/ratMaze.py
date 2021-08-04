def canGo(current_x, current_y, maze):
    n = len(maze)
    m = len(maze[0])

    if current_x >= 0 and current_x <= n-1 and current_y >= 0 and current_y <= m-1:
        return True
    return False


def solveMaze(maze, possible_step):
    n = len(maze)
    m = len(maze[0])

    result = [[0 for x in range(m)] for x in range(n)]

    current_x = 0
    current_y = 0

    result[0][0] = 1

    if solve(maze, result, current_x, current_y, possible_step):
        printArray(result)
    else:
        print("No way out")


def solve(maze, result, current_x, current_y, n):
    nextstep_x = [1, 0]
    nextstep_y = [0, 1]

    if current_x == len(maze[0]) - 1 and current_y == len(maze) - 1 and maze[current_x][current_y] == 1:
        result[current_x][current_y] = 1
        return True

    for i in range(n):
        next_x = current_x + nextstep_x[i]
        next_y = current_y + nextstep_y[i]

        if canGo(next_x, next_y, maze):
            if maze[next_x][next_y] == 1:
                result[next_x][next_y] = 1
                if solve(maze, result, next_x, next_y, n):
                    return True

                # back tracking
                result[next_x][next_y] = 0

    return False


def printArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print("")


if __name__ == "__main__":
    # Initialising the maze
    maze = [[1, 0, 0, 0],
            [1, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 0, 1, 1]]

    possible_step = 2
    solveMaze(maze, possible_step)
