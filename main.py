# getting telegram development credentials in telegram API Development Tools
from TG_id_hash import api_id, api_hash
from telethon.sync import TelegramClient
import json

client = TelegramClient('test_session', api_id, api_hash)
client.start()

# to store json dict data in a list
json_list = list()


for message in client.iter_messages('vuopak', limit=100, reverse=True):
    # print(dir(message))
    # print(message.date)
    # print(message.id)
    # print(message.text)
    # print(message.raw_text)
    # print(message.to_json())


    json_string = message.to_json()
    # convert string to dictionary
    str_dict = json.loads(json_string)
    # empty dict to store json data in a dict after filteration
    json_dict = dict()

    for key, value in str_dict.items():
        if key == "id" or key == "date" or (key == "edit_date" and value != None ) or key == "photo" or key == "file" or key == "thumbnail" or key == "message":
            json_dict[key] = value
    


    # insert dict into list
    json_list.append(json_dict)

    # client.download_media(message)

 

print(type(json_list))
print(json_list)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(json_list, file, ensure_ascii=False, indent=1)
