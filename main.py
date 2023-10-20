import telebot
from telebot import custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State

state_storage = StateMemoryStorage()
# Р’СЃС‚Р°РІРёС‚СЊ СЃРІРѕР№ С‚РѕРєРµС‚ РёР»Рё РѕСЃС‚Р°РІРёС‚СЊ РєР°Рє РµСЃС‚СЊ, С‚РѕРіРґР° РјС‹ СЃРѕР·РґР°РґРёРј РµРіРѕ СЃР°РјРё
bot = telebot.TeleBot("6588467550:AAGcZlGuao3OtqlzoIBWo_MnTzeJkrvz0FM",
                      state_storage=state_storage, parse_mode='Markdown')


class PollState(StatesGroup):
    name = State()
    age = State()


class HelpState(StatesGroup):
    wait_text = State()


text_poll = "Р°РЅРєРµС‚Р°"  # РњРѕР¶РЅРѕ РјРµРЅСЏС‚СЊ С‚РµРєСЃС‚
text_button_1 = "РїРµСЃРЅСЏ"  # РњРѕР¶РЅРѕ РјРµРЅСЏС‚СЊ С‚РµРєСЃС‚
text_button_2 = "С†РёС‚Р°С‚Р°"  # РњРѕР¶РЅРѕ РјРµРЅСЏС‚СЊ С‚РµРєСЃС‚
text_button_3 = "РІРёРґРµРѕ"  # РњРѕР¶РЅРѕ РјРµРЅСЏС‚СЊ С‚РµРєСЃС‚

menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_poll,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    )
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_2,
    ),
    telebot.types.KeyboardButton(
        text_button_3,
    )
)


@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    bot.send_message(
        message.chat.id,
        'РџСЂРёРІРµС‚РёРє! Р§РµРј Р·Р°Р№РјС‘РјСЃСЏ?',  # РњРѕР¶РЅРѕ РјРµРЅСЏС‚СЊ С‚РµРєСЃС‚
        reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_poll == message.text)
def first(message):
    bot.send_message(message.chat.id,
                     'Р—Р°РјРµС‡Р°С‚РµР»СЊРЅРѕ! РљР°Рє *С‚РµР±СЏ* _Р·РѕРІСѓС‚_?')  # РњРѕР¶РЅРѕ РјРµРЅСЏС‚СЊ С‚РµРєСЃС‚
    bot.set_state(message.from_user.id, PollState.name, message.chat.id)


@bot.message_handler(state=PollState.name)
def name(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text
    bot.send_message(message.chat.id, 'РљСЂСѓС‚Рѕ! _РўРІРѕР№_ `РІРѕР·СЂР°СЃС‚?`')  # РњРѕР¶РЅРѕ РјРµРЅСЏС‚СЊ С‚РµРєСЃС‚
    bot.set_state(message.from_user.id, PollState.age, message.chat.id)


@bot.message_handler(state=PollState.age)
def age(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = message.text
    bot.send_message(message.chat.id, 'Р‘Р»Р°РіРѕРґР°СЂСЋ Р·Р° СѓС‡Р°СЃС‚РёРµ!',
                     reply_markup=menu_keyboard)  # РњРѕР¶РЅРѕ РјРµРЅСЏС‚СЊ С‚РµРєСЃС‚
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "I know that you've never been this high Promise, baby, I 'll take you to heaven if you want it I 'll take you to heaven if you die _Chase Atlantic - Slide_ ", reply_markup=menu_keyboard)  # РњРѕР¶РЅРѕ РјРµРЅСЏС‚СЊ С‚РµРєСЃС‚ \ \


@ bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command(message):
    bot.send_message(message.chat.id,
                     "РЎР»РѕР¶РЅРµРµ РІСЃРµРіРѕ РЅР°С‡Р°С‚СЊ РґРµР№СЃС‚РІРѕРІР°С‚СЊ, РІСЃС‘ РѕСЃС‚Р°Р»СЊРЅРѕРµ Р·Р°РІРёСЃРёС‚ С‚РѕР»СЊРєРѕ РѕС‚ СѓРїРѕСЂСЃС‚РІР°",
                     reply_markup=menu_keyboard)  # РњРѕР¶РЅРѕ РјРµРЅСЏС‚СЊ С‚РµРєСЃС‚


@bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "[Clavier](https://youtu.be/kMi2YVTpw6o?si=CMHWz4fDd4jJJ1V6)",
                     reply_markup=menu_keyboard)  # РњРѕР¶РЅРѕ РјРµРЅСЏС‚СЊ С‚РµРєСЃС‚


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()