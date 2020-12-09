import telegram
import os
from dotenv import load_dotenv 
load_dotenv()

TELEGRAM_TOKEN = os.getenv('telegram_token')  # добавить токен

CHAT_ID = os.getenv('chat_id')  # добавить id пользователя


proxy = telegram.utils.request.Request(proxy_url='socks5://195.144.21.185:1080') # Получаем адрес прокси на http://spys.one/proxies/ 
bot = telegram.Bot(token=TELEGRAM_TOKEN, request=proxy) # Если прокси не требуется, удаляем request из аргумента

def send_message(message):

	return bot.send_message(chat_id=CHAT_ID, text=message)


send_message(f"Helo World!")

