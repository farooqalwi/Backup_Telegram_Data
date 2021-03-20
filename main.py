# getting telegram development credentials in telegram API Development Tools
from TG_id_hash import api_id, api_hash
from telethon.sync import TelegramClient
import json
import os
import shutil
from threading import Thread

client = TelegramClient('test_session', api_id, api_hash)
client.start()

# to store json dict data in a list
json_list = list()

obj = client.iter_messages('vuopak', reverse=True)
list_obj = list(obj)

# to donwload files
def file_downloader(start, end):
    for i in range(start, end):
        print("id: ", list_obj[i].id)
        if list_obj[i].photo is not None:
            # print("photo id: ", list_obj[i].photo.id)
            print("media name: ", client.download_media(list_obj[i]))

t1 = Thread(target=file_downloader, args=(0,5))
t1.start()

t2 = Thread(target=file_downloader, args=(5,10))
t2.start()




# for message in client.iter_messages('vuopak', limit=15, reverse=True):
    # print(dir(message))
    # print("message id: ", message.id)
    # print(message.date)
    # print(message.text)
    # print(message.raw_text)
    # print(message.to_json())
    # print(message.get_entities_text())
    # print("media name: ", client.download_media(message))

    
    # # photo attributes
    # print(dir(message.photo))

    # if message.photo is not None:
    #     print("photo id: ", message.photo.id)
    #     print("photo date: ", message.photo.date)
    #     print("photo dc_id: ", message.photo.dc_id)
    #     print("photo access_hash: ", message.photo.access_hash)
    #     print("photo file_reference: ", message.photo.file_reference)
    #     # print("photo from_reader: ", message.photo.from_reader())
    #     print("photo has_stickers: ", message.photo.has_stickers)
    #     # print("photo pretty_format: ", message.photo.pretty_format())
    #     # print("photo iserialize_bytes: ", message.photo.serialize_bytes())
    #     # print("photo serialize_datetime: ", message.photo.serialize_datetime())
    #     print("photo sizes: ", message.photo.sizes())
    #     print("photo stringify: ", message.photo.stringify())
    #     print("photo video_sizes: ", message.photo.video_sizes)
    #     print("photo to_dict: ", message.photo.to_dict())
    #     print("photo to_json: ", message.photo.to_json())
    # else:
    #     print("None")


    # file attributes
    # print(dir(message.file))

    # if message.file is not None:
    #     print("file id: ", message.file.id)
    #     print("file name: ", message.file.name)
    #     print("file title: ", message.file.title)
    #     print("file duration: ", message.file.duration)
    #     print("file emoji: ", message.file.emoji)
    #     print("file ext: ", message.file.ext)
    #     print("file width: ", message.file.width)
    #     print("file height: ", message.file.height)
    #     print("file media: ", message.file.media)
    #     print("file mime_type: ", message.file.mime_type)
    #     print("file performer: ", message.file.performer)
    #     print("file size: ", message.file.size)
    #     print("file sticker_set: ", message.file.sticker_set)
    # else:
    #     print("None")


    
    # json_string = message.to_json()
    # # convert string to dictionary
    # str_dict = json.loads(json_string)
    # # empty dict to store json data in a dict after filteration
    # json_nestedDict = dict()

    # for key, value in str_dict.items():
    #     # for id and date
    #     if key == "id" or key == "date":
    #         json_nestedDict[key] = value
        
    #     # for edited date
    #     if key == "edit_date" and value != None:
    #         json_nestedDict["edited"] = value
        
        
        # # for text
        # if key == "message":
        #     text_list = []
        #     for text_type, inner_text in message.get_entities_text():
        #         print(text_type)
        #         print(type(text_type))
        #         print(inner_text)
        #         print(type(inner_text))
        #         text_dict = {text_type : inner_text}
        #         text_list.append(text_dict)
        #     json_nestedDict["text"] = text_list
        
        
#         # for title
#         if key == "action":
#             for subKey, subValue in value.items():
#                 if subKey == "title":
#                     json_nestedDict[subKey] = subValue


#     # for media 
#     media_name = client.download_media(message)
#     if media_name != None:
#         # to update json
#         if 'photo_' and '.jpg' in media_name:
#             json_nestedDict['photo'] = media_name
#         elif '.mp4' or '.mp3' or '.png' or '.pdf' or '.exe' or '.doc' or '.docx':
#             json_nestedDict['file'] = media_name
#         elif '.png_thumb.jpg' or '.pdf_thumb.jpg' or '.png_thumb.jpg' or '.mp4_thumb.jpg':
#             json_nestedDict['thumbnail'] = media_name
#         else:
#             print("No file type: ", media_name)

#     # insert dict into list
#     json_list.append(json_nestedDict)

    
# json_dict = { "name": "Virtual University of Pakistan", "type": "public_channel", "id": 9999969886, "messages": []}
# # putting list to a dict in order to obtain result.json file
# json_dict["messages"] = json_list

# with open('custom_result.json', 'w', encoding='utf-8') as file:
#     json.dump(json_dict, file, ensure_ascii=False, indent=1)


