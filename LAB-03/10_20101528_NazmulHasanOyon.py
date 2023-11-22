import math
import random as r
n=input()
win=int(n[-1]+n[-2])
min_r=int(n[4])
num=int(int(win)*1.5)
lst=[]
for i in range(8):
    a=r.randint(min_r,num)
    lst.append(a)
graph={'A':['B','C'], 'B':['D','E'],'C':['F','G'],'D':[lst[0],lst[1]],'E':[lst[2],lst[3]],'F':[lst[4],lst[5]],'G':[lst[6],lst[7]]}
#print(graph)

def alphabetapruning(position, depth, alpha, beta, graph, maximizingplayer):
    if depth == 0:
        return position
    if maximizingplayer is True:
        maxvalue = -math.inf
        for child in graph[position]:
            max_Eval = alphabetapruning(child, depth - 1, alpha, beta, graph, False)
            maxvalue = max(max_Eval, maxvalue)
            alpha = max(alpha, maxvalue)
            if beta <= alpha:
                break
        return maxvalue
    else:
        minvalue = math.inf
        for i in graph[position]:
            min_Eval = alphabetapruning(i, depth - 1, alpha, beta, graph, True)
            minvalue = min(min_Eval, minvalue)
            beta = min(beta, minvalue)
            if beta <= alpha:
                break
        return minvalue


b=(alphabetapruning('A',3,-math.inf,math.inf,graph,True))
print('Generated 8 random points between the minimum and maximum point limits:',lst)
print('Total points to win:',win)
print('Achieved point by applying alpha-beta pruning =',b)
if b>=win:
    print('The winner is Optimus prime.')
else:
    print('The winner is Megatron.')


if n[3]=='0':
    shuffle_num=8
else:
    shuffle_num=int(n[3])
c=0
new_lst=[]
for i in range(shuffle_num):
    r.shuffle(lst)
    graph2 = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [lst[0], lst[1]], 'E': [lst[2], lst[3]],'F': [lst[4], lst[5]], 'G': [lst[6], lst[7]]}
    k=alphabetapruning('A',3,-math.inf,math.inf,graph2,True)
    new_lst.append(k)
    if k>=win:
        c+=1
print('After the shuffle:')
print('List of all points values from each shuffle:',new_lst)
print('The maximum value of all shuffles:',max(new_lst))
print('Won',c,'times out of',shuffle_num,'number of shuffles')
