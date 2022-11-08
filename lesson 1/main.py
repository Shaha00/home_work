from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from decouple import config
import logging

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Здрасте-мордасте, {message.from_user.first_name}")


@dp.message_handler(commands=['test'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Сколько длилась столетняя война?"
    answers = [
        "100",
        '139',
        '116',
        '96',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Садись 2!",
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Хакуна-Матата?"
    answers = [
        "Хакуна-Матата",
        "Hamata-Kakuna",
        "We`re the best",
        "Матата-Хакуна",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Почти...",
    )

@dp.message_handler(commands=['mem'])
async def mem(message):
    photo = open("media/028df0020a0f184e0fc08cb4c84b47a3.jpg", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

@dp.message_handler()
async def echo_stepen(message: types.Message):
    try:
        line = message.text
        a = int(line)
        res = a**2
        await bot.send_message(message.from_user.id, str(res))
    except:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)