# Will ask for the answers to the 5 times table. Write stop to stop it.


n = 5
for i in range (1,13):
    print("What's", i, "X", n, "?")
    guess = input ()
    if guess == "stop":
        break
    ans = i * n
    if int(guess) == ans:
        print("Correct!")
    else:
        print("No, it's", ans)
print("Finished")


