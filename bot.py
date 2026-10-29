from google import genai
import telebot

TELEGRAM_TOKEN = "9222964350:AAHZqTwKuGhB5Qw7O7eal_C3SpY_qXHFqeY"
GEMINI_API_KEY = "AQ.Ab8RN6LbLXWwGCgF66BCmawP7RJLYKoIRz8ciGOgQ_m9WltYGg"

ai_client = genai.Client(api_key=GEMINI_API_KEY)
bot = telebot.TeleBot(9222964350:AAHZqTwKuGhB5Qw7O7eal_C3SpY_qXHFqeY)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
  try:
    bot.send_chat_action(message.chat.id, "typing")
    response = ai_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message.text,
    )
    bot.reply_to(message, response.text)
  except Exception as e:
    bot.reply_to(
        message, "Произошла ошибка при обработке запроса. Попробуйте позже."
    )


print("Бот запущен!")
bot.infinity_polling()

