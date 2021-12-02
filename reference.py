import random

password = ""

def caps():

    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
    return randomUpperLetter

def letters():
    randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
    return randomLowerLetter   



def numbers():
    testing = random.randint(0, 9)
    return str(testing)




list = [caps, letters, numbers]

x = 0
sys_random = random.SystemRandom()
while x < 6:
    for y in list:
        password += y()
    random.shuffle(list)
    x += 1

print(password)