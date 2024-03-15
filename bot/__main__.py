from telebot import TeleBot
from telebot.types import Message
from handler import handle
api="1649598540:AAE0Q-XfbHkfsqrEr6LfyDJDBbYF7vq0uUE"
bot=TeleBot(token=api)
if __name__=="__main__":
    bot.register_channel_post_handler(callback=handle.handle_incoming,pass_bot=True)
    bot.infinity_polling(allowed_updates=[])