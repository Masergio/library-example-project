from aiogram import Bot, Dispatcher, types

from django.conf import settings
from tg_bot.models import Chat

# Initialize bot and dispatcher
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help', 'welcome'])
async def send_welcome(message: types.Message):
    chat_id = message.chat.id
    username = message.from_user.full_name or message.from_user.username
    obj, created = await Chat.objects.aget_or_create(chat_id=chat_id, username=username)
    if created is True:
        print(f"***Created new user chat={obj}")
    await message.reply("Hi!\nI'm LibraryBot!\nI will send your useful news.")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def show_cats(message: types.Message):
    with open('data/cat.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    await message.answer(message.text[::-1])
