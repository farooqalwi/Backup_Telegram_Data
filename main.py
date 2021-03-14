# getting telegram development credentials in telegram API Development Tools
from TG_id_hash import api_id, api_hash
from telethon.sync import TelegramClient
import json
import os
import shutil

client = TelegramClient('test_session', api_id, api_hash)
client.start()

# to store json dict data in a list
json_list = list()

# directories for meddia files
os.makedirs("photos", exist_ok = True)


for message in client.iter_messages('vuopak', limit=10, reverse=True):
    # print(dir(message))
    print("message id: ", message.id)
    # print(message.date)
    # print(message.text)
    # print(message.raw_text)
    # print(message.to_json())
    # print(message.get_entities_text())
    # print(client.download_media(message))

    if message.photo is not None:
        print("photo id: ", message.photo.id)
        print("photo date: ", message.photo.date)
        print("photo dc_id: ", message.photo.dc_id)
        print("photo access_hash: ", message.photo.access_hash)
        print("photo file_reference: ", message.photo.file_reference)
        # print("photo from_reader: ", message.photo.from_reader())
        print("photo has_stickers: ", message.photo.has_stickers)
        # print("photo pretty_format: ", message.photo.pretty_format())
        # print("photo iserialize_bytes: ", message.photo.serialize_bytes())
        # print("photo serialize_datetime: ", message.photo.serialize_datetime())
        print("photo sizes: ", message.photo.sizes())
        print("photo stringify: ", message.photo.stringify())
        print("photo video_sizes: ", message.photo.video_sizes)
        print("photo to_dict: ", message.photo.to_dict())
        print("photo to_json: ", message.photo.to_json())
    else:
        print("None")


    
#     json_string = message.to_json()
#     # convert string to dictionary
#     str_dict = json.loads(json_string)
#     # empty dict to store json data in a dict after filteration
#     json_nestedDict = dict()

#     for key, value in str_dict.items():
#         # for id and date
#         if key == "id" or key == "date":
#             json_nestedDict[key] = value
        
#         # for edited date
#         if key == "edit_date" and value != None:
#             json_nestedDict["edited"] = value
        
#         '''
#         # for text
#         if key == "message":
#             text_list = []
#             for text_type, inner_text in message.get_entities_text():
#                 print(text_type)
#                 print(type(text_type))
#                 print(inner_text)
#                 print(type(inner_text))
#                 text_dict = {text_type : inner_text}
#                 text_list.append(text_dict)
#             json_nestedDict["text"] = text_list
#         '''
        
#         # for title
#         if key == "action":
#             for subKey, subValue in value.items():
#                 if subKey == "title":
#                     json_nestedDict[subKey] = subValue


#     # for photos
#     # it generates photo and assign photo name in a variable
#     photo_name = client.download_media(message)
#     if photo_name != None:
#         path = os.path.join('photos', photo_name)
#         # to move photo to photos_dir
#         # if file exists then do not move it
#         # delete existed files
#         if not os.path.isfile(path):
#             shutil.move(photo_name, 'photos')
#         else:
#             os.remove(photo_name)

#         # to update json
#         json_nestedDict['photo'] = path
        

#     # insert dict into list
#     json_list.append(json_nestedDict)

    
# json_dict = { "name": "Virtual University of Pakistan", "type": "public_channel", "id": 9999969886, "messages": []}
# # putting list to a dict in order to obtain result.json file
# json_dict["messages"] = json_list

# with open('custom_result.json', 'w', encoding='utf-8') as file:
#     json.dump(json_dict, file, ensure_ascii=False, indent=1)

