from instagram_private_api import Client, ClientCompatPatch, ClientError, ClientCheckpointRequiredError
import time
from colorama import Fore, init
import os
import getpass

os.system("clear")
init(autoreset=True)

print(Fore.RED + " \t\t  ___     ___    _____   _____   _  _     ___     ___    _  __ ")
print(Fore.RED + " \t\t | _ \   | __|  |_   _| |_   _| | || |   /   \   / __|  | |/ / ")
print(Fore.RED + " \t\t |   /   | _|     | |     | |   | __ |   | - |  | (__   | ' <")
print(Fore.RED + " \t\t |_|_\   |___|   _|_|_   _|_|_  |_||_|   |_|_|   \___|  |_|\_\ \n")
print(Fore.YELLOW + "\t\t\tVersion 1.1\t\t\tinsta: @retthack\n\n")

username = input(Fore.BLUE + 'kullanici adini gir: ')
password = getpass.getpass(Fore.BLUE + 'sifreni gir:')

try:
    api = Client(username, password)
    following = api.user_following(api.authenticated_user_id, api.generate_uuid())

    os.system("clear")
    for user in following['users']:
        print(f'Takipten çıkarılıyor: {user["username"]}')
        api.friendships_destroy(user['pk'])
        time.sleep(0.1)

    print("Tüm takipler başarıyla kaldırıldı.")
except ClientCheckpointRequiredError:
    print(Fore.RED + "Checkpoint doğrulaması gerekiyor. Tarayıcıdan giriş yaparak doğrulama işlemini tamamlayın.")
except ClientError as e:
    print(Fore.RED + f"Diğer bir hata oluştu: {str(e)}")







