import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols=['!','"','#','$','%','{','|','}','~','@','^','&','*','+','(',')','_','/','?']
numbers=['0','1','2','3','4','5','6','7','8','9']
n_letters=int(input("Enter no of letters u need in password:"))
n_symbols=int(input("Enter no of symbols u need in password:"))
n_numbers=int(input("Enter no of numbers u need in password:"))
passwordlist=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    passwordlist+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    passwordlist+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    passwordlist+=char    
random.shuffle(passwordlist)
password=""         
for i in passwordlist:
    password+=i
print(password)    
