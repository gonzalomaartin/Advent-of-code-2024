with open("long.txt", "r") as file: 
    result = 0 
    lines = [line.strip() for line in file.readlines()]
    words = ["MAS", "SAM"] #Possible strings 
    for i,line in enumerate(lines): 
        for j,letter in enumerate(line):
            if i + len(words[0]) <= len(lines) and j+2 <= len(line)-1: #There's room for an X block 
                upper_diagonal = "".join(lines[i+aux][j+aux] for aux in range(3)) #Calculating the lower diagonal 
                lower_diagonal = "".join(lines[i+aux][j+2-aux] for aux in range(3)) #Calculating the upper diagonal 
                #print(upper_diagonal, lower_diagonal)
                if upper_diagonal in words and lower_diagonal in words: #Conditions for an X-MAS block to count
                        result += 1
            
    
    print(result)
