import csv
import os
import pyfiglet
from colorama import init, Fore, Style
import subprocess

# Инициализируем colorama
init()

def find_user_by_id(user_id):
    # Определяем путь к файлу telegram.csv в той же папке, где находится скрипт
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'telegram.csv')

    try:
        # Открываем файл и читаем данные
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Проходимся по строкам и ищем нужный ID
            for row in csv_reader:
                if row['id'] == user_id:
                    return row['phone'], row['username'], row['first_name'], row['last_name']
        
        # Если ID не найден, возвращаем None
        return None

    except FileNotFoundError:
        print(Fore.RED + "Файл telegram.csv не найден." + Style.RESET_ALL)
        return None

def print_blue_text(text):
    print(Fore.CYAN + text + Style.RESET_ALL)

def print_gradient_banner(text):
    gradient_colors = [
        Fore.LIGHTCYAN_EX, Fore.CYAN, Fore.LIGHTCYAN_EX, Fore.WHITE
    ]
    text_length = len(text)
    segment_length = text_length // (len(gradient_colors) - 1)
    
    for i, char in enumerate(text):
        color_index = min(i // segment_length, len(gradient_colors) - 1)
        print(gradient_colors[color_index] + char, end='')
    print(Style.RESET_ALL)

def show_menu():
    print_blue_text("=== Меню ===")
    print_blue_text("1. WannaCry")
    print_blue_text("2. Anubis")
    print_blue_text("3. TgKill")
    print_blue_text("4. Поиск по ID")
    print_blue_text("5. Узнать ID по US")
    print_blue_text("6. DDOS")
    print_blue_text("7. Port Scanner")
    print_blue_text("8. Генерация Всего")
    print_blue_text("============")

def run_wc_script():
    script_path = os.path.join(os.path.dirname(__file__), 'wc.py')
    subprocess.run(['python', script_path])

def run_anubis_script():
    script_path = os.path.join(os.path.dirname(__file__), 'Anub.py')
    subprocess.run(['python', script_path])

def run_tgkill_script():
    script_path = os.path.join(os.path.dirname(__file__), 'tgkill.py')
    subprocess.run(['python', script_path])

def run_idget1_script():
    script_path = os.path.join(os.path.dirname(__file__), 'idget1.py')
    subprocess.run(['python', script_path])

def run_ddos_script():
    script_path = os.path.join(os.path.dirname(__file__), 'ddos.py')
    subprocess.run(['python', script_path])

def run_portscan_script():
    script_path = os.path.join(os.path.dirname(__file__), 'portscan.py')
    subprocess.run(['python', script_path])

def run_fg_script():
    script_path = os.path.join(os.path.dirname(__file__), 'fg.py')
    subprocess.run(['python', script_path])

def main():
    # Отображаем надпись "GrestalID" с градиентом
    ascii_banner = pyfiglet.figlet_format("GrestalID", font="big")
    print_gradient_banner(ascii_banner)

    while True:
        show_menu()
        choice = input(Fore.CYAN + "Выберите опцию (1, 2, 3, 4, 5, 6, 7, 8) или введите 'exit' для выхода: " + Style.RESET_ALL)
        
        if choice == '1':
            print_blue_text("Запуск WannaCry...")
            run_wc_script()
        
        elif choice == '2':
            print_blue_text("Запуск Anubis...")
            run_anubis_script()
        
        elif choice == '3':
            print_blue_text("Запуск TgKill...")
            run_tgkill_script()
        
        elif choice == '4':
            user_id = input(Fore.CYAN + "Введите ID: " + Style.RESET_ALL)
            user_data = find_user_by_id(user_id)
        
            if user_data:
                phone, username, first_name, last_name = user_data
                print_blue_text(f"Телефон: {phone}")
                print_blue_text(f"Username: {username}")
                print_blue_text(f"Имя: {first_name}")
                print_blue_text(f"Фамилия: {last_name}")
                input(Fore.CYAN + "Нажмите ENTER для выхода в Меню..." + Style.RESET_ALL)
            else:
                print_blue_text("Пользователь с таким ID не найден.")
        
        elif choice == '5':
            print_blue_text("Запуск Узнать ID по US...")
            run_idget1_script()
        
        elif choice == '6':
            print_blue_text("Запуск DDOS...")
            run_ddos_script()
        
        elif choice == '7':
            print_blue_text("Запуск Port Scanner...")
            run_portscan_script()
        
        elif choice == '8':
            print_blue_text("Запуск Генерация Всего...")
            run_fg_script()
        
        elif choice.lower() == 'exit':
            break
        
        else:
            print_blue_text("Неверный выбор. Пожалуйста, выберите 1, 2, 3, 4, 5, 6, 7, 8 или 'exit'.")

if __name__ == "__main__":
    main()
