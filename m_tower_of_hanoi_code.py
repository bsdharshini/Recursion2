def tower(n,source,aux,dest):
    if n ==1:
        print(source,dest)
    if n == 0:
        return
    tower(n-1,source,dest,aux)
    print(source,dest)
    tower(n-1,aux,source,dest)

tower(3,'a','b','c')