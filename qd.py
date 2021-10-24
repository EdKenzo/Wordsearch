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
            
        def check_horizontal_f(r,c ):
            check_hf = []
            if fit_right(string,w,h):
                for letter in range(len(string)):
                    if puzzle[r][c + letter] == string[letter]:#checks front
                        check_hf.append((r,c+letter))
                        
                    else:
                        check_hf.clear()
                        break
                    print(check_hf)
        def check_horizontal_b(r,c ):
            check_hb = []
            if fit_left(string,w,h):
                for letter in range(len(string)):
                    if puzzle[r][c - letter] == string[letter]:#checks back
                        check_hb.append((r,c+letter))
                        
                    else:
                        check_hb.clear()
                        break
                    print(check_hb)
        
        def check_vertical_u(r,c ):
            check_vu = []
            if fit_top(string,w,h):
                for letter in range(len(string)):
                    if puzzle[r + letter][c] == string[letter]:#checks up
                        check_vu.append((r+letter,c))
                        
                    else:
                        check_vu.clear()
                        break
                    print(check_vu)
        def check_vertical_d(r,c ):
            check_vd = []
            if fit_down(string,w,h):
                for letter in range(len(string)):
                    if puzzle[r - letter][c] == string[letter]:#checks down
                        check_vd.append((r-letter,c))
                        
                    else:
                        check_vd.clear()
                        break
                    print(check_vd)
                 
        def check_diag_ur(r,c ):
            check_dur = []
            shifth = 0
            shiftv = 0
            for letter in range(len(string)):
                if fit_right(string,w,h) and fit_top(string,w,h):
                    if puzzle[r + shiftv][c + shifth] == string[letter]:#up right
                        check_dur.append((r + shiftv, c + shifth))
                        shiftv += 1
                        shifth += 1                        
                    else:
                        check_dur.clear()
                        break
                    print(check_dur)
                    
        def check_diag_dl(r,c ):
            check_ddl = []
            shifth = 0
            shiftv = 0
            for letter in range(len(string)):
                if fit_left(string,w,h) and fit_down(string,w,h):
                    if puzzle[r - shiftv][c - shifth] == string[letter]:#down left
                        check_ddl.append((r - shiftv, c - shifth))
                        shiftv -= 1
                        shifth -= 1
                        
                    else:
                        check_ddl.clear()
                        break
                    print(check_ddl)
        def check_diag_ul(r,c ):
            check_dul = []
            shifth = 0
            shiftv = 0
            for letter in range(len(string)):
                if fit_left(string,w,h) and fit_top(string,w,h):
                    if puzzle[r + shiftv][c - shifth] == string[letter]: #up left
                        check_dul.append((r + shiftv, c - shifth))
                        shiftv += 1
                        shifth -= 1
                        
                    else:
                        check_dul.clear()
                        break
                    print(check_dul)
        def check_diag_dr(r,c):
            check_ddr = []
            shifth = 0
            shiftv = 0
            for letter in range(len(string)):
                if fit_right(string,w,h) and fit_down(string,w,h):
                    if puzzle[r - shiftv][c + shifth] == string[letter]: #down right
                        check_ddr.append((r - shiftv, c + shifth))
                        shiftv -= 1
                        shifth += 1
                        
                    else:
                        check_ddr.clear()
                        break
                    print(check_ddr)
        check_horizontal_b(r,c)
        check_horizontal_f(r,c)
        check_vertical_u(r,c)
        check_vertical_d(r,c)
        check_diag_ur(r,c)
        check_diag_dl(r,c)
        check_diag_ul(r,c)
        check_diag_dr(r,c)
        
    for r in range(h):
        for c in range(w):
            if puzzle[r][c] == string[0]:
                check(r,c )
            
            
            
wordsearch('runaround')

