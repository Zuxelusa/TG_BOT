import random
from time import sleep

def inputcheck(n: str, rng_from: int, rng_to: int):
    if n.isdigit():
        if rng_from <= int(n) < rng_to + 1:
            return int(n)
    return f"Нужно число от {rng_from} до {rng_to}"

# жребий
# def su_e_fa():
#     while True:
#         variants = {
#             0: "КАМЕНЬ",
#             1: "НОЖНИЦЫ",
#             2: "БУМАГА"
#         }
#         print("Определим, кто ходит первым на 'Камень-Ножницы-Бумага'. ", end="")
#         sleep(0.5)
#         print("Раз! ", end="")
#         sleep(0.5)
#         print("Два! ", end="")
#         sleep(0.5)
#         print("Три! ")
#         bot = random.randint(0, 2)
#         user = input("Что вы показали ? (0 - к, 1 - н, 2 - б) ")
#         if user.isdigit():
#             user = int(user)
#             if 0 <= user < 3:
#                 print(f"У меня {variants[bot]},у тебя {variants[user]}.")
#                 if bot == user:
#                     print("Ничья!")
#                     print("Сыграем еще раз!")
#                 else:
#                     if (bot == 0 and user == 1) or (bot == 1 and user == 2) or (bot == 2 and user == 0):
#                         print("Я выиграл!")
#                         return -1
#                     else:
#                         print("Ты выиграл!")
#                         return 1
#             else:
#                 print("Нужно ввести 0 или 1 или 2.")
#         else:
#             print("Не понял вас...")
#             True

# процедура хода игрока (для бота и для игрока)
def input_player(limit: int, total: int,  player):
    if player == 0:
        cur = random.randint(1, min(total - 1, limit))
        return cur
    else:
        return "Сколько конфет забираете: "

def game_intro(limit, total):
    return (f"Кто возьмет последним, тот проиграл.\n"
      f"Брать можно не более чем {limit} конфет за ход.\nВсего на столе {total} конфет.\n")

# def player_type():
#     return inputcheck("Выберите режим игры: с ботом (0) или с другом(1): ", 0, 1)
def player_type(update):
    return inputcheck(update, "Выберите режим игры: с ботом (0) или с другом(1): ", 0, 1)