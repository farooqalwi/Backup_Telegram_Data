from telethon.sync import TelegramClient
import json

api_id=3172543
api_hash='f7f77128624651fb67'

client = TelegramClient('test_session', api_id, api_hash)
client.start()

# to store json data in a list
json_list = list()



for message in client.iter_messages('vuopak', limit=1, reverse=True):
    # print(dir(message))
    # print(message.date)
    # print(message.id)
    # print(message.text)
    # print(message.raw_text)
    json_list.append(message.to_json())
    # client.download_media(message)


print(json_list)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(json_list, file, ensure_ascii=False, indent=1)