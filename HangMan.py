word="mubin"
chances=len(word)
guesses=[]
done=False

while(not done):
    guess=str(input(f"{chances} Remaining , Enter the char : "))
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        chances-=1
        if chances==0:
            print("Better Luck For Next Time")
            break
    done =True

    for letter in word.lower():
        if letter.lower() not in guesses:
            done=False

    for letter in word.lower():
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_",end=" ")
    print("")