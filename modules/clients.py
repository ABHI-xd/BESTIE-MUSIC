
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import config


user = Client(config.SESSION, config.API_ID, config.API_HASH)


bot = Client(
    ":memory:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins={"root": "snehabhi"},
)

call_py = PyTgCalls(user)
