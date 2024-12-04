with open("long.txt", "r") as file: 
    result = 0 
    lines = [line.strip() for line in file.readlines()]
    words = ["XMAS", "SAMX"]
    for i,line in enumerate(lines): 
        for j,letter in enumerate(line): 
            #Check horizontal right as we allow both XMAS and SAMX 
            if j + len(words[0]) <= len(line): 
                if line[j: j+len(words[0])] in words: 
                    result += 1
        #Check vertical down
            if i + len(words[0]) <= len(lines):
                vertical = "".join(line[j] for line in lines[i:i+len(words[0])])
                if vertical in words: 
                    result += 1

            #Check lower diagonals (an lower diagonal with XMAS is the same as an upper diagonal with SAMX and the other way around, so no need to check for both)
                if j + len(words[0]) <= len(line): #Lower right diagonal 
                    upper_diagonal = "".join(lines[i+aux][j+aux] for aux in range(len(words[0])))
                    if upper_diagonal in words: 
                        result += 1
                    #print(upper_diagonal)
                if j - len(words[0]) >= -1: 
                    lower_diagonal = "".join(lines[i+aux][j-aux] for aux in range(len(words[0])))
                    if lower_diagonal in words: 
                        result += 1
                    #print(lower_diagonal)
            
    
    print(result)
