inputfile2=open("input2.txt", "r")
m=int(inputfile2.readline())
n=int(inputfile2.readline())
mat2=inputfile2.readlines()
lst=[]
for e in mat2:
  if e[-1] == '\n':
    s = e[:-1].split()
  else:
    s = e.split()
  lst.append(s)
time,count=0,0
def alien_tracker(lst):
    al=[]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j]=='A':
                al.append((i,j))
    return al
def human_tracker(lst):
    a=[]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j]=='H':
                a.append((i,j))
    return a
q=[]
def BFS(lst,visited,row, column):
    global time,q,count
    q.append((row,column))#enqueueing process
    moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    while len(q)>0:
        v=q[0]
        x,y=v
        for i in range(len(moves)):
            x, y = row + moves[i][0], column + moves[i][1]
            # here x denotes the new row and y denote the new column
            if x >= 0 and x <= len(lst) - 1 and y >= 0 and y <= len(lst[0]) - 1:  # for the margin part
                if lst[x][y] == 'H':
                    for w in visited:  # for all the adjacent
                        if (x, y) != w and (x, y) not in visited:
                            visited.append((x, y))
        q = q[1:]
        time+=1
    h=human_tracker(lst)
    for i in h:
        if i not in q:
            count+=1

      # labeling them as visited.
#b=alien_tracker(lst)
b=alien_tracker(lst)
for i in range(len(lst)):
    for j in range(len(lst[i])):
            if lst[i][j] == 'H':
                for k in b:
                    x = (i, j)
                    c = BFS(lst,[k], x[0], x[1])


print('Time:',time,'minutes')
if count==0:
    print('no one survived')
else:
    print(count,'survived.')
