import telebot

bot = telebot.TeleBot("7447412173:AAHOAXIRzqDeDb_By4nkDaGBzS1WIx3YpQs")


@bot.message_handler(commands=["command1"])
def start_handler(message):
    bot.send_message(message.chat.id, "Привет, отправь следующую команду")


@bot.message_handler(commands=["command2"])
def com2_handler(message):
    bot.send_message(message.chat.id, "[Игры для девочек](https://poki.com/ru/девочки#utm_source=redirect-en-ru)",
                     parse_mode="Markdown")


@bot.message_handler(commands=["command3"])
def com3_handler(message):
    bot.send_message(message.chat.id,
                     "[Игры для мальчиков](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://poki.com/en/boy&ved=2ahUKEwjCvMHw_-KHAxUvQEEAHddCGfEQFnoECBQQAQ&usg=AOvVaw2uCMxsyoj5tRzdIwXSZuis)",
                     parse_mode="Markdown")


bot.infinity_polling()