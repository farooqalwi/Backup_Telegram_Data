# getting telegram development credentials in telegram API Development Tools
from TG_id_hash import api_id, api_hash
from telethon.sync import TelegramClient
import json
import os

client = TelegramClient('test_session', api_id, api_hash)
client.start()

# to store json dict data in a list
json_list = list()


for message in client.iter_messages('vuopak', limit=20, reverse=True):
    # print(dir(message))
    # print(message.id)
    # print(message.date)
    # print(message.text)
    # print(message.raw_text)
    # print(message.to_json())
    # print(message.get_entities_text())
    # print(client.download_media(message))

    
    json_string = message.to_json()
    # convert string to dictionary
    str_dict = json.loads(json_string)
    # empty dict to store json data in a dict after filteration
    json_nestedDict = dict()

    for key, value in str_dict.items():
        # for id and date
        if key == "id" or key == "date":
            json_nestedDict[key] = value
        
        # for edited date
        if key == "edit_date" and value != None:
            json_nestedDict["edited"] = value
        
        # for text
        if key == "message":
            text_list = []
            for text_type, inner_text in message.get_entities_text():
                text_dict = {text_type : inner_text}
                text_list.append(text_dict)
            json_nestedDict["text"] = text_list
        
        
        if key == "action":
            for subKey, subValue in value.items():
                if subKey == "title":
                    json_nestedDict[subKey] = subValue


    # for photos            
    # if client.download_media(message) != None:
    #     fullPath = os.path.join('photos', client.download_media(message))
    #     json_nestedDict['photo'] = fullPath
        

    # insert dict into list
    json_list.append(json_nestedDict)

    # client.download_media(message)


json_dict = { "name": "Virtual University of Pakistan", "type": "public_channel", "id": 9999969886, "messages": []}
# putting list to a dict in order to obtain result.json file
json_dict["messages"] = json_list

with open('custom_result.json', 'w', encoding='utf-8') as file:
    json.dump(json_dict, file, ensure_ascii=False, indent=1)

