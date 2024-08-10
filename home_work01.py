import datetime

def get_days_from_today(date):

    try:
        given_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        today = datetime.datetime.today()
        return (given_date - today).days
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'")
        return None