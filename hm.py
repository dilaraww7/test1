import random
import string
az=string.ascii_letters
nb=random.randint(0,9)
x=input("Введите уровень сложности: ")
# y=["easy, medium, hard"]
z=["@","#","%","^",".","/",]
password=""
if x==("easy"):
    for i in range(0,5):
        password+=str(random.randint(0,9))+random.choice(az)+random.choice(z)
elif x==("medium"):
    for i in range(0,10):
        password+=str(random.randint(0,9))+random.choice(az)+random.choice(z)
elif x==("hard"):
    for i in range(0,15):
        password+=str(random.randint(0,9))+random.choice(az)+random.choice(z)   
print(password)