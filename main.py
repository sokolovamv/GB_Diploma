from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("equations", equations_command))
app.add_handler(CommandHandler("calculations", calculations_command))
app.add_handler(CommandHandler("inequalities", inequalities_command))
app.add_handler(CommandHandler("plots", plots_command))
app.add_handler(CommandHandler("probabilities", probabilities_command))
app.add_handler(CommandHandler("progressions", progressions_command))
app.run_polling()
# Работа до прерывания
app.updater.idle()


