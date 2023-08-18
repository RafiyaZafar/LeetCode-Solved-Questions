#User function Template for python3
from operator import itemgetter
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meetings = []
        for i in range(n):
            meetings.append((start[i], end[i], i + 1))
        
        # Sort the meetings based on ending times
        meetings.sort(key=lambda x: x[1])
        
        answer = []
        limit = meetings[0][1]
        answer.append(meetings[0][2])
        
        for i in range(1, n):
            if meetings[i][0] > limit:
                limit = meetings[i][1]
                answer.append(meetings[i][2])
        
        return len(answer)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends