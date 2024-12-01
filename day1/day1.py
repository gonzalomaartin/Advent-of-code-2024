with open("long.txt", "r") as file:
    left, right = [], []
    result = 0
    for line in file: 
        current = ""
        for number in line.strip(): 
            if number.isdigit(): 
                current += number
            elif current != "": 
                left.append(int(current)) 
                current = ""
            
        right.append(int(current))
   
    
    left.sort()
    right.sort()
    for i in range(len(left)):
        result += abs(left[i] - right[i])

    print(result)