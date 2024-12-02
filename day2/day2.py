with open("long.txt", "r") as file: 
    result = 0
    line_count = 0
    for line in file: 
        increase = True 
        count = True
        digit = True 
        numbers = []
        current = ""
        line_count += 1
        for i, number in enumerate(line.rstrip()):  
            if i == len(line.rstrip()) -1: 
                current += number
            if (number == " " or i == len(line.rstrip()) -1) and current != "": 
                numbers.append(int(current))
                current = ""
                if len(numbers) == 2: 
                    if numbers[-1] == numbers[-2] or abs(numbers[-1]-numbers[-2]) > 3: 
                        count = False 
                        break
                    elif numbers[-1] < numbers[-2]: 
                        increase = False
                    
                elif len(numbers) > 2: 
                    if (numbers[-1] > numbers[-2] and increase == False) or (numbers[-1] < numbers[-2] and increase) or numbers[-1] == numbers[-2] or abs(numbers[-1]-numbers[-2]) > 3: 
                        count = False 
                        break
                    
            else: 
                current += number 

        if count: 
            result += 1

    print(result) 
        