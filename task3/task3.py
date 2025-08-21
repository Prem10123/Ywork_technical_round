def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0) 

    for i, h in enumerate(heights):        
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()    
    return max_area

def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        current_row_area = largestRectangleArea(heights)
        max_area = max(max_area, current_row_area)
    return max_area

matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
print(f"The largest rectangle area is: {maximalRectangle(matrix)}")

