#Jason Fyrberg

import string
import random

#determines length of password
def define_length(a,b):
    pw_length = random.randint(a,b)
    return pw_length

# get lists of random characters
list1 = list(string.ascii_lowercase)
list2 = list(string.ascii_uppercase)
list3 = list(string.digits)
list4 = list(string.punctuation)

# shuffle lists 
random.shuffle(list1)
random.shuffle(list2)
random.shuffle(list3)
random.shuffle(list4)

# get a password ranging from 9-18 characters, and make it 80% letters and 20% numbers
pw_length = define_length(9,18)
first_half = round(pw_length * (40/100))
second_half = round(pw_length * (10/100))

result = []

for x in range(first_half):
    result.append(list1[x])
    result.append(list2[x])

for x in range(second_half):
    result.append(list3[x])
    result.append(list4[x])


#shuffle characters
random.shuffle(result)

#join characters and output password
complete_password = "".join(result)
print("Your generated password is:", complete_password)

