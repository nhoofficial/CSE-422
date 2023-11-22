import random as r
i, t = list(map(int, input().split()))
d = {}
for k in range(i):
    pname, pscore = input().split(' ')
    pscore = int(pscore)
    d[k] = [pname, pscore]

def population():
    p = []
    for outer in range(10):
        lst = [0] * i
        for j in range(i):
            num = r.randrange(0, 2)
            lst[j] = num
        c = 0
        for l in lst:
            if l == 0:
                c += 1
        if c == len(lst):
            continue
        else:
            if lst not in p:
                p.append(lst)
    return p
def fitness(d,p,t):
    fitness = []
    for i in range(len(p)):
        f = 0
        for j in range(len(p[i])):
            if p[i][j]==1:
                f+=d[j][1]
        f_new=abs(t-f)
        fitness.append(f_new)
    fitness.sort()
    return fitness
def selection(p,fitness):
    parent1 = None
    parent2 = None
    for i in range(len(p)):
        f = 0
        for j in range(len(p[i])):
            if p[i][j] == 1:
                f += d[j][1]
        if f==fitness[-1]:
            idx=p.index(p[i])
            parent1=p[idx]
        elif f==fitness[-2]:
            idx1 = p.index(p[i])
            parent2 = p[idx1]
    return parent1,parent2
def crossover(parent1, parent2,p):
    global d,t
    x=fitness(d,p,t)
    n=r.randrange(0,len(p))
    child1 = parent1[0:n] + parent2[n:]
    child2 = parent2[0:n] + parent1[n:]
    sum1,sum2=0,0
    for i in range(len(parent1)):
        sum1+=child1[i]
        sum2+=child2[i]
    idx=p.index(parent1)
    idx1=p.index(parent2)
    if sum1>x[-1] or sum1>x[-2]:
        p[idx]=child1
    else:
        if sum2 > x[-1] or sum1 > x[-2]:
            p[idx1] = child2


def mutation(p):
    for i in range(len(p-2),len(p)):
        s=0
        k=0
        new=p
        n=r.randint(0,len(p))
        for j in range(len(p[i])):
            s+=p[i][j]
        if new[i][n]==1:
            new[i][n]=0
        else:
            new[i][n] = 1
        for j in range(len(new[i])):
            k+=new[i][j]
        if s<k:
            p[i]=new[i]
        else:
            continue
    return p

def genetic_algo(d,t):
    for gen in range(50000):
        a = population()
        b = fitness(d, a, t)
        if b[-1] == t:
            c,d=selection(a,b)
            idx=None
            for i in range(len(a)):
                if c==a[i]:
                    idx=i
                    break
            lst=[]
            winner=''
            for i in range(len(a[idx])):
                winner+=a[idx][i]
                if a[idx][i]==1:
                    lst.append(d[i][0])
            print(lst)
            print(winner)
            return
        else:
            c,d=selection(a,b)
            e=crossover(c,d,a)
            f=mutation(a)
    return -1
genetic_algo(d,t)
