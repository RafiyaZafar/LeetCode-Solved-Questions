#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		ans = []
		def print_subset_sums(arr, index, subset_sum):
            # Base case: when we reach the end of the array
            if index == len(arr):
                ans.append(subset_sum)
                return
        
            # Include the current element and recurse
            print_subset_sums(arr, index + 1, subset_sum + arr[index])
        
            # Exclude the current element and recurse
            print_subset_sums(arr, index + 1, subset_sum)
        print_subset_sums(arr,0,0)
        ans.sort()
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends