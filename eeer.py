# def printNumber(n):
#     for i in range(1,10):
#         print(f'{n} x {i} = {n*i}')
# printNumber(5)

# def number(n1, n2):
#     formula = n1*n2
#     # print(f'{n1} x {n2}={n1*n2}')
#     return number
# result = number(3,4)
# print(result)

# res = 12
# my_number=12
# def formula(n):
#     print(res)
#     sum2 = n-my_number**2
# formula(12)

# phone_book={}
# phone_book["Medina"]=["17 years","cooking","+87786779034"]
# phone_book["Arlan"]=["12 years","dancing","+87022344405"]
# print(phone_book["Medina"])
# print(phone_book["Arlan"][1])

#To-do List
to_do_list={}
def add_task(day,task):
    if not day in to_do_list:
        to_do_list[day]=[ ]
        to_do_list[day].append(task)
        print("Вы успешно добавили задачу")
        return 
def main():
    user_input=input("Выберите опцию: ")
    while True:
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Посмотреть задачи на день")
        print("4. Посмотреть задачи на неделю")
        user_input=input("Выберите опцию: ")
        if user_input=="1":
            day=input("Введите день: ")
            task=input("Введите задачу: ")
            add_task(day, task)
        if user_input=="5":
            break
        if user_input=="3":
            print(to_do_list)
main()