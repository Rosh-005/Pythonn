import random
while true:
    print("choose any \n 1.rock \n 2.paper \n 3.scissor")
    a=int(input("user choice:"))
    while a>10:
        a=int(input("enter valid ones:")
              if(a==1)
              value='rock'
              else if(a==2):
              value='paper'
              elif(a==3):
              value='scissor'
              print("user's choice is:" +value)
              print("\nNow its computer turn.......") 
  
 
    comp_choice = random.randint(1, 3) 
      
 
    while comp_choice == choice: 
        comp_choice = random.randint(1, 3) 
  
     
    if comp_choice == 1: 
        comp_choice_name = 'Rock'
    elif comp_choice == 2: 
        comp_choice_name = 'paper'
    else: 
        comp_choice_name = 'scissor'
          
    print("Computer choice is: " + comp_choice_name) 
  
    print(choice_name + " V/s " + comp_choice_name) 
  
     
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )): 
        print("paper wins => ", end = "") 
        result = "paper"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        print("Rock wins =>", end = "") 
        result = "Rock"
    else: 
        print("scissor wins =>", end = "") 
        result = "scissor"
  
     
    if result == choice_name: 
        print("<== User wins ==>") 
    else: 
        print("<== Computer wins ==>") 
          
    print("Do you want to play again? (Y/N)") 
    ans = input() 
  
  
     
    if ans == 'n' or ans == 'N': 
        break
      
print("\nThanks for playing") 
        
              
    
    
