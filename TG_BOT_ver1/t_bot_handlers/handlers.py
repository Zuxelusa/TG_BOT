# обработчик калькулятора
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from ui import inputcheck

limit = 0
total = 0
step = 0
player_type = 0

def init_var():
    global limit, total, step, player_type
    limit = 28
    total = 221
    step = 1
    player_type = 0

def input_calc_exp(update: Update, context: CallbackContext) -> int:
    calc_exp = update.message.text
    if calc_exp.lower() == "quit":
        return ConversationHandler.END
    else:
        try:
            update.message.reply_text(eval(calc_exp))
        except NameError:
            update.message.reply_text("Не понял вас. Для выхода: 'quit'")
        except SyntaxError:
            update.message.reply_text("Неверная формула.")
        return 1

def game_choice(update: Update, context: CallbackContext) -> int:
    # choice = inputcheck(update.message.text, 0, 1)
    global step, player_type
    choice = update.message.text
    if choice == "с ботом" or choice == "с другом":
        if choice == "с ботом":
            # определить первый ход жребием
            player_type = 0
            pr = update.message.reply_text
            pr(f"Но сначала ...")
            pr("Определим, кто ходит первым на 'Камень-Ножницы-Бумага'. ")
            pr("Раз - Два - Три!")
            reply_kb_markup = ReplyKeyboardMarkup([["Камень", "Ножницы", "Бумага"], ], one_time_keybord=True)
            pr("Что вы показали ?", reply_markup=reply_kb_markup)
            return 2
        if choice == "с другом":
            player_type = 1
            reply_kb_markup = ReplyKeyboardMarkup([["Я", "Друг"], ], one_time_keybord=True)
            update.message.reply_text("Кто ходит первым?", reply_markup=reply_kb_markup)
            return 20
    else:
        return 1

def friend_order(update: Update, context: CallbackContext) -> int:
    global step
    choice = update.message.text
    pr = update.message.reply_text
    if choice == "Я":
        step = 1
    elif choice == "Друг":
        step = -1
    else:
        return 20
    pr(f"Начинаем игру! У нас на столе {total} конфет.")
    if step == 1:
        pr(f"Ваш ход!")
        pr("Сколько конфет забираете: ")
    if step == -1:
        pr(f"Ход второго игрока!")
        pr("Сколько конфет забираете: ")
    return 3
    # game_start(update, context)

def su_e_fa_ans(update: Update, context: CallbackContext) -> int:
    global step, total, limit
    pr = update.message.reply_text
    choice = update.message.text.upper()
    variants = {
                    0: "КАМЕНЬ",
                    1: "НОЖНИЦЫ",
                    2: "БУМАГА"
                }
    bot = random.randint(0, 2)
    pr(f"У меня {variants[bot]},у тебя {choice}.")
    if variants[bot] == choice:
            pr("Ничья!")
            pr("Сыграем еще раз!")
            pr("Раз - Два - Три!")
            reply_kb_markup = ReplyKeyboardMarkup([["Камень", "Ножницы", "Бумага"], ], one_time_keybord=True)
            pr("Что вы показали ?", reply_markup=reply_kb_markup)
            return 2
    else:
        if (bot == 0 and choice == "НОЖНИЦЫ") or (bot == 1 and choice == "БУМАГА") or (bot == 2 and choice == "КАМЕНЬ"):
            pr("Я выиграл!")
            step = -1
        else:
            pr("Ты выиграл!")
            step = 1

    pr(f"Начинаем игру! У нас на столе {total} конфет.")
    if step == 1:
        pr(f"Твой ход!")
        pr("Сколько конфет забираете: ")
        step = 1
    else:
        pr(f"Мой ход")
        cur = random.randint(1, min(total - 1, limit))
        total -= cur
        pr(f"Я забираю {cur} конфет(ы).\n")
        pr(f"У нас на столе {total} конфет.")
        pr(f"Ваш ход!")
        pr("Сколько конфет забираете: ")
        step = 1
    return 3

def game_body(update: Update, context: CallbackContext) -> int:
    global step, total, limit, player_type
    pr = update.message.reply_text
    cur = inputcheck(update.message.text, 1, min(total - 1, limit))
    print(f"cur = {cur}, step = {step}, player_type = {player_type}")

    if type(cur) == int:
        step *= -1
        # if step == 1 and player_type != 0:
        if step == 1:
            total -= cur
            if check_status(pr): return ConversationHandler.END
            pr(f"Сейчас на столе {total} конфет(ы).\n")
            pr(f"Твой ход!")
            pr("Сколько конфет забираете: ")

        # процедура хода игрока 2 или бота
        if step == -1:
            if player_type == 0:
                total -= cur
                if check_status(pr): return ConversationHandler.END
                pr(f"Сейчас на столе {total} конфет(ы).\n")
                pr(f"Мой ход")
                cur = random.randint(1, min(total - 1, limit))
                total -= cur
                pr(f"Я забираю {cur} конфет(ы).\n")
                if check_status(pr): return ConversationHandler.END
                pr(f"Сейчас на столе {total} конфет(ы).\n")
                pr(f"Твой ход!")
                pr("Сколько конфет забираете: ")
                step = 1
            elif player_type == 1:
                total -= cur
                if check_status(pr): return ConversationHandler.END
                pr(f"Сейчас на столе {total} конфет(ы).\n")
                pr(f"Ход второго игрока!")
                pr("Сколько конфет забираете: ")
    else:
        pr(cur)
    return 3

def check_status(pr) -> bool:

    if total == 1:
        pr(f"Сейчас на столе {total} конфета.\n")
        if step == -1 and player_type == 0:
            pr("Я выиграл!")
        if step == -1 and player_type == 1:
            pr("Ты выиграл!")
        if step == 1 and player_type == 1:
            pr("Победа второго игрока")
        return True
    else:
        return False


