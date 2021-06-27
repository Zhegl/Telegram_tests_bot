# By Aleksandr Zheglov
from telegram.ext import Updater, Filters, CallbackContext, CommandHandler, MessageHandler
from telegram.ext import *
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from tests_save import *

users = {}
count_of_test = {}


def chat(update, context):
    try:
        print(update.message.text)
        if 'В меню' in update.message.text or '/start' in update.message.text:
            meny_keyboard = [['Тесты'], ['Топ игроков', 'Создать тест']]
            meny_markup = ReplyKeyboardMarkup(meny_keyboard, one_time_keyboard=False)
            update.message.reply_text("Выберите, что хотите сделать", reply_markup=meny_markup)
        elif 'Тесты' in update.message.text:
            testslist = open('tests.list', 'rt').readlines()
            testslist_str = ''
            for i in range(len(testslist)):
                testslist_str += str(i + 1) + ". " + testslist[i] + '\n'
            meny_keyboard = [['🔙 В меню']]
            meny_markup = ReplyKeyboardMarkup(meny_keyboard, one_time_keyboard=False)
            update.message.reply_text(testslist_str + "Введите номер теста", reply_markup=meny_markup)
        elif update.message.text.isdigit():
            testslist = open('tests.list', 'rt').readlines()
            if 0 < int(update.message.text) <= len(testslist):
                users[update.message.from_user.id] = load_test(testslist[int(update.message.text) - 1])
                count_of_test[update.message.from_user.id] = [0, 0]
            else:
                update.message.reply_text("❗Номер теста введен не верно")
        print(users)
        if update.message.from_user.id in users.keys():

            id = update.message.from_user.id
            num = count_of_test[update.message.from_user.id][0]
            if count_of_test[update.message.from_user.id][0] != 0:

                if '1. ' in update.message.text and users[update.message.from_user.id][1][
                    count_of_test[update.message.from_user.id][0] - 1] == '1':
                    count_of_test[update.message.from_user.id][1] += 1
                if '2. ' in update.message.text and users[update.message.from_user.id][1][
                    count_of_test[update.message.from_user.id][0] - 1] == '2':
                    count_of_test[update.message.from_user.id][1] += 1
                if '3. ' in update.message.text and users[update.message.from_user.id][1][
                    count_of_test[update.message.from_user.id][0] - 1] == '3':
                    count_of_test[update.message.from_user.id][1] += 1
                if '4. ' in update.message.text and users[update.message.from_user.id][1][
                    count_of_test[update.message.from_user.id][0] - 1] == '4':
                    count_of_test[update.message.from_user.id][1] += 1
            count_of_test[update.message.from_user.id][0] += 1
            if count_of_test[update.message.from_user.id][0] <= len(users[update.message.from_user.id][1]):
                meny_keyboard = list(map(lambda x: [x], users[id][3][num]))
                print(meny_keyboard)
                meny_markup = ReplyKeyboardMarkup(meny_keyboard, one_time_keyboard=False)
                update.message.reply_text(users[id][2][num], reply_markup=meny_markup)
            else:
                ln = len(users[update.message.from_user.id][1])
                del (users[update.message.from_user.id])
                meny_keyboard = [['🔙 В меню']]
                meny_markup = ReplyKeyboardMarkup(meny_keyboard, one_time_keyboard=False)
                update.message.reply_text("Поздравляем\nВы набрали " + str(count_of_test[update.message.from_user.id][1]) + " баллов из " + str(ln), reply_markup=meny_markup)
    except Exception:
        update.message.reply_text("❗Что то пошло не так!\nВозможно вы ввели что-то неправильно" )
def main():
    updater = Updater('TOKEN', use_context=True)
    dp = updater.dispatcher
    text_hadler = MessageHandler(Filters.text, chat)
    dp.add_handler(text_hadler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
