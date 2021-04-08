import configparser
import os
from telethon.sync import TelegramClient
import json
import shutil
from threading import Thread

# telegram development credentials in telegram API Development Tools
config = configparser.ConfigParser()

if not os.path.exists('config.ini'):
    api_id_from_user = input("Enter API ID first time: ")
    api_hash_from_user = input("Enter API HASH first time: ")
    # Writing Configs
    config['Telegram'] = {'api_id': api_id_from_user, 'api_hash': api_hash_from_user}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


# Reading Configs
config.read("config.ini")
# Setting configuration values
api_id = int(config['Telegram']['api_id'])
api_hash = config['Telegram']['api_hash']

client = TelegramClient('test_session', api_id, api_hash)
client.start()

# to store json dict data in a list
json_list = list()


for message in client.iter_messages('vuopak', limit=220, reverse=True):
    # print(dir(message))
    print("message id: ", message.id)
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
        # print("file id: ", message.file.id)
        # print("file name: ", message.file.name)
        # print("file title: ", message.file.title)
        # print("file duration: ", message.file.duration)
        # print("file emoji: ", message.file.emoji)
        # print("file ext: ", message.file.ext)
        # print("file width: ", message.file.width)
        # print("file height: ", message.file.height)
        # print("file media: ", message.file.media)
        # print("file mime_type: ", message.file.mime_type)
        # print("file performer: ", message.file.performer)
        # print("file size: ", message.file.size)
        # print("file sticker_set: ", message.file.sticker_set)
    # else:
    #     print("None")


    
    json_string = message.to_json()
    # print(json_string)
    # convert string to dictionary
    str_dict = json.loads(json_string)
    # empty dict to store json data in a dict after filteration
    json_nestedDict = dict()
    # print(str_dict.items())

    for key, value in str_dict.items():
        # for id and date
        if key == "id" or key == "date":
            json_nestedDict[key] = value
        
        # for edited date
        if key == "edit_date" and value is not None:
            json_nestedDict["edited"] = value
        
        # for title
        if key == "action":
            for subKey, subValue in value.items():
                if subKey == "title":
                    json_nestedDict[subKey] = subValue

    # for reply_to_msg_id
    if message.reply_to_msg_id is not None:
        json_nestedDict["reply_to_msg_id"] = message.reply_to_msg_id
    

    # for media
    if message.file is not None and 'jpeg' in message.file.mime_type:
        # jpeg is for photos
        media_name = client.download_media(message, 'photos')
        if media_name is not None:
            # to update json
            if 'photo_' and '.jpg' in media_name:
                json_nestedDict['photo'] = media_name
    elif message.file is not None and ('png' in message.file.mime_type or 'mpeg' in message.file.mime_type or 'officedocument' in message.file.mime_type or 'msword' in message.file.mime_type):
        # mpeg is for mp3, officedocument is for docx and msword files is for doc
        media_name = client.download_media(message, 'files')
        if media_name is not None:
            # to update json
            if '.mp4' or '.mp3' or '.png' or '.exe' or '.doc' or '.docx' in media_name:
                thumb_name = media_name + "_thumb.jpg"
                json_nestedDict['file'] = media_name
                json_nestedDict['mime_type'] = message.file.mime_type
                json_nestedDict['width'] = message.file.width
                json_nestedDict['height'] = message.file.height
    
    # for thumbnail
    if message.file is not None and 'png' in message.file.mime_type:
        media_name = client.download_media(message, 'files', thumb=-1)
        json_nestedDict['thumbnail'] = thumb_name
    

    # for text
    if message.text is not None:
        json_nestedDict["text"] = message.text

    # insert dict into list
    json_list.append(json_nestedDict)

    
json_dict = { "name": "Virtual University of Pakistan", "type": "public_channel", "id": 9999969886, "messages": []}
# putting list to a dict in order to obtain result.json file
json_dict["messages"] = json_list

with open('custom_result.json', 'w', encoding='utf-8') as file:
    json.dump(json_dict, file, ensure_ascii=False, indent=1)

