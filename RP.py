print("GENERATING RANDOM 'N' NUMBER OF PASSWORDS WITH LENGTH DEPENDING ON USER REQUIREMENT")

print("WELCOME")

import random
import string

#the shuffle function -created for shuffling the password,
def shuffle(strings):
    templist = list(strings)
    random.shuffle(templist)
    return templist
amount=int(input("How many passwords you require?:"))
passwordlength = int(input("Enter the length of password you require?:"))

print(f"Generated passwords==>")
print("*********************")

for amt in range(amount):
    passwds =''.join(random.sample(string.ascii_letters + string.digits+string.punctuation,k=passwordlength))
#calling the shuffle function to shuffle the password
    password = shuffle(passwds)
#The Shuffled password will be a list, now converting list to string with 'join' function
    Random_password = ''.join(password)
    print(f"{Random_password}")
#loop continues
    amount += 1


print("Thank you")



