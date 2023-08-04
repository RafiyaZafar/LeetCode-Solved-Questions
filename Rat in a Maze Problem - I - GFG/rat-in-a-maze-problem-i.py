#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        def solve(i, j, m, n, ans, move, vis, di, dj):
            if(i == n-1 and j == n-1):
                ans.append(move)
                return

            dir = 'DLRU'
            for ind in range(4):
                nexti =  i + di[ind]
                nextj =  j + dj[ind]

                if(nexti >= 0 and nextj >= 0 and nexti < n and nextj < n and not vis[nexti][nextj] and m[nexti][nextj] == 1):
                    vis[i][j] = 1
                    solve(nexti, nextj, m, n, ans, move + dir[ind], vis, di, dj)
                    vis[i][j]=0

        ans = []
        vis= [[0]*n for _ in range (n)]
        di = [+1,0,0,-1]
        dj = [0,-1,+1,0]
        if(m[0][0] == 1):
            solve(0,0, m,n,ans,"",vis,di,dj)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends