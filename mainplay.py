def play(): 
    
    p1name = input("player 1, Please enter your name :") 
    print ("JUST-A check i heared - ", p1name )
    p2name = input("Player 2 , Please enter your name: ") 
    print ("Yes I know U wanna defeat "+p1name+" U r "+ p2name )
  
    # variable for counting score. 
    pp1 = 0
    pp2 = 0
  
    # variable for counting turn 
    turn = 0
  
    # keep looping 
    while True: 
  
        # choose() function calling 
        picked_word = choose() 
  
        # jumble() fucntion calling 
        qn = jumble(picked_word) 
        print("jumbled word is :", qn) 
  
        # checking turn is odd or even 
        if turn % 2 == 0: 
  
            # if turn no. is even 
            # player1 turn 
            print(p1name, 'Your Turn.') 
  
            ans = input("what is in your mind? ") 
  
            # checking ans is equal to picked_word or not 
            if ans == picked_word: 
  
                # incremented by 1 
                pp1 += 1
  
                print('Your score is :', pp1) 
                turn += 1
  
            else: 
                print("Better luck next time ..") 
  
                # player 2 turn 
                print(p2name, 'Your turn.') 
  
                ans = input('what is in your mind? ') 
  
                if ans == picked_word: 
                    pp2 += 1
                    print("Your Score is :", pp2) 
  
                else: 
                    print("Better luck next time...correct word is :", picked_word) 
  
                c = int(input("press 1 to continue and 0 to quit :")) 
  
                # checking the c is equal to 0 or not 
                # if c is equal to 0 then break out 
                # of the while loop o/w keep looping. 
                if c == 0: 
                    # thank() function calling 
                    thank(p1name, p2name, pp1, pp2) 
                    break
  
        else: 
  
            # if turn no. is odd 
            # player2 turn 
            print(p2name, 'Your turn.') 
            ans = input('what is in your mind? ') 
  
            if ans == picked_word: 
                pp2 += 1
                print("Your Score is :", pp2) 
                turn += 1
  
            else: 
                print("Better luck next time.. :") 
                print(p1name, 'Your turn.') 
                ans = input('what is in your mind? ') 
                if ans == picked_word: 
                    pp1 += 1
                    print("Your Score is :", pp1) 
  
                else: 
                    print("Better luck next time...correct word is :", picked_word) 
  
                    c = int(input("press 1 to continue and 0 to quit :")) 
  
                    if c == 0: 
                        # thank() function calling 
                        thank(p1name, p2name, pp1, pp2) 
                        break
  
            c = int(input("press 1 to continue and 0 to quit :")) 
            if c == 0: 
                # thank() function calling 
                thank(p1name, p2name, pp1, pp2) 
                break
  
  
# Driver code 
if __name__ == '__main__': 
      
    # play() function calling 
    play() 
