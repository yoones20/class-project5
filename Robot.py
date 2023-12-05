from ast import main
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  level=logging.INFO)

logger = logging.getLogger(name)

def start(update, context):

    """Send a message when the command /start is issued."""

    update.message.reply_text('Hi!')





def help(update, context):

    """Send a message when the command /help is issued."""

    update.message.reply_text('Help!')





def echo(update, context):

    """Echo the user message."""

    update.message.reply_text(update.message.text)
 




def error(update, context):

    """Log Errors caused by Updates."""

    logger.warning('Update "%s" caused error "%s"', update, context.error)

    updater = Updater(6646644652:AAE1zlPXWJi05ld-k666D4wGwYj4wEdOPdE, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


    if name == 'main':

        main()