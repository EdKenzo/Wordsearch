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
        total_ans = []
        
        def fit_right(string,w,h):
            if len(string) <= (w - c): #enough space to the right
                return True
        def fit_down(string,w,h):  
            if len(string) <= (h - r): #enough space to downwards  
                return True
        def fit_top (string,w,h):
            if len(string) <= (r + 1):#enough space on top 
                return True
        def fit_left(string,w,h):
            if len(string) <= (c + 1):#enough space to the left 
                return True
            
        
    
        def check_front(r,c):
            ans = []
            if fit_right(string,w,h):
                for letter in range(len(string)):
                    if puzzle[r][c + letter] == string[letter]:#checks front
                        ans.append((r,c+letter))
                            
                    else:
                        ans.clear()
                        break
                if len(ans) == len(string):
                    return(ans)
                    
            return False
        
        def check_back(r,c):
            ans = []
            if fit_left(string,w,h):
                for letter in range(len(string)):
                    if puzzle[r][c - letter] == string[letter]:#checks back
                        ans.append((r,c-letter))
                            
                    else:
                        ans.clear()
                        break
                if len(ans) == len(string):
                    return(ans)
                    
            return False
        
        
        def check_up(r,c):
            ans = []
            if fit_top(string,w,h):
                for letter in range(len(string)):
                    if puzzle[r - letter][c] == string[letter]:#checks up
                        ans.append((r-letter,c))
                            
                    else:
                        ans.clear()
                        break
                if len(ans) == len(string):
                    return(ans)
            return False
        
        def check_down(r,c):
            ans = []
            if fit_down(string,w,h):
                for letter in range(len(string)):
                    if puzzle[r + letter][c] == string[letter]:#checks down
                        ans.append((r + letter,c))     
                    else:
                        ans.clear()
                        break
                if len(ans) == len(string):
                    return(ans)
            return False
                 
        def check_up_right(r,c):
            ans = []
            if fit_right(string,w,h) and fit_top(string,w,h):
                for letter in range(len(string)):            
                    if puzzle[r - letter][c + letter] == string[letter]:#up right
                        ans.append((r - letter, c + letter))
                    else:
                        ans.clear()
                        break
                if len(ans) == len(string):
                    return(ans)
            return False
                    
        
               
        def check_down_left(r,c):
            ans = []
            if fit_left(string,w,h) and fit_down(string,w,h):
                for letter in range(len(string)):
                    if puzzle[r + letter][c - letter] == string[letter]:#down left
                        ans.append((r + letter, c - letter))
                    else:
                        ans.clear()
                        break
                if len(ans) == len(string):
                    return(ans)
            return False
    
        
        def check_up_left(r,c):
            ans = []
            if fit_left(string,w,h) and fit_top(string,w,h):
                for letter in range(len(string)):
                    if puzzle[r - letter][c - letter] == string[letter]: #up left
                        ans.append((r - letter, c - letter))
                        
                    else:
                        ans.clear()
                        break
                if len(ans) == len(string):
                    return(ans)
            return False
        
        
        def check_down_right(r,c):
            ans = []
            if fit_right(string,w,h) and fit_down(string,w,h):
                for letter in range(len(string)):
                    if puzzle[r + letter][c + letter] == string[letter]: #down right
                        ans.append((r + letter, c + letter))  
                    else:
                        ans.clear()
                        break
                if len(ans) == len(string):
                    return(ans)
            return False

        cf = check_front(r,c)
        if cf : 
            total_ans.append(cf)
                        
        cb = check_back(r,c)
        if cb:
            total_ans.append(cb)
        
        cu = check_up(r,c)
        if cu:
            total_ans.append(cu)
            
        cd = check_down(r,c)
        if cd:
            total_ans.append(cd)
        
        cur = check_up_right(r,c)
        if cur:
            total_ans.append(cur)
        
        cul = check_up_left(r,c)
        if cul:
            total_ans.append(cul)
            
        cdl = check_down_left(r,c)
        if cdl:
            total_ans.append(cdl)
        
        cdr = check_down_right(r,c)
        if cdr: 
            total_ans.append(cdr)
        return total_ans

        
        
        
        
        

        
    for r in range(h):
        for c in range(w):
            if puzzle[r][c] == string[0]:
                print(check(r,c))
                
            
    
            
            
            
wordsearch('lee')
