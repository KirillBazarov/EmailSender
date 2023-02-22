import csv
import re
from typing import List


def is_valid_email(email: str) -> bool:
    """
        Функция проверяет, является ли переданный email корректным по формату.

        Args:
            email (str): Email для проверки.

        Returns:
            bool: True, если email корректен, иначе False.
        """
    # Проверяем корректность email с помощью регулярного выражения
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        return False


def add_emails_to_csv(emails: List[str]) -> None:
    """
       Функция добавляет подходящие email из переданного списка в csv файл,
       игнорируя дубликаты.

       Args:
           emails (List[str]): Список email для добавления в csv файл.

       Returns:
           None
       """
    valid_emails = []
    invalid_emails = []
    # Считываем все email из csv файла
    with open("emails.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        existing_emails = [row[0] for row in reader]

    for email in emails:
        if email in existing_emails:
            print("-" * 20)
            print(f"Email {email} уже существует в файле.")
            continue

        if is_valid_email(email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)

    # Добавляем только подходящие email в csv файл
    with open("emails.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for email in valid_emails:
            writer.writerow([email])

    # Выводим список неподходящих email
    if invalid_emails:
        for email in invalid_emails:
            print("!" * 20)
            print(f"Неподходящие email:{email}")
    print("-" * 20)
    print(f"Программа закончена. Было внесено {len(valid_emails)} email")


def remove_emails_from_csv(emails: List[str]) -> None:
    """
    Функция удаляет email из csv файла, если он существует в файле.

    Args:
        emails (List[str]): Список email для удаления из csv файла.

    Returns:
        None
    """
    # Считываем все email из csv файла
    with open("emails.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        existing_emails = [row[0] for row in reader]

    # Создаем новый csv файл, исключая удаляемые email
    with open("emails.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for email in existing_emails:
            if email not in emails:
                writer.writerow([email])


remove_emails_from_csv(['xfsafasfasdfasdf@gmail.com',"xfsafas@gmail.com"])
