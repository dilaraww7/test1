import random
user_choice=input("enter your choice").lower()
choices=["камень ","ножницы ","бумага"]
bot_choices=random.choice(choices)
# print(bot_choices)
# print(user_choice)
if user_choice==bot_choices:
    print("ничья")
elif (user_choice=="камень" and bot_choices=="бумага") or\
    (user_choice=="бумага" and bot_choices=="ножницы") or\
    (user_choice=="ножницы" and bot_choices=="камень"):
    print("бот выиграл")
else:
    print("вы выиграли")