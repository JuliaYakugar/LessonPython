import open_base

def search(arg):
    employees = open_base.read_csv()
    search_arg = input('Введите параметр поиска: ')

    res = []
    for employee in employees:
        if employee[arg] == search_arg:
            res.append(f"{employee['id']}, {employee['last_name']}, {employee['first_name']}, {employee['position']}, {employee['phone_number']}, {employee['salary']}")
    return res

def salary_search():
    employees = open_base.read_csv()
    x1 = float(input('Введите начало диапазона зп: '))
    x2 = float(input('Введите конец диапазона зп: '))

    res = []
    for employee in employees:
        if x1 <= employee['salary'] <= x2:
            res.append(f"{employee['id']}, {employee['last_name']}, {employee['first_name']}, {employee['position']}, {employee['phone_number']}, {employee['salary']}")
    return res

def add_employee():
    employees = open_base.read_csv()
    fam = input('Фамилия: ')
    name = input('Имя/Отчество: ')
    job_title = input('должность: ')
    num = input('Телефон: ')
    other = float(input('Зарплата: '))

    open_base.write_csv(f'{len(employees) + 1 },{fam},{name},{job_title},{num},{other}\n')

def del_employee():
    employees = open_base.read_csv()
    employee = int(input('Введите ID сотрудника для удаления: '))

    for emp in employees:
        if emp['id'] == employee:
            employees.remove(emp)
            open_base.new_csv(employees)

def new_employee():
    employees = open_base.read_csv()
    employee = int(input('Введите ID сотрудника для изменения: '))

    for emp in employees:
        if emp['id'] == employee:
            emp["last_name"] = input(f'{emp["last_name"]} -> ')
            emp["first_name"] = input(f'{emp["first_name"]} -> ')
            emp["position"] = input(f'{emp["position"]} -> ')
            emp["phone_number"] = input(f'{emp["phone_number"]} -> ')
            emp["salary"] = float(input(f'{emp["salary"]} -> '))

            open_base.new_csv(employees)

def exp_json():
    employees = open_base.read_csv()
    open_base.write_json(employees)

def open_json():
    employees = open_base.read_json()
    for emp in employees:
        print(emp)