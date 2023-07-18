class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        maxm, minm = 0, float('inf')
        cnt=0
        count = {}
        for i in A:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
                if maxm < i:
                    maxm = i
                if minm > i:
                    minm = i
        while minm<=maxm:
            if minm in count:
                for i in range(count[minm]):
                    A[cnt]=minm
                    cnt+=1
            minm+=1


        print(f'sorted array : {A}')




Solution().solve([1, 3, 1,5,10])
