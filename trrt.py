# for digit in range(23):
#     print(digit)
# import time
# timer=int(input("введите секунды"))
# for i in range(100,timer,-5):
#     print(i)
#     time.sleep(1)
# for i in range(100):
#     if i%2==0:
#        print(i)
# sum=0
# x=int(input(""))
# for i in range(x):
#     print(sum)
#     sum=sum+i
# x=100
# while True:
#     print(x)
# import random
# x=random.randint(1,10)
# print(x)
import random
answer= "yes"
sum=0
while answer=="yes":
    x=random.randint(1,6)
    if x==1:
        print("[     ]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[     ]")
    elif x==2:
        print("[     ]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[     ]")
    elif x==3:
        print("[     ]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[     ]")
    elif x==4:
        print("[     ]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[     ]")
    elif x==5:
        print("[     ]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[     ]")
    else:
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
    answer=input("enter yes to try again: ")
    sum+=x
print(sum)
