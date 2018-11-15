def triangles():
    row = [1]
    while True:
        yield(row)
        row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]  
         
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break



def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        pass
    else:
        move(n-1,a,c,b)
        print(a, '-->', c)
        move(n-1,b,a,c)

move(3,'A','B','C')



