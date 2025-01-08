from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import logging

API_TOKEN = '5166535439:AAGC3HqIr4KTiasGH6hG6z6N8ijGNPd-Mu8'  # Bot tokeningizni shu yerga qo'ying

# Bot va dispatcher yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

# /start komandasi uchun handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("TINGLASH", web_app=types.WebAppInfo(url="https://763e-90-156-164-117.ngrok-free.app"))
    )
    await message.answer("Qo'shiqni tinglash uchun ushbu tinglash tugmasini bosing", reply_markup=keyboard)

# Botni ishga tushirish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
