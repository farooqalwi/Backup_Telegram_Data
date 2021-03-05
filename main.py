from telethon.sync import TelegramClient
import json
import ast    # to convert strign to dic

api_id=3175343146456
api_hash='39da8f7f70b84e0a71'

client = TelegramClient('test_session', api_id, api_hash)
client.start()

# to store json data in a list
json_dict = dict()


for message in client.iter_messages('vuopak', limit=1, reverse=True):
    # print(dir(message))
    # print(message.date)
    # print(message.id)
    # print(message.text)
    # print(message.raw_text)
    
    # string_to_dic = ast.literal_eval(message.to_json())
    # print(type(message.to_json()))
    json_dict = message.to_json()

    # client.download_media(message)

# import jsonpickle
# json_dict = jsonpickle.encode(json_dict)
# print(type(json_dict))
# print(json_dict)

# with open('result.json', 'w', encoding='utf-8') as file:
#     json.dump(json_list, file, ensure_ascii=False, indent=1)