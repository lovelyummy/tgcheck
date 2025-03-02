import requests
from bs4 import BeautifulSoup
import time


def check_username_on_fragment(username):
    # URL для проверки username на Fragment
    url = f"https://fragment.com/username/{username}"

    # Заголовки, чтобы имитировать запрос от браузера
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Отправляем GET-запрос
    response = requests.get(url, headers=headers)

    # Проверяем статус ответа
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем информацию о доступности username
        availability = soup.find('div', {'class': 'tm-value'})
        if availability:
            status = availability.text.strip().lower()
            if "available" in status:
                return True  # Username свободен
            else:
                return False  # Username занят
        else:
            print(f"Username @{username}: информация не найдена.")
            return False
    else:
        print(f"Ошибка при запросе: {response.status_code}")
        return False


# Чтение никнеймов из файла
def read_usernames_from_file(filename):
    with open(filename, 'r') as file:
        usernames = file.read().splitlines()
    return usernames


# Сохранение свободных никнеймов в файл
def save_good_usernames(good_usernames, filename):
    with open(filename, 'w') as file:
        for username in good_usernames:
            file.write(f"{username}\n")


# Основная функция
def main():
    input_file = "usernames.txt"  # Файл с никнеймами для проверки
    output_file = "good.txt"  # Файл для сохранения свободных никнеймов
    delay_between_requests = 5  # Задержка между запросами (в секундах)

    # Чтение никнеймов из файла
    usernames = read_usernames_from_file(input_file)
    good_usernames = []

    for username in usernames:
        print(f"Проверка @{username}...")
        if check_username_on_fragment(username):
            print(f"Username @{username} свободен!")
            good_usernames.append(username)
        else:
            print(f"Username @{username} занят.")

        # Задержка между запросами
        time.sleep(delay_between_requests)

    # Сохранение свободных никнеймов в файл
    save_good_usernames(good_usernames, output_file)
    print(f"Свободные никнеймы сохранены в {output_file}.")


# Запуск программы
if __name__ == "__main__":
    main()