from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()  # set to keep track of visited positions

        def dfs(r, c, i):
            if i == len(word):  # if we reach the end of the word, word found
                return True
            if (r < 0 or c < 0 or
                    r >= rows or c >= cols or
                    word[i] != board[r][c] or
                    (r, c) in path):
                return False

            path.add((r, c))  # mark current position as visited
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))  # remove current position from visited set

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


        

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(r,c,k):
            if k == len(word):
                return True
            if r<0 or r>= len(board) or c<0 or c>=len(board[0]) or board[r][c] != word[k]:
                return False

            temp = board[r][c]
            board[r][c] = ''

            if backtrack(r+1,c,k+1) or backtrack(r-1,c,k+1) or backtrack(r,c+1, k+1) or backtrack(r,c-1,k+1):
                return True

            board[r][c] = temp
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r,c,0):
                    return True
        return False

