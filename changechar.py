class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = {}
        res = 0
        for i in A:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            if count[i] == B:
                res += 1
        return res
Solution().solve('aa')
