#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        k = 0
        dicti = {}
        sum = 0
        maxLen = 0
        for i in range(n):
            sum += arr[i]
            if(sum == k):
                maxLen = max(maxLen, i+1)
            rem = sum - k
            if rem in dicti:
                len = i - dicti[rem]
                maxLen = max(maxLen, len)
            if rem not in dicti:
                dicti[sum] = i
        return maxLen


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends