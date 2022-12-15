import pandas as pd
import numpy as np
import streamlit as st
#import telebot
#from telebot import types
#import logging

#st.subheader("Web interface")

st.subheader("Telegram bot")

#st.write("You can find bot by this link t.me/Alcash1bot")

# In[ ]:


st.code("logging.basicConfig(filename='bot.log', level=logging.INFO)")


code = '''def dialog_sex(update, context):
    reply_keyboard = [['Мужской'], ['Женский']]
    update.message.reply_text(
        'Пожалуйста, выберите ваш пол:',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True)
    )

    return 'time'")


def dialog_time(update, context):
    sex = update.message.text
    if sex == 'Мужской':
        context.user_data['dialog'] = {'sex': 1}
    elif sex == 'Женский':
        context.user_data['dialog'] = {'sex': 0}
    update.message.reply_text(
        'Сколько у вас свободного времени по шкале от 1 до 5?',
        reply_markup=digits_keyboard()
    )

    return "friends"


def dialog_friends(update, context):
    context.user_data['dialog']['time'] = int(update.message.text)
    update.message.reply_text(
        'По шкале от 1 до 5 – как часто вы встречаетесь с друзьями?',
        reply_markup=digits_keyboard()
    )

    return 'ending'

def dialog_ending(update, context):
    context.user_data['dialog']['friends'] = int(update.message.text)
    sex = context.user_data['dialog']['sex']
    free_time = context.user_data['dialog']['time']
    times_with_friends = context.user_data['dialog']['friends']

    result = (times_with_friends * 9) + (free_time * 9) + 10 * sex

    update.message.reply_text(
        f'Риск подверженности алкоголизму {result}%!',
        reply_markup=main_keyboard()
    )

    return ConversationHandler.END


def dialog_dontknow(update, context):
    update.message.reply_text(
        'Кажется, вы прислали мне что-то не то!'
    )


def main_keyboard():
    return ReplyKeyboardMarkup(
        [['Посчитать степень алкоголизма']]
    )


def digits_keyboard():
    return ReplyKeyboardMarkup(
        [['1', '2', '3', '4', '5']]
    )


def greet_user(update, context):
    user = update.effective_user
    update.message.reply_text(
        f'Привет, {user.first_name}! Если хочешь узнать степень своего алкоголизма, просто напиши мне «Посчитать степень алкоголизма»',
        reply_markup=main_keyboard()
    )


def main():
    mybot = Updater('5807673465:AAHGUxfVfoH7SyrBkablRY8nmYhEhbnMB8w')
    dp = mybot.dispatcher

    dialog = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex(
            '^(Посчитать степень алкоголизма|посчитать степень алкоголизма)$'),
            dialog_sex)],
        states={'time': [MessageHandler(Filters.regex(
            '^(Мужской|Женский)$'), dialog_time)],
            'friends': [MessageHandler(Filters.regex(
                '^(1|2|3|4|5)$'), dialog_friends)],
            'ending': [MessageHandler(Filters.regex(
                '^(1|2|3|4|5)$'), dialog_ending)]},
        fallbacks=[MessageHandler(Filters.text | Filters.video |
                                  Filters.photo | Filters.document |
                                  Filters.location | Filters.attachment, dialog_dontknow)])

    dp.add_handler(dialog)
    dp.add_handler(CommandHandler("start", greet_user))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()


#if __name__ == "__main__":'''
#    main()
st.code(code,language='python')