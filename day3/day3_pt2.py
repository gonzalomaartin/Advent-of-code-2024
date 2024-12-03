import re 
with open("long.txt", "r") as file: 
    result = 0
    numbers = []
    conditions = []
    do = True 
    for line in file:
        numbers = re.finditer(r"mul\((\d+),(\d+)\)", line)
        conditions = re.finditer(r"(don't|do)\(\)", line)
        conditions_list = [(x.group(0), x.start()) for x in conditions]
        index = 0
        for number in numbers: 
            while index < len(conditions_list) and conditions_list[index][1] < number.start(): 
                if conditions_list[index][0] == "don't()": 
                    do = False
                else: 
                    do = True
                index += 1
            
            if do: 
                result += int(number.group(1))*int(number.group(2))

    print(result)

