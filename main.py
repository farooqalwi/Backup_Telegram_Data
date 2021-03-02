from telethon.sync import TelegramClient

api_id=1234567
api_hash='faroq'

client = TelegramClient('test_session', api_id, api_hash)
client.start()

for message in client.iter_messages('vuopak', limit=2, reverse=True):
    # print(dir(message))
    print(message.date)
    print(message.id)
    # print(message.text)
    # print(message.raw_text)
    # print(message.to_json())
    # client.download_media(message)
