import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from get_token import get_telegram_token
from t_bot_commands.commands import start, calc, candies
from t_bot_handlers.handlers import *

TOKEN = get_telegram_token()

# # Enable logging
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )
# logger = logging.getLogger(__name__)

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    calc_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('calc', calc)],
        states={
            1: [MessageHandler(Filters.text, input_calc_exp)],
        },
        fallbacks=[],
    )
    dispatcher.add_handler(calc_conv_handler)

    game_candies_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('candies', candies)],
        states={
            1: [MessageHandler(Filters.text, game_choice)],
            2: [MessageHandler(Filters.text, su_e_fa_ans)],
            20: [MessageHandler(Filters.text, friend_order)],
            3: [MessageHandler(Filters.text, game_body)],
        },
        fallbacks=[],
    )
    dispatcher.add_handler(game_candies_conv_handler)

    # player_profile_conv_handler = ConversationHandler(
    #     entry_points=[CommandHandler('player_profile', player_profile_command)],
    #     states={
    #         PLAYER_NAME_STATE: [MessageHandler(Filters.text, input_player_name_handler)],
    #         PLAYER_AGE_STATE: [MessageHandler(Filters.text, input_player_age_handler)],
    #         PLAYER_GENDER_STATE: [MessageHandler(Filters.text, input_player_gender_handler)]
    #     },
    #     fallbacks=[],
    # )
    # dispatcher.add_handler(player_profile_conv_handler)

    # Start the Bot
    updater.start_polling()
    print("BOT STARTED")
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.

    updater.idle()

if __name__ == '__main__':
    main()

