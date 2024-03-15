from telebot import TeleBot
import json
import facebook
from urlextract import URLExtract
from telebot.types import Message
from requests import post
access_token="EAAv3kbozAgMBO1DZCYwuM4f6nEG6w8OVPiW0MtKnYdDMrMbXnVvNDZAZBNsRxa0TZCJxJfkRf5DUDEnlfPp78yYff19PSCbnMgr0RGy4x73yR9C0N5gwzg62rj959xGav1IPtSEHnM8BYfWGNZAYHCB1TlV051zIgZAeAG3XuNdBz7M3Xd2SzdAj8x7asL0U8ZD"
page_id="233223429882748"
extractor=URLExtract()
def remove_urls(urls,text):
    for url in urls:
        text=text.replace(url,'')
    return text
def handle_incoming(message:Message,bot:TeleBot):
    print(message)
    text=message.text if message.text else message.caption 
    #url=f"https://graph.facebook.com/v19.0/{page_id}/feed"
    urls=extractor.find_urls(text)
    to_send="BuY Link In Comment"+"\n"+remove_urls(urls=urls,text=text)
    print(to_send)
    fb=facebook.GraphAPI(access_token=access_token)
    comment=""
    for url in urls:
        comment+=url+"\n"
    if message.content_type=="photo":
        fileID=message.photo[-1].file_id
        file_info= bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        try:
            result=fb.put_photo(image=downloaded_file,message=to_send,parent_object=page_id)
        except Exception as e:
            print(e)
        else:
            print(result)
            try:
                fb.put_comment(object_id=result['id'],message=comment)
            except Exception as e:
                print(e)
    else:
        try:
            result=fb.put_object(parent_object=page_id,message=to_send,connection_name="feed")
        except Exception as e:
            print(e)
        else:
            print(result)
            try:
                fb.put_comment(object_id=result['id'],message=comment)
            except Exception as e:
                print(e)