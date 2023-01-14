import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove
bot = telebot.TeleBot('5907921763:AAHApILqIHcvZ2kE3rI1ZhrOfMNNGEWq44s')


@bot.message_handler(commands=['start'])
def start_message(message):
    global item1, reply_markup
    bot.send_message(message.chat.id, "Привет, тебя заинтересовал мой бот, который будет показывать тебе всю мою жизнь при помощи моей музыки? \n Жми на кнопку 'Да!!!', и я пришлю тебе мою самую первую песню, под которую я начал грустить после того, как мои чувства отвергли")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Да!!!")
    markup.add(item1)
    bot.send_message(message.chat.id, 'жмакай на "Да!!!"', reply_markup=markup)
    if item1==1:
        item1 = reply_markup = types.ReplyKeyboardRemove()






@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Да!!!":
        bot.send_message(message.chat.id,"Спасибо тебе, что заинтересовался моим музыкальным вкусом в переломный момент.\n Сейчас я тебе отошлю песню, которая помогала мне справляться со стрессом", reply_markup=ReplyKeyboardRemove())
        audio = open(r'C:\Users\Герундий\Desktop\песня с бота\Softcore(speed up).m4a', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Давай", callback_data="писька")
        keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Продолжим? Перед чтением моей истории, включи музыку и запасись вкусняшками:)", reply_markup=keyboard)


@bot.callback_query_handler(func = lambda call:True)
def callback(call):
    if call.data == 'писька':
        kb = types.InlineKeyboardMarkup()
        callback_bt = types.InlineKeyboardButton(text = 'Далее ->', callback_data = 'писька1')
        kb.add(callback_bt)
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = "Очень хорошо, давай ебанём историю со мной!", reply_markup=kb)
    if call.data == 'писька1':
        kb1 = types.InlineKeyboardMarkup()
        callback_bt1 = types.InlineKeyboardButton(text='Жми далее, как будешь готов', callback_data='писька2')
        kb1.add(callback_bt1)
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = "Началось всё с того, что 18 марта 2022 года утром в пятницу я подержал, ей дверь в школу. \n Она мне не особо сильно нравилась, поэтому я не обратил на неё особого внимания. Но после того, как она мне написала вечером моя жизнь полностью изменилась", reply_markup=kb1)
    if call.data == 'писька2':
        kb2 = types.InlineKeyboardMarkup()
        callback_bt2 = types.InlineKeyboardButton(text='Далее ->', callback_data='писька3')
        kb2.add(callback_bt2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text = "Далее мы с ней очень много времени проводили вместе, гуляли, общались, и я влюбился.\n Это произошло внезапно, но взаимностью она мне так и не ответила, от чего я много страдал морально, не мог справиться с депрессией.", reply_markup = kb2)
    if call.data == 'писька3':
        kb3 = types.InlineKeyboardMarkup()
        callback_bt3 = types.InlineKeyboardButton(text='Далее ->', callback_data='писька4')
        kb3.add(callback_bt3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Наше общение постоянно заканачивалось ссорами, а порой даже прекращением общения на 2 и более недели. \n В период нашего "не общения" я безумно сильно страдал, но друзья меня выручали, поэтому мне становилось только легче, но избавиться от мыслей насчёт неё я не мог. Она была незаменимой частью в моей жизни, она очень сильно повлияла на моё  дальнейшее поведение, во многом поменяла взгляды на мою жизнь. \n Однажды настал переломный момент в нашей истории, когда 2 мая я позвал её в киноху, но она отменила встречу, мол, пошла уже с мамой. \n Я пошёл гулять с друзьями, и нас увидела Соня, её подруга. \n Её подруга завела разговаор, якобы я с ней будто не общаюсь, потому что всегда были вместе. ', reply_markup=kb3)
    if call.data == 'писька4':
        kb4 = types.InlineKeyboardMarkup()
        callback_bt4 = types.InlineKeyboardButton(text='Далее ->', callback_data='писька5')
        kb4.add(callback_bt4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Я решил зацепиться за данную тему. \n Когда я сказал, что и вправду наше общение стало ничтожно малым, на что получил от неё довольно резкий ответ, что у неё ко мне пропали полностью чувства. \n После этого мой мир рухнул. Я забухал. Мне было ужасно', reply_markup = kb4)
    if call.data == 'писька5':
        kb5 = types.InlineKeyboardMarkup()
        callback_bt5 = types.InlineKeyboardButton(text='Далее ->', callback_data='писька6')
        kb5.add(callback_bt5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Прошло 5 месяцев. \n Я про неё почти забыл, и вот, решил пойти погулять с нашими общими подругами. Так получилось, что её общая подруга побежала к ней и всё рассказала про меня, что я классный тип. \n Она решила извиниться передо мной и начать всё заново', reply_markup=kb5)
    if call.data == 'писька6':
        kb6 = types.InlineKeyboardMarkup()
        callback_bt6 = types.InlineKeyboardButton(text='Далее ->', callback_data='писька7')
        kb6.add(callback_bt6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= '30 сентября 2022 года мы заново начали общаться. \n Мы опять гуляли вместе, обнимались много, наше общение изменилось. Месяц тусили, думал, что у нас взаимные чувства. Но судьба повернулась ко мне спиной', reply_markup = kb6)
    if call.data == 'писька7':
        kb7 = types.InlineKeyboardMarkup()
        callback_bt7 = types.InlineKeyboardButton(text='Далее ->', callback_data='писька8')
        kb7.add(callback_bt7)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Она начала всячески напоминать мне, что мы с ней всего лишь друзья и отталкивала меня. \n 29 октября я сидел у репетитора по русскому, она позвала меня в киноху. От дома репетитора до кинотеатра 30 минут. Я бежал изо всех сил, было холодно, но я всё-таки добежал до кинотеатра. \n Но вот незадача, она была с пацаном и пятью девочками. Было видно, что она меня избегала.', reply_markup = kb7)
    if call.data == 'писька8':
        kb8 = types.InlineKeyboardMarkup()
        callback_bt8 = types.InlineKeyboardButton(text='Далее ->', callback_data='писька9')
        kb8.add(callback_bt8)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Заходим в зал, мы сели так, что я был далеко от неё, поэтому мне не удалось с ней поговорить. \n Когда до дома шли, она была холодна ко мне. ', reply_markup= kb8)
    if call.data == 'писька9':
        kb9 = types.InlineKeyboardMarkup()
        callback_bt9 = types.InlineKeyboardButton(text='Далее ->', callback_data='писька10')
        kb9.add(callback_bt9)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= 'Ночью она мне написала, что между нами ничего не может быть, лучше мне не идти к ней на днюху. \n Я опять умер внутри, думал, что всё окончено. \n Начал заниматься музыкой, углубился в монтаж, но забыть мне её не удалось', reply_markup = kb9)
    if call.data == 'писька10':
        kb10 = types.InlineKeyboardMarkup()
        callback_bt10 = types.InlineKeyboardButton(text='Подвести итоги', callback_data='писька11')
        kb10.add(callback_bt10)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= '7 ноября я решил поздравить её с днюхой, подарил огромный букет цветов из 25 штук. \n Она приняла этот букет, сделала вид, что ей безумно всё понравилось и так и не общалась со мной более', reply_markup=kb10)
    if call.data == 'писька11':
        kb11 = types.InlineKeyboardMarkup()
        callback_bt11 = types.InlineKeyboardButton(text='Вернуться в начало', callback_data='писька1')
        kb11.add(callback_bt11)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Подведя итоги, хотелось бы сказать, что я влил всю свою душу в этого бота. \n Я очень сильно хочу, чтобы ты с достоинством отнёсся к моей истории и обучился на моих ошибках. Удачи тебе, целую;)', reply_markup = kb11)



bot.polling(none_stop=True)




