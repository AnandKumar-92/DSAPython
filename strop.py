class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        res = ""
        vowel = "aeiou"
        for i in range(len(A)):
            if ord(A[i]) < 65 or ord(A[i]) > 90:
                if A[i] in vowel:
                    res += "#"
                else:
                    res += A[i]
        return res + res


Solution().solve("hgUe")
