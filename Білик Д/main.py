project_tasks={
    "Task1":{
        "назва" : "Аналіз конкурентів",
        "пріоритет" : "4/5",
        "виконавець" : "Наталія (BA)",
        "статус" : "В процесі роботи",},
    "Task2":{
        "назва" : "Дизайн інтерфейсу",
        "пріоритет" : "3/5",
        "виконавець" : "Ольга (Дизайнер)",
        "статус" : "На етапі завершення"},
    "Task3":{
        "назва" : "Тестування",
        "пріоритет" : "5/5",
        "виконавець" : "Максим (QA)",
        "статус" : "Етап старту"},
}
def display():
    for key, value in project_tasks.items():
        print(f"[{key}] | Назва: {value["назва"]} ; Статус: {value["статус"]} ; Виконавець: {value["виконавець"]} ; Пріоритет: {value["пріоритет"]} \n")
    return project_tasks

def update():
    key = input("Введіть ID значення(Task1/2/3), яке бажаєте змінити:")
    if key not in project_tasks:
        print("Помилка!")
    task = input("Введіть назву поля для зміни (назва/пріоритет/виконавець/статус):")
    if task in project_tasks[key]:
        new_value = input(f"Введіть нове значення для {task}")
        old_value = project_tasks[key][task]
        project_tasks[key][task] = new_value
        print(f"Поле {task} оновлено з {old_value} на {new_value}")
    else:
        print("Помилка!")
    return project_tasks

def add():
    new_id = input("Введіть ID нового завдання: ")
    new_name = input("Введіть назву завдання: ")
    new_priority = input("Введіть пріоритет (наприклад, 2/5): ")
    new_executor = input("Введіть виконавця: ")
    new_status = input("Введіть початковий статус: ")
    project_tasks[new_id] = {
        "назва": new_name,
        "пріоритет": new_priority,
        "виконавець": new_executor,
        "статус": new_status
    }
    return project_tasks
def delete():
    task_id=input("Введіть  завдання, яке бажаєте видалити (Task1/2/3): ")
    if task_id not in project_tasks:
        print ("Помилка!")
        return project_tasks
    delete_task = project_tasks.pop(task_id)
    print(f"Завдання {task_id} ({delete_task["назва"]}) успішно видалено")
    return project_tasks
action = input("Введіть дію яку бажаєте виконати у консоль: (вивести/замінити/додати/видалити)\n")
match action:
    case "вивести":
        result = display()
    case "замінити":
        result = update()
    case "додати":
        result= add()
    case "видалити":
        result= delete()
    case _:
        print("Введіть коректну дію")
