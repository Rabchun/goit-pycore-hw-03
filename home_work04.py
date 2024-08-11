import datetime

def get_upcoming_birthdays(users):


    today = datetime.date.today()
    next_week = today + datetime.timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime.date(today.year, birthday.month, birthday.day)

        if birthday_this_year < today:
            birthday_this_year = datetime.date(today.year + 1, birthday.month, birthday.day)

        if today <= birthday_this_year <= next_week:

            if birthday_this_year.weekday() >= 5:  # 5 - п'ятниця, 6 - субота
                congratulation_date = birthday_this_year + datetime.timedelta(days=7 - birthday_this_year.weekday())
            else:
                congratulation_date = birthday_this_year
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays