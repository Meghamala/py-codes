# A Pyramid Descent Puzzle consists of a pyramid of positive integers. To solve the puzzle, you must find a path that traverses the pyramid from top to bottom visiting numbers whose product is a given target value. Each step in the path must go down one row, and go either one step to the left or one step to the right.

# For example, suppose the pyramid below has a target value of 2.

# 1		
# 2		3	
# 4		1		1
# A solver for this puzzle should output LR, indicating that the correct path starts from the 1 on top, goes Left to the 2 on the second row, then goes Right to the 1 in the center of the bottom row. (Note in particular that the successful path cannot go through the 1 at the end of the bottom row.) This gives the path shown in red below:

# 1		
# 2		3	
# 4		1		1

def find_path(pyramid, target):
    def dfs(row, col, curr):
        if row == len(pyramid) - 1:
            if curr == target:
                return ""
            return None


        next_r = row + 1

        # check if curr col exists in next row and then only move to col
        if col < len(pyramid[next_r]):
            left = dfs(next_r, col, curr * pyramid[next_r][col]) # return letter
            if left is not None:
                return "L" + left


        if col + 1 < len(pyramid) - 1:
            right = dfs(next_r, col + 1, curr * pyramid[next_r][col+1])
            if right is not None:
                return "R" + right


        return None # no valid path

    return dfs(0, 0, pyramid[0][0])

pyramid = [
    [2],
    [4, 3],
    [3, 2, 6],
    [2, 9, 5, 2],
    [10, 5, 2, 15, 5]
]
target = 720

path = find_path(pyramid, target)
if path:
    print("Path found:", path)
else:
    print("No path found")


