# getting telegram development credentials in telegram API Development Tools
from TG_id_hash import api_id, api_hash
from telethon.sync import TelegramClient
import json

client = TelegramClient('test_session', api_id, api_hash)
client.start()

# to store json dict data in a list
json_list = list()


for message in client.iter_messages('vuopak', limit=30, reverse=True):
    # print(dir(message))
    # print(message.date)
    # print(message.id)
    # print(message.text)
    # print(message.raw_text)
    print(message.to_json())


    json_string = message.to_json()
    # convert string to dictionary
    str_dict = json.loads(json_string)
    # empty dict to store json data in a dict after filteration
    json_nestedDict = dict()

    for key, value in str_dict.items():
        if key == "id" or key == "date" or (key == "edit_date" and value != None ):
            json_nestedDict[key] = value
        
        # we are saving it by naming it 'text' because it is available in manual downloaded json by this name
        if key == "message":
            json_nestedDict["text"] = value
        
        
        if key == "action":
            for subKey, subValue in value.items():
                if subKey == "title":
                    json_nestedDict[subKey] = subValue
                    

    # insert dict into list
    json_list.append(json_nestedDict)

    # client.download_media(message)


json_dict = { "name": "Virtual University of Pakistan", "type": "public_channel", "id": 9999969886, "messages": []}
# putting list to a dict in order to obtain result.json file
json_dict["messages"] = json_list

with open('custom_result.json', 'w', encoding='utf-8') as file:
    json.dump(json_dict, file, ensure_ascii=False, indent=1)

