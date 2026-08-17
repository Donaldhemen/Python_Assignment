
def multiplication_quiz():
    number_one = random.randrange(1, 9)
    number_two = random.randrange(1, 9)

    pass_remark_one = "Very good!"
    pass_remark_two = "Nice work!"
    pass_remark_three = "Keep up the good work!"
    
    fail_remark_one = "No. Please try again."
    fail_remark_two = "Wrong. Try once more."
    fail_remark_three = "No. Keep trying."
    
    while True:
        answer = int(input(f"How much is {number_one} * {number_two}?: "))
        
        randnumber = random.randrange(1, 3)

        if answer == number_one * number_two:
            if randnumber == 1:
                print(pass_remark_one)
            elif randnumber == 2:
                print(pass_remark_two)
            elif randnumber == 3:
                print(pass_remark_three)
#            break
        elif answer != number_one * number_two:
            if randnumber == 1:
                print(fail_remark_one)
            elif randnumber == 2:
                print(fail_remark_two)
            elif randnumber == 3:
                print(fail_remark_three)
                
def addition_quiz():
    number_one = random.randrange(1, 9)
    number_two = random.randrange(1, 9)

    pass_remark_one = "Very good!"
    pass_remark_two = "Nice work!"
    pass_remark_three = "Keep up the good work!"
    
    fail_remark_one = "No. Please try again."
    fail_remark_two = "Wrong. Try once more."
    fail_remark_three = "No. Keep trying."
    
    while True:
        answer = int(input(f"How much is {number_one} + {number_two}?: "))
        
        randnumber = random.randrange(1, 3)

        if answer == number_one + number_two:
            if randnumber == 1:
                print(pass_remark_one)
            elif randnumber == 2:
                print(pass_remark_two)
            elif randnumber == 3:
                print(pass_remark_three)
#            break
        elif answer != number_one + number_two:
            if randnumber == 1:
                print(fail_remark_one)
            elif randnumber == 2:
                print(fail_remark_two)
            elif randnumber == 3:
                print(fail_remark_three)
                
def subtraction_quiz():
    number_one = random.randrange(1, 9)
    number_two = random.randrange(1, 9)

    pass_remark_one = "Very good!"
    pass_remark_two = "Nice work!"
    pass_remark_three = "Keep up the good work!"
    
    fail_remark_one = "No. Please try again."
    fail_remark_two = "Wrong. Try once more."
    fail_remark_three = "No. Keep trying."
    
    while True:
        answer = int(input(f"How much is {number_one} - {number_two}?: "))
        
        randnumber = random.randrange(1, 3)

        if answer == number_one - number_two:
            if randnumber == 1:
                print(pass_remark_one)
            elif randnumber == 2:
                print(pass_remark_two)
            elif randnumber == 3:
                print(pass_remark_three)
#            break
        elif answer != number_one - number_two:
            if randnumber == 1:
                print(fail_remark_one)
            elif randnumber == 2:
                print(fail_remark_two)
            elif randnumber == 3:
                print(fail_remark_three)
                
def division_quiz():
    number_one = random.randrange(1, 9)
    number_two = random.randrange(1, 9)

    pass_remark_one = "Very good!"
    pass_remark_two = "Nice work!"
    pass_remark_three = "Keep up the good work!"
    
    fail_remark_one = "No. Please try again."
    fail_remark_two = "Wrong. Try once more."
    fail_remark_three = "No. Keep trying."
    
    while True:
        answer = int(input(f"How much is {number_one} / {number_two}?: "))
        
        randnumber = random.randrange(1, 3)

        if answer == number_one / number_two:
            if randnumber == 1:
                print(pass_remark_one)
            elif randnumber == 2:
                print(pass_remark_two)
            elif randnumber == 3:
                print(pass_remark_three)
#            break
        elif answer != number_one / number_two:
            if randnumber == 1:
                print(fail_remark_one)
            elif randnumber == 2:
                print(fail_remark_two)
            elif randnumber == 3:
                print(fail_remark_three)
                
def 
