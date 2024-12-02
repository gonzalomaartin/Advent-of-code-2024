def check(numbers, increase): 
    if len(numbers) == 1: 
        return (True, None)
    if increase == None: 
        if numbers[-1] == numbers[-2] or abs(numbers[-1]-numbers[-2]) > 3: 
            return (False, None)
        elif numbers[-1] < numbers[-2]: 
            return (True, False)
        else: 
            return (True, True)
        
    else: 
        if (numbers[-1] > numbers[-2] and increase == False) or (numbers[-1] < numbers[-2] and increase) or numbers[-1] == numbers[-2] or abs(numbers[-1]-numbers[-2]) > 3: 
            return (False, None)
        else: 
            return (True, None)


with open("long.txt", "r") as file: 
    result = 0
    line_count = 0
    for line in file: 
        increase = None
        count = True
        extra_life = True
        other_path = []
        numbers = []
        current = ""
        bool_numbers = True 
        bool_other_path = False
        increase_other_path = None
        for i, number in enumerate(line.rstrip()):  
            if i == len(line.rstrip()) -1: 
                current += number
            if (number == " " or i == len(line.rstrip()) -1) and current != "": 
                numbers.append(int(current))
                current = ""
                if bool_numbers: 
                    sol = check(numbers, increase)
                    if sol[0]: 
                        if increase == None:
                            increase =  sol[1]
                    elif extra_life: 
                        extra_life = False
                        other_path = numbers.copy()
                        other_path.pop(-2)
                        numbers.pop(-1)
                        if len(other_path) == 2: 
                            bool_other_path, increase_other_path = check(numbers, None)

                        else: 
                            bool_other_path = check(numbers, increase)[0]
                            increase_other_path = increase
                    else: 
                        bool_numbers = False

                if bool_other_path: 
                    if not check(numbers, increase_other_path)[0]: 
                        bool_other_path = False
                    
            else: 
                current += number 

        if bool_numbers or bool_other_path: 
            result += 1

    print(result) 

#Solution: have two arrays one the usual one and another one with the additional route (same but without the last element) and create a function that will check if the new element makes the array valid 
#When an invalid element comes, skip it one array and in the other remove the last element and call check, for the next elements added call check (create a boolean to know to call check on the 
#additional route array), if another invalid element comes on both arrays return false (sol-> numbers or additional route). Note that if check returns false on when an additional route is created
#we should stop adding elements and calling check on that array as it is a dead branch of a tree. If check is called on a new path of length 2, increase should be passed as None 