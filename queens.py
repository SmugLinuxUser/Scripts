def queens(n):
    def Board(n):
        grind = []
        cunt = 0
        count = 0
        while cunt < n:
            grind.append([])
            cunt += 1
        for x in grind:
            while count < n:
                x.append(".")
                count += 1
            count = 0    
        return grind     

       

    def Checking(grid, n, row, col):
        ass = None
        for x in grid:
            if "Q" in x:
                if x.index("Q") == col:
                    return False
        def Diagonal(grid, n, row, col):
            ass = row - 1
            for yes, y in enumerate(grid):
                if yes == row:
                    if ass >= 0:
                        while ass >= 0:
                            if col + (row - ass) <= n - 1:
                                if grid[ass][col + (row - ass)] == "Q":
                                    
                                    
                                    return False
                            if col - (row - ass) >= 0:
                                if grid[ass][col - (row - ass)] == "Q":
                                    
                                    return False
                            ass -= 1    
                          
                    return True              
        if Diagonal(grid, n, row, col) == False:
            return False                    
        else:
            return True


    def backtrack(grid, n, helpme, bool, arson):
        hope = 0
        notlost = None
        if bool:
            helpme = arson
        for i, x in enumerate(grid):
            if "Q" not in x:
                if helpme < n - 1:
                    for oh, y in enumerate(x):
                        if bool:
                            if arson > 0:
                                arson -= 1
                                continue
                            bool = False    
                            continue
                                
                            
                        if Checking(grid, n, i, oh) == True:
                            grid[i][oh] = "Q"
                            helpme = x.index("Q")
                            arson = helpme
                            break
                    
            if "Q" not in x:
                arson = grid[i - 1].index("Q")
                grid[i - 1][arson] = "."

                if i - 1 == 0 and arson == n - 1:
                    print("que paso?")
                    return 
                sis = True
    
                backtrack(grid, n, helpme, sis, arson)
                return
            helpme = 0
               
            if i < n - 1:
                continue
            print(grid)
            if grid[0].index("Q") < n - 1:
                backtrack(Board(n), n, 0, True, grid[0].index("Q"))

            return grid
    backtrack(Board(n), n, 0, False, 0)      
    
queens(8)            

                 



                        


        
            