import re

def normalize_phone(phone_number):

    phone_number = re.sub(r'\D', '', phone_number)  # Видаляємо всі, крім цифр
    if phone_number.startswith('0'):
        phone_number = f"+38{phone_number[1:]}"
    elif not phone_number.startswith('+'):
        phone_number = f"+38{phone_number}"
    return phone_number