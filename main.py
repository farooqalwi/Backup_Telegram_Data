from telethon.sync import TelegramClient
import json

api_id=317
api_hash='39da8f7f70b8'

client = TelegramClient('test_session', api_id, api_hash)
client.start()

# to store json data in a dic
json_dict = dict()
# json_list = list()

# def addItem(key, value):
#     json_dict[key] = value

for message in client.iter_messages('vuopak', limit=1, reverse=True):
    # print(dir(message))
    # print(message.date)
    # print(message.id)
    # print(message.text)
    # print(message.raw_text)
    # print(message.to_json())


    json_string = message.to_json()

    # convert string to dictionary
    str_dict = json.loads(json_string) 
    for key, value in str_dict.items():
        if key == "id" or key == "date" or key == "photo" or key == "file" or key == "thumbnail":
            json_dict[key] = value
        
    # json_list.append(json_dict)

    # client.download_media(message)

 

print(type(json_dict))
print(json_dict)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(json_dict, file, ensure_ascii=False, indent=1)
