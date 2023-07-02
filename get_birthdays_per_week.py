from datetime import datetime, timedelta
from copy import deepcopy
from collections import defaultdict


def get_birthdays_per_week(users: list) -> None:
    """
    Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.
    Функція виводить користувачів з днями народження на тиждень вперед від поточного дня.
    Тиждень починається з понеділка.

    :param users: list
    :return: None
    """

    users = deepcopy(users)
    filtered_users = []
    days_of_week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
    today = datetime.today()
    current_year = datetime.today().year
    current_month = datetime.today().month
    current_weekday = datetime.today().weekday() + 1
    for user in users:
        if current_month <= user["birthday"].month <= current_month + 1:
            user["birthday"] = user["birthday"].replace(year=current_year)
            filtered_users.append(user)

    delta = 6 - current_weekday
    nearest_saturday = datetime(year=today.year, month=today.month, day=today.day) + timedelta(days=delta)
    next_saturday = nearest_saturday + timedelta(days=7)

    dict_to_print = defaultdict(list)
    for user in filtered_users:
        if nearest_saturday <= user["birthday"] < next_saturday:
            key = user["birthday"].weekday() + 1
            dict_to_print.setdefault(key, []).append(user["name"])

    dict_to_print[1].extend(dict_to_print.get(6, []))
    dict_to_print[1].extend(dict_to_print.get(7, []))

    for key in range(1, 6):
        if key in dict_to_print:
            if len(dict_to_print.get(key)) != 0:
                print(f"{days_of_week[key]}:", end=" ")
                print(*dict_to_print.get(key), sep=", ")


def main():
    collegues = [{"name": "Bill", "birthday": datetime(year=1979, month=7, day=5)},
                 {"name": "Jimmy", "birthday": datetime(year=1985, month=6, day=30)},
                 {"name": "Carol", "birthday": datetime(year=2023, month=7, day=4)},
                 {"name": "Will", "birthday": datetime(year=2023, month=7, day=6)},
                 {"name": "Mark", "birthday": datetime(year=1977, month=11, day=27)},
                 {"name": "Michael", "birthday": datetime(year=1979, month=7, day=4)},
                 {"name": "Sara", "birthday": datetime(year=1979, month=7, day=8)}
                 ]
    get_birthdays_per_week(collegues)


if __name__ == "__main__":
    main()
