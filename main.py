from wiki import wiki_bot
# from trans import trans_bot
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from aiogram.filters import CommandStart, Command
from aiogram.types import Message

TOKEN = "7421047891:AAGDzakl1Zm_zm7v2CQnOubX2EWb-m3Ws5Y"

dp = Dispatcher()

@dp.message(Command("salom"))
async def salom_handler(message: Message):
    await message.reply(f"Salom {message.from_user.username} Xush kelibsiz!")

@dp.message(Command("help"))
async def help_handler(msg: Message):
    await msg.answer(f"Salom sizga qanday yordam bera olaman \n\nbizning botimizdagi buyuriqlar \n/start - botni ishga tushurish \n/salom - botni uzbekcha ishga tushirish \n/help - botdan yordam so'rash \n/number - raqamni ko'rib olish \n/age - yoshni ko'rib olish")

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

# @dp.message()
# async def trans_handler(msg: Message):
#     text = msg.text
#     await msg.reply(trans_bot(text))

@dp.message()
async def wiki_handler(msg: Message):
    text = msg.text
    await msg.reply(wiki_bot(text))

@dp.message()
async def echo_handler(message: Message) -> None:

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())