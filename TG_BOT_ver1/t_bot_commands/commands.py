from t_bot_handlers.handlers import *
from ui import game_intro

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    print(f"{user.full_name} подключился!")
    update.message.reply_text(f"Привет, {user.full_name}!\nСписок команд:\nКалькулятор: /calc\nИгра \"Конфеты\": /candies\n")

# калькулятор
def calc(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Введи выражение:\n")
    return 1

# поиграть в игру 2021
def candies(update: Update, context: CallbackContext) -> None:
    pr = update.message
    init_var()
    pr.reply_text(f"Начинаем игру \"Конфеты\"\n")
    pr.reply_text(game_intro(limit, total))
    reply_kb_markup = ReplyKeyboardMarkup([["с ботом", "с другом"], ], one_time_keybord=True)
    pr.reply_text("Выберите режим игры: ", reply_markup=reply_kb_markup)
    return 1