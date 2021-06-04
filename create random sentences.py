# Will create 10 random sentences using the 3 available lists

name = ["Andreia", "Bruna", "Carolina", "Dionision"]
verb = ["buys", "rides", "kicks", "slaps"]
noun = ["lion", "bicycle", "plane", "clown", "soup"]

from random import randint
def pick(words):
    num_words =len(words)
    num_picked=randint(0, num_words -1)
    word_picked=words[num_picked]
    return word_picked
sentences=0
while sentences < 10:
    print(pick(name), pick(verb), "a", pick(noun), end=".\n")
    sentences=sentences+1
    