lst_1 = ["animals","names", "cities", "verbs"]

animals  = "angelfish, dung beetle, beaver, alpaca, orangutan "
names = "Marcus, Ahan, Rosie, Shreya, Yesenia "
cities = "New York, Memphis, Huntington, Houston, Paris "
verbs = "pleasing, requesting, searching, loving, rejecting "

answers_lst = []

import random 
x = random.choice(lst_1)
import time 
start = time.time()

for i in range(1):

    if x == "animals":
        y = input("Your category is animals. Choose between: " + animals)
        answers_lst.append(y)
    elif x == "names":
        z = input("Your category is names. Choose between: "+ names)
        answers_lst.append(z)
    elif x == "cities":
        a = input("Your category is cities. Choose between: "+ cities)
        answers_lst.append(a)
    else:
        b = input("your category is verbs. Choose between: "+ verbs)
        answers_lst.append(b)

for i in range(9):

    if x == "animals":
        c = input("Choose again: " + animals)
        answers_lst.append(c)
    elif x == "names":
        d = input("Choose again: " + names)
        answers_lst.append(d)
    elif x == "cities":
        e = input("Choose again: " + cities)
        answers_lst.append(e)
    else:
        f = input("Choose again: " + verbs)
        answers_lst.append(f)

for x in answers_lst:
    print(x.center(100))

end = time.time() 

print("Your time was ",(end-start))






