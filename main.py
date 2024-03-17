from random import randint

pc_choice = randint(1,50)
keep_play = True

while keep_play:
    user_choice = int(input("Guess right number! range is 1 to 50 : "))
    if user_choice == pc_choice:
          print("Congrat Your are winner!")
          keep_play = False
    elif user_choice < pc_choice:
         print("It's Higher")
    elif user_choice > pc_choice:
        print("It's Lower")
          
        