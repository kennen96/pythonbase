class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '(', left = 1, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

a=Solution()
print(a.generateParenthesis(4))

