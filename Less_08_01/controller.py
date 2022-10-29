import model
import view

def button_click():
    value = view.show_menu()

    if value == 1:
        view.print_result(model.search('last_name'))
    if value == 2:
        view.print_result(model.search('position'))
    if value == 3:
        view.print_result(model.salary_search())
    if value == 4:
        model.add_employee()
    if value == 5:
        model.del_employee()
    if value == 6:
        model.new_employee()
    if value == 7:
        model.exp_json()
    if value == 8:
        model.open_json()
    if value != 9:
        button_click()
    if value == 9:
        print("Работа завершена")