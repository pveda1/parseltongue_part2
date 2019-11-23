x = input("Enter your palindrome: ")

s = '''!()-{}[];:'"\,<>.?@#$%^&*_~'''

x = x.lower()

for y in x:
    if y in s:
        x = x.replace(y, "")

new_lst = x.split()

new = ""

for i in new_lst:
    for char in i:
        new = new + (char)
 
#print(new)

new_str = ""

for t in new:
     new_str = t + new_str

if new  == new_str:
     print("CONGRATS! Your input really IS a palindrome!")
else: 
     print("Sorry, this is not a palindrome :(")






    


