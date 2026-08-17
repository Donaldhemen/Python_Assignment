#create a simple multiple choice game
#question 1 what is the capital of Nigeria 
#options: 1. Paris 2. London 3. Abuja 4. Lagos


import random

#
#def generate_question():
#
def quiz_one():
    correct_score = 0
    wrong_score = 0
    
    while(True):
        print("Question 1: What is the capital of Nigeria?")
        print()
        answer = int(input("Options: 1.Paris 2.London 3.Abuja 4.Lagos"))
        if answer == 3 :
            print("correct")
            correct_score += 1
        else :  
            print("Wrong")
            wrong_score += 1
        break

def quiz_two():
    correct_score = 0
    wrong_score = 0
    
    while(True):
        print("Question 2: When did Nigeria gain independence?")
        print()
        answer = int(input("Options: 1.1960 2. 1963 3. 1914 4. 1999"))
        if answer == 1 :
            print("correct")
            correct_score += 1
        else :  
            print("Wrong")
            wrong_score += 1
        break

def quiz_three():
    correct_score = 0
    wrong_score = 0
    
    while(True):
        print("Question 3: What is the capital of Lagos?")
        print()
        answer = int(input("Options: 1. Lagos Island 2. Ikeja 3. Oshodi 4. Agege"))
        if answer == 2 :
            print("correct")
            correct_score += 1
        else :  
            print("Wrong")
            wrong_score += 1
        break

def quiz_four():
    correct_score = 0
    wrong_score = 0
    
    while(True):
        print("Question 4: What is the capital of Lagos?")
        print()
        answer = int(input("Options: 1. Lagos Island 2. Ikeja 3. Oshodi 4. Agege"))
        if answer == 2 :
            print("correct")
            correct_score += 1
        else :  
            print("Wrong")
            wrong_score += 1
        break
        
