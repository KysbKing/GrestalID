import subprocess
from telethon.sync import TelegramClient
from colorama import init, Fore, Back, Style

# Инициализация colorama для поддержки ANSI цветов в Windows
init()

# Форматирование огромного баннера USERTOID с использованием ASCII-арт и цветов
banner_text = r"""
██████╗ ██╗   ██╗███████╗███╗   ███╗
██╔══██╗╚██╗ ██╔╝██╔════╝████╗ ████║
██████╔╝ ╚████╔╝ █████╗  ██╔████╔██║
██╔══██╗  ╚██╔╝  ██╔══╝  ██║╚██╔╝██║
██║  ██║   ██║   ███████╗██║ ╚═╝ ██║
╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝     ╚═╝
"""

formatted_banner = (
    Back.CYAN + Fore.BLUE + Style.BRIGHT +
    f"{banner_text}" +
    Style.RESET_ALL
)

api_id = '23711985'  # Замените на свой API ID
api_hash = 'ee6d68d9069b9be23de8f7b32701734b'  # Замените на свой API Hash

def get_telegram_id(username):
    try:
        with TelegramClient('session_name', api_id, api_hash) as client:
            user = client.get_entity(username)
            return user.id
    except PhoneNumberInvalidError:
        print(f"{Fore.BLUE}Ошибка: Неверный номер телефона. Проверьте настройки API.{Style.RESET_ALL}")
    except ValueError as e:
        print(f"{Fore.BLUE}Ошибка: {e}{Style.RESET_ALL}")
    return None

if __name__ == "__main__":
    print(formatted_banner)  # Вывод огромного баннера USERTOID
    print(f"{Fore.BLUE}RYEM by GrestalID{Style.RESET_ALL}")  # Вывод информации о создателе
    
    while True:
        username = input(f"{Fore.BLUE}Введите username пользователя Telegram (для выхода введите 'exit'): {Style.RESET_ALL}")
        if username.lower() == 'exit':
            subprocess.run(['python', 'GrestalID.py'])
            break
        telegram_id = get_telegram_id(username)
        if telegram_id:
            print(f"{Fore.BLUE}ID пользователя {username} в Telegram: {telegram_id}{Style.RESET_ALL}")
        else:
            print(f"{Fore.BLUE}Не удалось получить ID пользователя. Проверьте корректность username.{Style.RESET_ALL}")