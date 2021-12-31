#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

menu_items = ['/help - display commands\n',
              '/test - request system response\n',
              '/start - init bot\n',
              '/kdwrite - write to knowledge base\n',
              '/kdsearch - search knowledge base\n',
              '/newdebit - add debit to sheet\n',
              '/viewsheet - view finacial sheet\n',
              '/addcredit - add credit to sheet\n',
              '/newtask - add task to list\n',
              '/viewtask - view task list\n', 
              '/completetask - complete task on list\n',
              '/deltask - delete task on list\n',
              '/author - justin johnson\n']

MENU = "".join(menu_items)

WHITELIST = 1786291673
BLACKLIST = 0

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, commandhandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def checkUser(update, context):
    user = update.message.from_user
    if(user['id'] != WHITELIST):
        BLACKLIST = str(user['id'])
        blist = open("blacklist.txt", "w+")
        blist.write(BLACKLIST+"\n")
        blist.close()
        return False
    elif(user['id'] == WHITELIST):
        return True

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('Python Butler Version 1 - ready()')

def help(update, context):
    """Send a message when the command /help is issued."""
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text(MENU)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def comHandler(update, context):
    """ Get user input (not commands) """
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('casual conversation')

def kdwrite(update, context):
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('kdwrite')

def kdsearch(update, context):
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('kdsearch')

def newdebit(update, context):
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('newdebit')

def viewsheet(update, context):
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('viewsheet')

def addcredit(update, context):
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('addcredit')

def newtask(update, context):
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('newtask')

def viewtask(update, context):
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('view task')

def completetask(update, context):
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('complete task')

def deltask(update, context):
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('delete task')

def author(update, context):
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('Author: Justin Johnson')

def test(update, context):
    results = checkUser(update=update, context=context)
    if(results == False):
        update.message.reply_text('You are not Authorized! - not whitelisted!')
    else:
        update.message.reply_text('Butler is ready')

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("5055389915:AAFUOyWio4PwggZ7IN3DI19M2NM7lh5kFQA", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("newdebit", newdebit))
    dp.add_handler(CommandHandler("viewsheet", viewsheet))
    dp.add_handler(CommandHandler("addcredit", addcredit))
    dp.add_handler(CommandHandler("newtask", newtask))
    dp.add_handler(CommandHandler("viewtask", viewtask))
    dp.add_handler(CommandHandler("completetask", completetask))
    dp.add_handler(CommandHandler("deltask", deltask))
    dp.add_handler(CommandHandler("author", author))
    dp.add_handler(CommandHandler("kdwrite", kdwrite))
    dp.add_handler(CommandHandler("kdsearch", kdsearch))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("test", test))


    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, comHandler))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()