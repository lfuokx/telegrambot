import telebot
import searcher

bot = telebot.TeleBot('6199614952:AAHR_lJmfHbMIDguJMJ6ptxgF4VFe04CXzM')
task = ""


@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    if task == "":
        msg = bot.reply_to(message, "Hey, lets search for something! What genre of the book do you like?")
        bot.register_next_step_handler(msg, process_genre_step)


def process_genre_step(message):
    msg = bot.reply_to(message, "What writer do you prefer?")
    global task
    task += message.text
    bot.register_next_step_handler(msg, process_writer_step)


def process_writer_step(message):
    msg = bot.reply_to(message, "How is his book called?")
    global task
    task += " " + message.text
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    global task
    task += " " + message.text + "listen to an audiobook"
    bot.reply_to(message, searcher.youtube_search(task))
    print("results for:", task)
    task = ""


bot.infinity_polling()
