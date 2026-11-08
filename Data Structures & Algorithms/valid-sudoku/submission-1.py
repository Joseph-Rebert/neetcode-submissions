class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## Check rows

        occurences = set()
        for row in board:
            for value in row:
                if value in occurences:
                    return False
                else:
                    if value != '.':
                        occurences.add(value)
            occurences.clear()

        print(occurences)
        
        ## Check columns


        for i in range(9):
            for j in range(9):
                value = board[j][i]
                if value in occurences:
                    return False
                else:
                    if value != '.':
                        occurences.add(value)
            occurences.clear()


        ## Check 3x3

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
        
            
        

        