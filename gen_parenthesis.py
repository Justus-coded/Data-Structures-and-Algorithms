from typing import List

def generate_par(n):
    def generate(p, left, right, parens=[]):
        if left:
            generate(p + '(', left-1, right)
        if right > left:
            generate(p + ')', left, right-1)
        if not right:
            parens += p,
        return parens
    return generate('', n, n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
