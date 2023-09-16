# with open ("database.txt","r")as file:
#     content=file.read()
#     print(content)

# user_input=input("введите словo: ")
# with open("text.txt","a")as file:
#     file.write(user_input)



user_input=input("Введите что то")
pp_input=input("Введите что то")
with open("text.txt","r")as file:
    for line in file:
        stored_username,stored_password=line.strip().split(":")
        if user_input==stored_username and pp_input==stored_password:
            print("Вы успешно вошли в систему")
    else:
        print("------------")
