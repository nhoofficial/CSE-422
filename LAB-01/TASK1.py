s = []
m=[[0, 0, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0], [1, 1, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]
moves = [(0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1),(-1, 0), (1, 0), (0, 1)]
          #left #left_dia  #for_back #right_dia #left_back
def DFS(visited,moves,row, column, z):
    global s,m# here s as stack and m is the given matrix in the question.
    s.append((row, column))#pushing into the stack
    while len(s)>=1:#we will itearte the loop until stack is not empty.
        row,column=s[-1][0],s[-1][1]#inititializing the last tuple (x,y) as row and column
        for i in range(len(moves)):
            x,y = row + moves[i][0],column + moves[i][1]
            # here x denotes the new row and y denote the new column
            if x >= 0 and x <= len(m) - 1 and y >= 0 and y <= len(m[0]) - 1:#for the margin part
                if m[x][y] == 1:
                    for w in visited:#for all the adjacent
                        if (x,y)!=w and (x,y) not in visited:
                            visited.append((x, y))  # labeling them as visited.
                            return DFS(visited, moves, x, y, z + 1, )  # recursively calling DFS
            else:
                continue
        s.pop()#popping out from stack
    return z
def max_reg(m):
    lst = [0] * len(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 1:
                x = (i, j)  # i=row j=column
                c = DFS([x], moves, i, j, 1)
                lst[i] = c
    lst.sort()
    return lst[-1]

print(max_reg(m))






