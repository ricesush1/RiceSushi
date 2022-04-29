def main():
  list = [0,0,0] #used to track user progress

  Q1 = int(input("How much sleep, in hours, do you get per day?")) #first question
  if Q1 in range(7,9):
    list[0]=1 #keeps tally of how good user is doing
  print("next question!")
  Q2 = int(input("How much time, in hours, do you work or study per day")) #question 2
  if Q2 in range(2,4):
    list[1]=1
  print("next question!")
  
  Q3 = int(input("How many hours of free time do you give yourself per day?")) #question 3
  if Q3 in range(2,4):
    list[2]=1
  print("here are your results:")
  
  if (list[0]) == 1: #provides final results
    print("your sleep is good!")
  else:
    print("your sleep schedule needs to be improved")
    
  if (list[1]) == 1:
    print("you are managing your work well!")
  else:
    print("try to balance how much you work!")
    
  if (list[2]) == 1:
    print("You are giving yourself enough free time")
  else:
    print("you need to balance your free time better!")

print("take this quiz to see if you are using your time well!") #tells user what the program does
while True: #makes sure the user provides a valid input
  answer = input("Start the quiz? (Y/N)")
  if(answer == "Y" or answer == "y"):
    main();
    break
    
  elif(answer == "N" or answer == "n"):
    print("OK, goodbye!")
    break;
    
  else:
    print("Please enter Y/N") #reprompts the user to provide a valid input
    