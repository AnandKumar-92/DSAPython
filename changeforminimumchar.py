class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        index = [0] * (26)
        for i in A:
            index[ord(i) - ord('a')] += 1  # first created an index array with elemnts as freq of index lik 0=a,1=b..........25=z

        index.sort()  # index is sorted from 0 to min values to max values
        # only minimum values less than B can be changed
        count = 26
        for i in range(25):
            if index[i] <= B:
                count -= 1  # those alphabets whose freq=0 will be dedcuted until we get total no of elemnts in our string
                B -= index[i]
        return count
Solution().solve("abcabbccd",3)

