if __name__=="__main__":
     
    # P0, P1, P2, P3, P4 are the Process names here
    n = 3 # Number of processes
    m = 3 # Number of resources
     
    # Allocation Matrix
    alloc = [[ 1, 2, 1 ],
            [2, 0, 1 ],[2, 2, 1]]
     
    # MAX Matrix
    need = [[1, 0, 3 ],[0, 1, 2 ],
            [1, 2, 0]]
     
    avail = [0, 1, 2] # Available Resources
     
    f = [0]*n
    ans = [0]*n
    ind = 0
    for k in range(n):
        f[k] = 0
         
    
    y = 0
    for k in range(3):
        for i in range(n):
            if (f[i] == 0):
                flag = 0
                for j in range(m):
                    if (need[i][j] > avail[j]):
                        flag = 1
                        break
                 
                if (flag == 0):
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1
                     
    print("Following is the SAFE Sequence")
     
    for i in range(n - 1):
        print(" P", ans[i], " ->", sep="", end="")
    print(" P", ans[n - 1], sep="")
