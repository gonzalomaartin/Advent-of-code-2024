with open("long.txt", "r") as file:
    hash_right = dict()
    left = []
    result = 0
    for line in file: 
        current = ""
        for number in line.strip(): 
            if number.isdigit(): 
                current += number
            elif current != "":
                left.append(int(current))
                current = ""

        current = int(current)
        if current in hash_right: 
            hash_right[current] += 1 
        else: 
            hash_right[current] = 1
   
    
    for number in left: 
        if number in hash_right: 
            result += number * hash_right[number]

    print(result)