import sys
sys.setrecursionlimit(10000)
def sudoku(board):
    freedom = []
    despair = []
    def Checking(board, n, row, col):
        if n in board[row]:
            return False
        hope = 0    
        while hope < 9:
            if board[hope][col] == n:
                return False
            hope += 1            
        if row == 0 or row == 1 or row == 2:
            peace = 0
        if row == 3 or row == 4 or row == 5:
            peace = 3 
        if row == 6 or row == 7 or row == 8:
            peace = 6           
        if col == 0 or col == 1 or col == 2:
            gf = 0
        if col == 3 or col == 4 or col == 5:
            gf = 3 
        if col == 6 or col == 7 or col == 8:
            gf = 6 
        hope = 3
        berry = 3
        for val, x in enumerate(board[peace::]):
            if hope == 0:
                break
            for nin, y in enumerate(x[gf::]):
                if berry == 0:
                    break
                if y == n:
                    return False  
                berry -= 1    
            hope -= 1
            berry = 3       
        return True              


    def recursion(board, checkpoint):
        for val, x in enumerate(board):
            if 0 in x:
                for yes, y in enumerate(x):
                    if y == 0:
                        for z in range(1, 10):
                            if checkpoint > 0:
                                checkpoint -= 1
                                continue
                                
                            if Checking(board, z, val, yes):
                                board[val][yes] = z
                                

                                freedom.append(z)
                                despair.append(yes)
                                    
                                #print(board[val], "and despair", despair ) 
                                break
                    if board[val][yes] == 0:
                        
                        if despair[-1] > yes:
                            board[val - 1][despair.pop()] = 0
                        else:
                            board[val][despair.pop()] = 0  
                        
                        #print(freedom, "/n", despair ) 
                        #print(board)
                        recursion(board, freedom.pop())
                        return        
                    if val == 8 and yes == 8:
                        print("huh?")
                        print(board)
                        return board
    recursion(board, 0)                    
sudoku([[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]])                        

            
