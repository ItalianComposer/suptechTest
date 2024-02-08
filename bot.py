from telegram.ext import Updater, MessageHandler, Filters

# Задаем функцию-обработчик сообщений
def echo(update, context):
    # Отправляем обратно полученное сообщение
    update.message.reply_text(update.message.text)

def main():
    # Токен бота
    token = "BOT_TOKEN"
    # Создаем объект updater
    updater = Updater(token, use_context=True)
    # Получаем объект диспетчера из updater
    dp = updater.dispatcher
    # Добавляем обработчик сообщений типа MessageHandler с фильтром текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    # Запускаем бота
    updater.start_polling()
    # Ждем завершения работы бота
    updater.idle()

if __name__ == '__main__':
    main()
