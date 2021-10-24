def wordsearch(search_string):
    string = [char.upper() for char in search_string]
    

    puzzle = [['R', 'U', 'N', 'A', 'R', 'O', 'U', 'N', 'D', 'D', 'L'],
              ['E', 'D', 'C', 'I', 'T', 'O', 'A', 'H', 'C', 'Y', 'V'],
              ['Z', 'Y', 'U', 'W', 'S', 'W', 'E', 'D', 'Z', 'Y', 'A'],
              ['A', 'K', 'O', 'T', 'C', 'O', 'N', 'V', 'O', 'Y', 'V'],
              ['L', 'S', 'B', 'O', 'S', 'E', 'V', 'R', 'U', 'C', 'I'],
              ['B', 'O', 'B', 'L', 'L', 'C', 'G', 'L', 'P', 'B', 'D'],
              ['L', 'K', 'T', 'E', 'E', 'N', 'A', 'G', 'E', 'D', 'L'],
              ['I', 'S', 'T', 'R', 'E', 'W', 'Z', 'L', 'C', 'G', 'Y'],
              ['A', 'U', 'R', 'A', 'P', 'L', 'E', 'B', 'A', 'Y', 'G'],
              ['R', 'D', 'A', 'T', 'Y', 'T', 'B', 'I', 'W', 'R', 'A'],
              ['T', 'E', 'Y', 'E', 'M', 'R', 'O', 'F', 'I', 'N', 'U']]

    w = len(puzzle[0])
    h = len(puzzle)

    
    def check(r,c):
        def fit_right(string,w,h):
            if len(string) <= (w - c): #enough space to the right
                return True
        def fit_down(string,w,h):  
            if len(string) <= (h - r): #enough space to downwards  
                return True
        def fit_top (string,w,h):
            if len(string) <= r:#enough space on top 
                return True
        def fit_left(string,w,h):
            if len(string) <= c:#enough space to the left 
                return True
            
        ans = []
        if fit_right(string,w,h):
            for letter in range(len(string)):
                if puzzle[r][c + letter] == string[letter]:#checks front
                    ans.append((r,c+letter))
                        
                else:
                    ans.clear()
                    break
            if len(ans) == len(string):
                print(ans,"Hori front")
        
    
        if fit_left(string,w,h):
            for letter in range(len(string)):
                if puzzle[r][c - letter] == string[letter]:#checks back
                    ans.append((r,c-letter))
                        
                else:
                    ans.clear()
                    break
            if len(ans) == len(string):
                print(ans,"Hori back")
        
        
          
        if fit_top(string,w,h):
            for letter in range(len(string)):
                if puzzle[r + letter][c] == string[letter]:#checks up
                    ans.append((r+letter,c))
                        
                else:
                    ans.clear()
                    break
            if len(ans) == len(string):
                print(check_vu,"Vert up")
        
        if fit_down(string,w,h):
            for letter in range(len(string)):
                if puzzle[r - letter][c] == string[letter]:#checks down
                    ans.append((r-letter,c))
                        
                else:
                    ans.clear()
                    break
            if len(ans) == len(string):
                print(check_vd,"Vert down")
                 
        
        shifth = 0
        shiftv = 0
        for letter in range(len(string)):
            if fit_right(string,w,h) and fit_top(string,w,h):
                if puzzle[r + shiftv][c + shifth] == string[letter]:#up right
                    ans.append((r + shiftv, c + shifth))
                    shiftv += 1
                    shifth += 1                        
                else:
                    ans.clear()
                    break
            if len(ans) == len(string):
                print(ans,"Diag up right")
                    
        
        shifth = 0
        shiftv = 0
        for letter in range(len(string)):
            if fit_left(string,w,h) and fit_down(string,w,h):
                if puzzle[r - shiftv][c - shifth] == string[letter]:#down left
                    ans.append((r - shiftv, c - shifth))
                    shiftv -= 1
                    shifth -= 1
                        
                else:
                    ans.clear()
                    break
            if len(ans) == len(string):
                print(ans,"Diag down left")
        
        shifth = 0
        shiftv = 0
        for letter in range(len(string)):
            if fit_left(string,w,h) and fit_top(string,w,h):
                if puzzle[r + shiftv][c - shifth] == string[letter]: #up left
                    ans.append((r + shiftv, c - shifth))
                    shiftv += 1
                    shifth -= 1
                else:
                    ans.clear()
                    break
            if len(ans) == len(string):
                print(ans,"Diag up left")
        
        shifth = 0
        shiftv = 0
        for letter in range(len(string)):
            if fit_right(string,w,h) and fit_down(string,w,h):
                if puzzle[r - shiftv][c + shifth] == string[letter]: #down right
                    ans.append((r - shiftv, c + shifth))
                    shiftv -= 1
                    shifth += 1
                        
                else:
                    ans.clear()
                    break
            if len(ans) == len(string):
                print(ans,"Diag down right")

        
    for r in range(h):
        for c in range(w):
            if puzzle[r][c] == string[0]:
                check(r,c )
            
            
            
wordsearch('chaotic')
