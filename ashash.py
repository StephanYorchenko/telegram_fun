from telethon import TelegramClient
from telethon.tl.types import DocumentAttributeAudio
import mimetypes
import time

entity = '' #имя сессии - все равно какое
api_id = '1495679'
api_hash = '499e87ee61533a91dc4217d1b16360b4'
phone = '+79012010744'
client = TelegramClient(entity, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    # client.send_code_request(phone) #при первом запуске - раскомментить, после авторизации для избежания FloodWait советую закомментить
    client.sign_in(phone, input('Enter code: '))
client.start()
user_name = '@shaikhullin_aidar'

def blink(user_name, text):
    #for i in text:
        #if i != ' ':
            #client.loop.run_until_complete(client.send_message(user_name, i))
    message = client.loop.run_until_complete(client.send_message(user_name, text))
    for i in range(1000):
        for j in range(len(text)):
            new_text = text[:j]+text[j].upper()+text[j+1:] 
            print(new_text)
            client.loop.run_until_complete(client.edit_message(message, new_text))
            time.sleep(1)
    client.disconnect()
    return 0

def appear(user_name, text):
    spl = text.split()
    mes = spl[0]
    message = client.loop.run_until_complete(client.send_message(user_name, mes))
    for i in range(1, len(spl)):
        mes += ' ' + spl[i]
        client.loop.run_until_complete(client.edit_message(message, mes))
        time.sleep(10)
    client.disconnect()

def spam(user_name, text, count=10, c=1):
    for i in range(int(count)):
        time.sleep(int(c))
        client.loop.run_until_complete(client.send_message(user_name, text))
    client.disconnect()

def blink_word(user_name, text):
    message = client.loop.run_until_complete(client.send_message(user_name, text))
    for i in range(1000):
        for j in range(len(text)):
            new_text = text.upper()
            client.loop.run_until_complete(client.edit_message(message, new_text))
            time.sleep(1)
            client.loop.run_until_complete(client.edit_message(message, text))
            time.sleep(1)

    client.disconnect()
    return 0


if __name__ == '__main__':
    import sys
    if sys.argv[3] == 'b':
        blink(sys.argv[1], sys.argv[2])
    elif sys.argv[3] == 'a':
        appear(sys.argv[1], sys.argv[2])
    elif sys.argv[3] == 'spam':
        spam(sys.argv[1], sys.argv[2], sys.argv[4], sys.argv[5])
    elif sys.argv[3] == 'bb':
        blink_word(sys.argv[1], sys.argv[2])

