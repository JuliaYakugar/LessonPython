from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from Less_09_02_bot_commans import *

app = ApplicationBuilder().token("5693013331:AAFoFfa2MAlCjR-4Q8JFjwcRuPNmSH5Hwao").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("del", del_command))

print('server start')

app.run_polling()