lst_1 = [False, True, True, None, True, None, None, False, False, None, True, False]
lst_2 = ["or","or", "or","==","!=","==","and","==","!=","and","==","or"]
lst_3 = [False, False, None, None, True, True, False, True, None, False, True, None]
lst_4 = [0,1,2,3,4,5,6,7,8,9,10,11]

#for i in range(10):
for x in lst_4:
    a = lst_1[x]
    b = lst_2[x]
    c = lst_3[x]
    d = str(a) + " " + b + " " + str(c)
    print(eval(d))



