import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, FSInputFile, WebAppInfo
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = "7621000610:AAHgzBhpQ2xjaZFbqLrOMiJvPSM2AxOJHsY"

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

dp.include_router(router)



# Счетчики лайков и дизлайков
likes = 0
dislikes = 0

# Главное меню
def get_main_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="📅 Показать расписание", callback_data="show_schedule")
    builder.button(text="📖 Показать методики", callback_data="show_methods") 
    builder.button(text="🔔 Показать расписание звонков", callback_data="show_bell_schedule")
    builder.button(text="📊 Опрос", callback_data="start_poll")
    return builder.as_markup()

# Опрос
def get_poll_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="👍 Нравится", callback_data="poll_like"),
             InlineKeyboardButton(text="👎 Не нравится", callback_data="poll_dislike")]
        ]
    )

@dp.callback_query(F.data == "start_poll")
async def poll_callback(call: types.CallbackQuery):
    await call.message.answer("Как вам бот? Оставьте отзыв!", reply_markup=get_poll_keyboard())
    await call.answer()

@dp.callback_query(F.data.in_(["poll_like", "poll_dislike"]))
async def poll_feedback(call: types.CallbackQuery):
    global likes, dislikes
    
    if call.data == "poll_like":
        likes += 1
        text = f"Спасибо за вашу поддержку! 😊\n👍 Лайков: {likes} | 👎 Дизлайков: {dislikes}"
    else:
        dislikes += 1
        text = f"Мы учтём ваш отзыв и постараемся улучшить бот! 😔\n👍 Лайков: {likes} | 👎 Дизлайков: {dislikes}"
    
    await call.message.answer(text)
    await call.answer()

@dp.message(Command("start", "main", "hello"))
async def start_command(message: types.Message):
    user = message.from_user
    text = f"Привет, {user.first_name}!\nТвой ID: {user.id}\n"
    if user.username:
        text += f"Твой username: @{user.username}"
    await message.answer(text, reply_markup=get_main_menu())


# Кнопки для отправки файлов
def get_file_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📄 Получить файл 1")],
            [KeyboardButton(text="📄 Получить файл 2")]
        ],
        resize_keyboard=True
    )

@dp.message(Command("app"))
async def start_web(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Открыть веб", web_app=WebAppInfo(url="https://docs.aiogram.dev/en/v3.18.0/"))]
        ],
        resize_keyboard=True
    )
    
    # Ответ с кнопкой
    await message.answer("Нажми кнопку, чтобы открыть веб-приложение.", reply_markup=keyboard)

# Файлы
@dp.message(Command("files"))
async def send_file_menu(message: types.Message):
    await message.answer("Выберите файл:", reply_markup=get_file_menu())

@dp.message(F.text == "📄 Получить файл 1")
async def send_file1(message: types.Message):
    file_path = "documents/file1.docx"
    await message.answer_document(FSInputFile(file_path), caption="Вот ваш документ 📄")

@dp.message(F.text == "📄 Получить файл 2")
async def send_file2(message: types.Message):
    file_path = "documents/file2.docx"
    await message.answer_document(FSInputFile(file_path), caption="Вот ваш документ 📄")

# /start
@dp.message(Command("start", "main", "hello"))
async def start_command(message: types.Message):
    user = message.from_user
    text = f"Привет, {user.first_name}!\nТвой ID: {user.id}\n"
    if user.username:
        text += f"Твой username: @{user.username}"
    await message.answer(text, reply_markup=get_main_menu())

# /help
@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("<b>help</b> <em><u>information</u></em>", parse_mode="HTML")

# /site
@dp.message(Command("site"))
async def site_command(message: types.Message):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Перейти на сайт", url="https://donstu.ru/university/...")]
        ]
    )
    await message.answer("🌐 Официальный сайт:", reply_markup=markup)

# Приветствие
@dp.message(F.text.lower() == "привет")
async def greet_user(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}! 😊", reply_markup=get_main_menu())

@dp.message(F.text == "СИС-31")
async def send_schedule_sis31(message: types.Message):
    await message.answer_photo(FSInputFile("assets/f1.jpg"), caption="Ваше расписание")

@dp.message(F.text == "СИС-32")
async def send_schedule_sis32(message: types.Message):
    await message.answer_photo(FSInputFile("assets/F2.jpg"), caption="Ваше расписание")

# Обработчик inline-кнопок
@dp.callback_query(F.data.in_(["show_schedule", "show_methods", "show_bell_schedule"]))
async def callback_handler(call: types.CallbackQuery):
    if call.data == "show_schedule":
        text = (
            "📅 *Расписание занятий:*\n"
            "🕘 08:00 - 09:30 | Пара 1\n"
            "🕙 09:45 - 11:15 | Пара 2\n"
            "🕛 11:30 - 13:00 | Пара 3\n"
            "🕑 13:45 - 15:15 | Пара 4\n"
            "🕒 15:30 - 17:00 | Пара 5\n"
        )
    elif call.data == "show_methods":
        text = (
            "📖 *Методические материалы:*\n"
            "1️⃣ Основы программирования\n"
            "2️⃣ Алгоритмы и структуры данных\n"
            "3️⃣ Базы данных и SQL\n"
            "4️⃣ Веб-разработка\n"
            "5️⃣ Машинное обучение\n"
        )
    else:
        text = (
            "🔔 *Расписание звонков:*\n"
            "🕘 08:00 - 09:30 | 1-я пара\n"
            "🕙 09:45 - 11:15 | 2-я пара\n"
            "🕛 11:30 - 13:00 | 3-я пара\n"
            "🕑 13:45 - 15:15 | 4-я пара\n"
            "🕒 15:30 - 17:00 | 5-я пара\n"
        )

    await call.message.answer(text, parse_mode="Markdown")
    await call.answer()

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
