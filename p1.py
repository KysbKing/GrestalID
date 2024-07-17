import subprocess
from colorama import init, Fore, Style
import os

# Инициализация colorama для поддержки стилей и цветов в терминале
init()

packages = [
    'requests',
    'asyncio',
    'colorama',
    'bs4',
    'uuid',
    'pystyle',
    'whois',
    'phonenumbers',
    'termcolor',
    'telethon',
    'faker',
    'telebot',
    'qrcode',
    'pyfiglet',
    'UserAgent',
    'fake_useragent',
    'telethon'
]

def install_packages(packages):
    print("GrestalID\n")
    print(Fore.YELLOW + Style.BRIGHT + "Установка библиотек..." + Style.RESET_ALL)

    for package in packages:
        try:
            subprocess.check_call(['pip', 'install', package])
            print(Fore.GREEN + f'Successfully installed {package}' + Style.RESET_ALL)
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f'Failed to install {package}: {str(e)}' + Style.RESET_ALL)

    # После установки библиотек запускаем скрипт GrestalID.py
    print("\nЗапуск скрипта GrestalID.py...")
    try:
        subprocess.check_call(['python', 'GrestalID.py'])
        print(Fore.GREEN + "Скрипт GrestalID.py успешно выполнен." + Style.RESET_ALL)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f'Ошибка при выполнении скрипта GrestalID.py: {str(e)}' + Style.RESET_ALL)

if __name__ == "__main__":
    install_packages(packages)
