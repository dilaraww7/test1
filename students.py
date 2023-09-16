students={}
def add_students(name):
    if not name in students:
        students[name]=[]
        print("Вы успешно добавили студента в список")
        return
def show_students():
    if not students:
        print("Список пуст")
    else:
        print("")
        for name, grades in students.items():
            print(f'оценка {name}')
            for grade in grades:
                print(grade)
            print("-------------------")
def add_grades(name,grade):
    students[name].append(grade)
    print("Вы успешно добавили оценку")
def remove_students(students,name):
    del students[name]
    print("Вы успешно удалили студента из списка")
def main():
    while True:
        print("0. Выход")
        print("1. Добавить студента")
        print("2. Посмотреть список студентов")
        print("3. Удалить студента")
        print("4. Добавить оценки студента")
        user_input=input("Выберите опцию: ")
        if user_input=="1":
            name=input("Введите имя: ")
            add_students(name)
        if user_input=="2":
            show_students()
        if user_input=="3":
            name=input("Введите имя студента которое хотите удалить")
            remove_students(students,name)
        if user_input=="4":
            name = input("Введите имя студента")
            grade =input("Введите оценку студента")
            add_grades(name, grade)
            print(students)
        if user_input=="0":
            break   
main()